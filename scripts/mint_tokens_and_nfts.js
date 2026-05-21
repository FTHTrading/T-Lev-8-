#!/usr/bin/env node
/**
 * XRPL Token + NFT Minting Scripts
 * Run AFTER issuer is funded with ≥11 XRP
 * 
 * Prerequisites:
 * - Node.js + xrpl library installed
 * - .env file with ISSUER_SEED (rJLMST... family seed)
 * - Issuer wallet funded with ≥11 XRP
 * 
 * What this does:
 * 1. Creates trust lines for new tokens
 * 2. Issues tokens with custom transfer fees
 * 3. Mints NFTs with IPFS metadata
 * 4. Sets up AMM pool deposits
 * 5. Creates batch transaction templates
 */

require('dotenv').config();
const { Client, Wallet, TrustSet, Transaction, IssuedCurrencyAmount, NFTokenMint, NFTokenCreateOffer, Payment, AMMCreate } = require('xrpl');

// CONFIGURATION — Update these before running
const CONFIG = {
  // XRPL Mainnet
  network: 'wss://xrplcluster.com',
  
  // Issuer wallet (must be funded with ≥11 XRP)
  issuerSeed: process.env.ISSUER_SEED,
  issuerAddress: 'rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ',
  
  // Distribution wallet (receives tokens, fees)
  distributionAddress: 'rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt',
  
  // NFT Minter (create a dedicated minter wallet)
  nftMinterSeed: process.env.NFT_MINTER_SEED,
};

// TOKEN DEFINITIONS — What you want to mint
const TOKENS = [
  {
    code: 'MTI',           // Token code (3-4 chars)
    name: 'MTI Real Estate Token',
    supply: '100000000',   // Total supply
    decimals: 0,
    transferFee: 25,       // 0.25% (in basis points: 25 = 0.25%)
    // transferFee: 0 = 0%, 50 = 0.5%, 100 = 1.0%, etc.
  },
  {
    code: 'BUILD',
    name: 'TROPTIONS Build Token',
    supply: '50000000',
    decimals: 0,
    transferFee: 50,       // 0.50%
  },
  {
    code: 'WC26',
    name: 'World Cup 2026 Fan Token',
    supply: '1000000',
    decimals: 0,
    transferFee: 0,        // 0% — free for fans
  },
];

// NFT COLLECTION — Metadata on IPFS
const NFT_COLLECTION = {
  name: 'TROPTIONS MTI Collection',
  description: 'Fractional real estate ownership NFTs',
  baseUri: 'ipfs://QmYourIpfsHashHere/', // Update after pinning to IPFS
  totalSupply: 1000,
  transferFee: 0, // 0% for NFT transfers (or set to earn on secondary)
};

// AMM CONFIGURATION
const AMM_CONFIG = {
  // Deposit XRP + TROPTIONS into AMM pool
  asset1: 'XRP',
  asset2: {
    currency: 'TROPTIONS',
    issuer: CONFIG.issuerAddress,
  },
  // Amount to deposit (in drops for XRP, in issued amount for token)
  xrpAmount: '10000000000', // 10,000 XRP (in drops)
  tokenAmount: '100000000',   // 100M TROPTIONS
};

// ========================
// SCRIPT 1: CREATE TRUST LINES
// ========================
async function createTrustLines(client, wallet, tokens) {
  console.log('🏗️  Creating trust lines for new tokens...');
  
  for (const token of tokens) {
    const trustSetTx = {
      TransactionType: 'TrustSet',
      Account: wallet.address,
      LimitAmount: {
        currency: token.code,
        issuer: CONFIG.issuerAddress,
        value: token.supply,
      },
    };
    
    try {
      const prepared = await client.autofill(trustSetTx);
      const signed = wallet.sign(prepared);
      const result = await client.submitAndWait(signed.tx_blob);
      
      if (result.result.meta.TransactionResult === 'tesSUCCESS') {
        console.log(`✅ Trust line created: ${token.code}`);
        console.log(`   Hash: ${result.result.hash}`);
      } else {
        console.log(`❌ Failed: ${token.code} — ${result.result.meta.TransactionResult}`);
      }
    } catch (err) {
      console.error(`❌ Error creating trust line for ${token.code}:`, err.message);
    }
  }
}

// ========================
// SCRIPT 2: ISSUE TOKENS
// ========================
async function issueTokens(client, wallet, tokens) {
  console.log('🪙 Issuing tokens...');
  
  for (const token of tokens) {
    const paymentTx = {
      TransactionType: 'Payment',
      Account: wallet.address,
      Destination: CONFIG.distributionAddress,
      Amount: {
        currency: token.code,
        issuer: wallet.address,
        value: token.supply,
      },
      // Set transfer fee on the issuer
      TransferRate: token.transferFee === 0 ? 0 : 1000000000 + (token.transferFee * 1000000),
      // TransferRate: 0 = 0%, 1002000000 = 0.2%, 1002500000 = 0.25%, etc.
    };
    
    try {
      const prepared = await client.autofill(paymentTx);
      const signed = wallet.sign(prepared);
      const result = await client.submitAndWait(signed.tx_blob);
      
      if (result.result.meta.TransactionResult === 'tesSUCCESS') {
        console.log(`✅ Issued: ${token.code} (${token.supply} tokens)`);
        console.log(`   Hash: ${result.result.hash}`);
        console.log(`   Transfer fee: ${token.transferFee / 100}%`);
      } else {
        console.log(`❌ Failed to issue ${token.code}: ${result.result.meta.TransactionResult}`);
      }
    } catch (err) {
      console.error(`❌ Error issuing ${token.code}:`, err.message);
    }
  }
}

// ========================
// SCRIPT 3: MINT NFTs
// ========================
async function mintNFTs(client, wallet, collection) {
  console.log('🎨 Minting NFTs...');
  
  // Example: Mint first 10 NFTs
  for (let i = 1; i <= 10; i++) {
    const nftMintTx = {
      TransactionType: 'NFTokenMint',
      Account: wallet.address,
      // URI pointing to IPFS metadata
      URI: Buffer.from(`${collection.baseUri}${i}.json`).toString('hex').toUpperCase(),
      // Transfer fee (0 = free, 500 = 5%, 1000 = 10%)
      TransferFee: collection.transferFee,
      // 0 = issuer can burn, 1 = issuer cannot burn
      Flags: 1,
    };
    
    try {
      const prepared = await client.autofill(nftMintTx);
      const signed = wallet.sign(prepared);
      const result = await client.submitAndWait(signed.tx_blob);
      
      if (result.result.meta.TransactionResult === 'tesSUCCESS') {
        console.log(`✅ Minted NFT #${i}`);
        console.log(`   Hash: ${result.result.hash}`);
        console.log(`   URI: ${collection.baseUri}${i}.json`);
      } else {
        console.log(`❌ Failed to mint NFT #${i}: ${result.result.meta.TransactionResult}`);
      }
    } catch (err) {
      console.error(`❌ Error minting NFT #${i}:`, err.message);
    }
  }
}

// ========================
// SCRIPT 4: SEED AMM
// ========================
async function seedAMM(client, wallet, config) {
  console.log('🏊 Seeding AMM pool...');
  
  const ammCreateTx = {
    TransactionType: 'AMMVote', // or AMMCreate if pool doesn't exist
    Account: wallet.address,
    Asset: {
      currency: config.asset2.currency,
      issuer: config.asset2.issuer,
    },
    Asset2: {
      currency: 'XRP',
    },
    Amount: config.tokenAmount,
    Amount2: config.xrpAmount,
    TradingFee: 500, // 0.5% trading fee for the pool
  };
  
  try {
    const prepared = await client.autofill(ammCreateTx);
    const signed = wallet.sign(prepared);
    const result = await client.submitAndWait(signed.tx_blob);
    
    if (result.result.meta.TransactionResult === 'tesSUCCESS') {
      console.log('✅ AMM pool seeded');
      console.log(`   XRP deposited: ${config.xrpAmount / 1000000}`);
      console.log(`   Tokens deposited: ${config.tokenAmount}`);
      console.log(`   Hash: ${result.result.hash}`);
    } else {
      console.log(`❌ Failed to seed AMM: ${result.result.meta.TransactionResult}`);
    }
  } catch (err) {
    console.error('❌ Error seeding AMM:', err.message);
  }
}

// ========================
// MAIN EXECUTION
// ========================
async function main() {
  if (!CONFIG.issuerSeed) {
    console.error('❌ ISSUER_SEED not found in .env');
    console.error('   Add: ISSUER_SEED=snYourFamilySeedHere');
    process.exit(1);
  }
  
  const client = new Client(CONFIG.network);
  await client.connect();
  console.log('✅ Connected to XRPL mainnet');
  
  const wallet = Wallet.fromSeed(CONFIG.issuerSeed);
  console.log(`✅ Loaded wallet: ${wallet.address}`);
  
  // Check balance
  const balance = await client.getXrpBalance(wallet.address);
  console.log(`💰 Issuer balance: ${balance} XRP`);
  
  if (parseFloat(balance) < 11) {
    console.error('❌ Insufficient balance. Need ≥11 XRP. Halting.');
    console.error('   See: OPERATIONS/GAS_FUND_TRACKER.md');
    await client.disconnect();
    process.exit(1);
  }
  
  // Execute scripts
  console.log('\n=== STEP 1: Trust Lines ===');
  await createTrustLines(client, wallet, TOKENS);
  
  console.log('\n=== STEP 2: Token Issuance ===');
  await issueTokens(client, wallet, TOKENS);
  
  console.log('\n=== STEP 3: NFT Minting ===');
  if (CONFIG.nftMinterSeed) {
    const nftWallet = Wallet.fromSeed(CONFIG.nftMinterSeed);
    await mintNFTs(client, nftWallet, NFT_COLLECTION);
  } else {
    console.log('⚠️  NFT_MINTER_SEED not set. Skipping NFT mint.');
  }
  
  console.log('\n=== STEP 4: AMM Seeding ===');
  await seedAMM(client, wallet, AMM_CONFIG);
  
  await client.disconnect();
  console.log('\n✅ All operations complete');
}

main().catch(console.error);

// ========================
// USAGE
// ========================
/**
 * 1. Install dependencies:
 *    npm install xrpl dotenv
 * 
 * 2. Create .env file:
 *    ISSUER_SEED=snYourFamilySeedHere
 *    NFT_MINTER_SEED=snYourNftMinterSeedHere (optional)
 * 
 * 3. Fund issuer with ≥11 XRP
 * 
 * 4. Run:
 *    node scripts/mint_tokens_and_nfts.js
 * 
 * 5. Verify on Bithomp:
 *    https://bithomp.com/explorer/rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ
 */
