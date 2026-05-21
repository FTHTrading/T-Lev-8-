# Gas Fund Tracker — XRPL Issuer Funding
**Status:** CRITICAL — Issuer HALTED due to insufficient reserve
**Target:** 11 XRP minimum for issuer operations

---

## Current Balances (Live)

| Wallet | Address | Balance | Needed | Gap | Action |
|--------|---------|---------|--------|-----|--------|
| **Production Issuer** | `rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ` | ~1.20 XRP | ≥11.00 | **~10 XRP** | 🔴 FUND NOW |
| **Distribution** | `rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt` | ~3.30 XRP | ≥5.00 | **~2 XRP** | 🟡 FUND |
| **AMM Pool** | `rBU6exSQHkrTog6n1F5RX8gzcUrXoniGcp` | ~1.01 XRP | ≥1.00 | ~0 | 🟢 OK |
| **Unknown/Mystery** | `rfbZzM6SGZHbfxrg85vyeKSEMMQCfNXTNw` | ~12.00 XRP | N/A | +12 | 🟡 VERIFY OWNERSHIP |
| **External** | `rnJrjec2vrTJAAQUTMTjj7U6xdXrk9N4mT` | ~43.8M | N/A | N/A | 🔴 NOT YOURS |

**Total Production Liquid:** ~5.51 XRP  
**Total Needed:** ≥16.00 XRP  
**Total Gap:** ~11 XRP (~$18 USD at current prices)

---

## Funding Options

### Option A: Use rfbZz... (if you own it)
**Cost:** $0  
**Risk:** LOW (if you hold the seed)

If you have the family seed (`sn...`) for `rfbZz...`:
```bash
# Send 10 XRP to issuer
# Send 2 XRP to distribution
# Keep 0.01 for fees
```

**How to verify ownership:**
1. Check your `.env` files for `rfbZz` or Destination Tag 1001
2. Check your XRPL wallets for a wallet with ~12 XRP
3. If you recognize the activation transaction (20 XRP from rnJrj... ~10 days ago), you may have created it

### Option B: Buy XRP (if rfbZz is NOT yours)
**Cost:** ~$18 USD for 11 XRP  
**Sources:**
- Coinbase
- Kraken
- Binance.US
- Any exchange with XRP

**Steps:**
1. Buy 15 XRP (~$25)
2. Withdraw 10 XRP to `rJLMST...`
3. Withdraw 5 XRP to `rNX4fa...`
4. Done

### Option C: Judson's $10K Integration Fee
**Timeline:** 30 days (if term sheet signed today)  
**Amount:** $10K buys ~6,000 XRP at current prices

This funds everything + seeds the AMM.

---

## What 11 XRP Unlocks

| Feature | XRP Cost | Status |
|---------|----------|--------|
| Create new trust line | 0.2 XRP | ❌ BLOCKED (insufficient reserve) |
| Issue new token | 0.2 XRP | ❌ BLOCKED |
| Mint NFT | 0.2 XRP + minting fee | ❌ BLOCKED |
| Batch transaction | 0.01–0.05 XRP | ❌ BLOCKED |
| AMM deposit | 1.0 XRP + tokens | ❌ BLOCKED |
| Transfer fee collection | 0 XRP (passive) | ✅ Works once trust lines exist |

---

## Quick Check: Do You Own rfbZz...?

**If YES:** You can fund the issuer today for free.  
**If NO:** Buy 11 XRP (~$18) or wait for Judson's $10K.

**To verify:**
1. Open your XRPL wallet app
2. Check if any wallet has ~12 XRP
3. Check if any wallet has RLUSD trust line
4. Check transaction history for Destination Tag 1001

---

## Post-Funding Action Plan

Once issuer has 11+ XRP:

### Immediate (Hour 1)
- [ ] Create trust line for MTI NFT collection
- [ ] Create trust line for new token (if any)
- [ ] Enable mainnet spend in Exchange OS

### Short-term (Day 1)
- [ ] Seed AMM with 10,000 XRP + TROPTIONS (if distribution funded)
- [ ] Set up NFT minter address
- [ ] Create first batch transaction test

### Medium-term (Week 1)
- [ ] Onboard first merchant (transfer fees begin)
- [ ] Execute first Stellar bridge (bridge toll begins)
- [ ] Launch MTI NFT collection

---

*Document:* `OPERATIONS/GAS_FUND_TRACKER.md`  
*Updated:* 2026-05-21  
*Next Review:* After funding or 48 hours
