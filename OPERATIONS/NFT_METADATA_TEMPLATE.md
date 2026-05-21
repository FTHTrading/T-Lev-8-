# MTI NFT Metadata Template
## TROPTIONS Real Estate Collection

---

## How to Use This Template

1. **Replace placeholders** with your actual data
2. **Pin to IPFS** using Pinata or local Kubo node
3. **Update baseUri** in `scripts/mint_tokens_and_nfts.js`
4. **Mint NFTs** using the minting script

---

## Token #1 Example (Replace for each property)

```json
{
  "name": "MTI Property #001 — Atlanta Downtown Condo",
  "description": "Fractional ownership of a 2-bedroom condo in downtown Atlanta. Revenue from short-term rentals distributed to token holders. World Cup 2026 premium location.",
  "image": "ipfs://QmYourPropertyImageHashHere",
  "attributes": [
    {
      "trait_type": "Property Type",
      "value": "Residential Condo"
    },
    {
      "trait_type": "Location",
      "value": "Atlanta, GA"
    },
    {
      "trait_type": "Distance to Stadium",
      "value": "0.8 miles"
    },
    {
      "trait_type": "Total Shares",
      "value": "10,000"
    },
    {
      "trait_type": "Share Price",
      "value": "100 TROPTIONS"
    },
    {
      "trait_type": "Expected Yield",
      "value": "8-12% annually"
    },
    {
      "trait_type": "World Cup 2026 Ready",
      "value": "Yes"
    },
    {
      "trait_type": "Rental Platform",
      "value": "Airbnb / VRBO"
    }
  ],
  "properties": {
    "address": "123 Peachtree St NE, Atlanta, GA 30309",
    "square_feet": 1200,
    "bedrooms": 2,
    "bathrooms": 2,
    "year_built": 2018,
    "appraisal_value_usd": 450000,
    "tokenized_value": "1000000 TROPTIONS",
    "legal_entity": "MTI Atlanta LLC (Wyoming Series)",
    "property_manager": "TROPTIONS Property Management",
    "insurance": "TokenShield Coverage",
    "blockchain": "XRPL",
    "issuer": "rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ",
    "ipfs_deed": "ipfs://QmYourDeedDocumentHashHere",
    "apostle_proof": "ipfs://QmYourApostleChainHashHere"
  },
  "external_url": "https://troptionslive.unykorn.org/property/001",
  "animation_url": null,
  "background_color": "D4AF37"
}
```

---

## Token #2 — Tradeline Example

```json
{
  "name": "MTI Tradeline #002 — Commercial Strip Mall",
  "description": "Revenue-sharing tradeline for a commercial strip mall in Atlanta suburbs. Monthly rent payments distributed as stablecoin yield to holders.",
  "image": "ipfs://QmYourPropertyImageHashHere",
  "attributes": [
    {
      "trait_type": "Property Type",
      "value": "Commercial Retail"
    },
    {
      "trait_type": "Location",
      "value": "Atlanta Suburbs"
    },
    {
      "trait_type": "Total Units",
      "value": "12"
    },
    {
      "trait_type": "Occupancy Rate",
      "value": "94%"
    },
    {
      "trait_type": "Monthly Rent Roll",
      "value": "$18,500"
    },
    {
      "trait_type": "Token Type",
      "value": "Tradeline"
    },
    {
      "trait_type": "Yield Distribution",
      "value": "Monthly USDC"
    }
  ],
  "properties": {
    "address": "456 Buford Hwy, Atlanta, GA 30345",
    "square_feet": 15000,
    "units": 12,
    "parking_spaces": 48,
    "appraisal_value_usd": 1200000,
    "tokenized_value": "2500000 TROPTIONS",
    "monthly_yield_usd": 15540,
    "annual_yield_pct": 15.5,
    "lease_terms": "NNN, 5-year average",
    "anchor_tenant": "Community Grocery",
    "blockchain": "XRPL",
    "issuer": "rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ"
  },
  "external_url": "https://troptionslive.unykorn.org/tradeline/002"
}
```

---

## Token #3 — Build Token (Representation of Ecosystem)

```json
{
  "name": "TROPTIONS Build Token #003",
  "description": "Governance token representing contribution to the TROPTIONS ecosystem. Holders receive fee share from Exchange OS and priority access to new features.",
  "image": "ipfs://QmYourBuildTokenImageHashHere",
  "attributes": [
    {
      "trait_type": "Token Type",
      "value": "Governance"
    },
    {
      "trait_type": "Voting Power",
      "value": "1 per token"
    },
    {
      "trait_type": "Fee Share",
      "value": "0.5% of Exchange OS volume"
    },
    {
      "trait_type": "Staking Reward",
      "value": "5% APY in USDC"
    },
    {
      "trait_type": "Ecosystem",
      "value": "TROPTIONS"
    }
  ],
  "properties": {
    "total_supply": "50000000",
    "circulating_supply": "10000000",
    "burn_address": "rrrrrrrrrrrrrrrrrrrrrhoLvTp",
    "blockchain": "XRPL",
    "issuer": "rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ",
    "exchange_os": "https://troptionslive.unykorn.org/exchange-os",
    "governance_forum": "https://troptions.unykorn.org/governance"
  },
  "external_url": "https://troptions.unykorn.org/build-token"
}
```

---

## Batch Upload Script

```javascript
// Pin all metadata JSONs to IPFS
const pinataSDK = require('@pinata/sdk');
const pinata = pinataSDK('YOUR_API_KEY', 'YOUR_SECRET_KEY');

const fs = require('fs');
const path = require('path');

async function pinMetadata() {
  const metadataDir = './metadata';
  const files = fs.readdirSync(metadataDir);
  
  for (const file of files) {
    if (file.endsWith('.json')) {
      const filePath = path.join(metadataDir, file);
      const result = await pinata.pinFileToIPFS(fs.createReadStream(filePath), {
        pinataMetadata: {
          name: `MTI-${file}`,
        },
      });
      console.log(`Pinned ${file}: ${result.IpfsHash}`);
    }
  }
}

pinMetadata().catch(console.error);
```

---

## Directory Structure

```
nft-metadata/
├── metadata/
│   ├── 001-atlanta-condo.json
│   ├── 002-strip-mall.json
│   ├── 003-build-token.json
│   └── ... (one per token)
├── images/
│   ├── 001-property.jpg
│   ├── 002-property.jpg
│   └── ...
├── deeds/
│   ├── 001-deed.pdf
│   └── ...
└── scripts/
    ├── pin-to-ipfs.js
    └── verify-metadata.js
```

---

## Verification Checklist

Before minting:
- [ ] All JSON files valid (use JSONLint)
- [ ] Images pinned to IPFS
- [ ] Deeds pinned to IPFS
- [ ] Metadata pinned to IPFS
- [ ] baseUri updated in minting script
- [ ] Issuer funded with ≥11 XRP
- [ ] Trust lines created for new tokens
- [ ] Transfer fees set correctly
- [ ] Legal wrapper verified (LLC, Series, etc.)

---

*Document:* `T-Lev-8-/OPERATIONS/NFT_METADATA_TEMPLATE.md`  
*Author:* DONK AI for TROPTIONS  
*Date:* 2026-05-21
