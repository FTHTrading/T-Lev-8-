# TROPTIONS Ecosystem Address Registry
**Scope:** All XRPL, Stellar, Ethereum, domain, and transaction identifiers referenced in T-VEX-8 conversations.
**Last Updated:** 2026-05-21
**Security Rule:** This document contains ONLY public addresses. Seeds, private keys, and API secrets are NEVER stored here.

---

## 1. EXECUTIVE SUMMARY

| Network | Wallets | Status |
|---------|---------|--------|
| **XRPL Mainnet** | 6 tracked | Production rails are `rJLMST...` + `rNX4fa...` |
| **XRPL Testnet** | 1 tracked | `rGaiC...` (100 XRP, dev only) |
| **Stellar Mainnet** | 2 tracked | Issuer + Distribution live |
| **Ethereum/Sepolia** | 1 gate manager | Awaiting `.env` deploy |
| **Domains** | 11 active | 6 redirecting, 2 parked, 2 TBD |
| **Ops spend** | 1 | `rfbZz...` — ~12 XRP + RLUSD; seed local (`XRPL_OPS_SEED`) |

---

## 2. XRPL MAINNET WALLET REGISTRY

| # | Address | Name | XRP Balance | Issued Assets | Role | Status |
|---|---------|------|-------------|---------------|------|--------|
| **1** | `rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ` | **Production Issuer** | ~1.20 | TROPTIONS (100M), USDC (175M), USDT (100M), DAI (50M), EURC (50M) | Cold issuer; all IOU obligations; transfer fee collector (25–100 bps) | ⚠️ **UNDERFUNDED** — needs ≥11 XRP |
| **2** | `rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt` | **Distribution & Fee Treasury** | ~3.30 | Receives: ~99.999M TROPTIONS, 174M USDC, 100M USDT, 50M DAI, 50M EURC, LP tokens | AMM operator; fee sweep destination; batch platform fees route here | ⚠️ **UNDERFUNDED** — needs buffer for tx fees |
| **3** | `rBU6exSQHkrTog6n1F5RX8gzcUrXoniGcp` | **AMM Pool** | ~1.01 | LP tokens | TROPTIONS/XRP AMM liquidity pool | 🟡 Operational but low TVL ($7.91) |
| **4** | `rPF2M1QjdVh1hkNgmMMTkT9qMU7tA7Wds3` | **Bootstrap Funnel (legacy)** | ~3.00 | None | Apr 28: sent 3 XRP→`rJLMST`, 5 XRP→`rNX4fa`; received 12 XRP; **not** live issuer | 🔴 **DEPRECATED** — do not mint from this address |
| **5** | `rfbZzM6SGZHbfxrg85vyeKSEMMQCfNXTNw` | **Ops Spend Wallet** | ~12.00 | **RLUSD ~11.82** (limit 1M; balance ~$12) | TrustSet 5/11/2026; 20 XRP inbound; signs via `XRPL_OPS_SEED` | 🟢 **OPS** — not issuer; use for pilots/fees |
| **6** | `rnJrjec2vrTJAAQUTMTjj7U6xdXrk9N4mT` | **External Fund Source** | ~43.8M | Unknown | Exchange-scale account that sent 20 XRP to `rfbZz...` | 🟡 **EXTERNAL** — not under TROPTIONS control |

---

## 3. ISSUED ASSET REGISTRY (XRPL Mainnet)

All assets issued by `rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ`:

| Asset | Code | Supply | Transfer Fee | Status | TrustSet Tx Hash | Issue Tx Hash |
|-------|------|--------|--------------|--------|------------------|---------------|
| **TROPTIONS** | `TROPTIONS` | 100,000,000 | 25 bps (0.25%) | LIVE | — | — |
| **USDC** | `USDC` | 175,000,000 | 0 bps | LIVE | `63225EF5...0613A` | `CD727127...E642` |
| **USDT** | `USDT` | 100,000,000 | 0 bps | LIVE | `01A93483...4241` | `42092147...F6F` |
| **DAI** | `DAI` | 50,000,000 | 0 bps | LIVE | `B14C09D2...8093` | `C0D75DCC...F641` |
| **EURC** | `EURC` | 50,000,000 | 0 bps | LIVE | `37D4C6F7...3E0F` | `FF11D777...60D1` |
| **GOLD** | `GOLD` | — | 50 bps | DRAFT | — | — |
| **GBP** | `GBP` | — | 0 bps | DRAFT | — | — |
| **DONK** | `DONK` | — | 100 bps | DRAFT | — | — |
| **LEGACY** | `LEGACY` | — | 0 bps | DRAFT | — | — |
| **SOVBND** | `SOVBND` | — | 25 bps | DRAFT | — | — |
| **PETRO** | `PETRO` | — | 50 bps | DRAFT | — | — |
| **ATTEST** | `ATTEST` | — | 0 bps | DRAFT | — | — |

---

## 4. TRANSACTION REGISTRY

| Hash | Type | From | To | Amount | Date | Status |
|------|------|------|----|--------|------|--------|
| `8E26321733467C94A1A4291381AA06EA737ACA0EDBF66F6738606B7779DE4F38` | Payment | `rnJrj...` | `rfbZz...` | 20 XRP | ~10 days ago | ✅ `tesSUCCESS` |
| `744B1680A79388A29CC2FFE6220817098B94484E2A086428F584162E87920A7C` | — | — | — | — | — | Referenced in Bithomp data |

**Note:** The 20 XRP payment to `rfbZz...` cost 0.006 XRP in fees and activated the account with Destination Tag 1001.

---

## 5. STELLAR MAINNET

| Address | Role | XLM | Status |
|---------|------|-----|--------|
| `GB4FHGFUTLLMS3SC5RWRK6RYBGDIUQ5NR7IGN5TWAA3QVHULJ34JGEG4` | Stellar Issuer | 5 XLM (funded) | LIVE |
| `GBH4YY6EKSIM3LEHUQHEXFDZKMLON64HKMCB2K7CCOXGNCIVGH5GGVWC` | Stellar Distribution | 15 XLM (funded) | LIVE |

**Stellar ledgers:** 62321764 (issuer), 62321765 (distribution)

---

## 6. TESTNET / DEVNET

| Address | Network | Balance | Purpose |
|---------|---------|---------|---------|
| `rGaiC1bw8uND7Z9XzzpcAWyAuH72p82HES` | XRPL Testnet | 100 XRP | Batch builder testing; `temDISABLED` expected |

---

## 7. LEGACY DOMAIN & REDIRECT REGISTRY

### Live Redirects (301 → TROPTIONS Live Targets)

| Legacy Domain | Redirects To | Status |
|---------------|-------------|--------|
| `troptionsxchange.io` | `https://troptionslive.unykorn.org/exchange-os` | ✅ Active |
| `troptions-university.com` | `https://fthedu.unykorn.org/` | ✅ Active |
| `troptionstelevisionnetwork.tv` | `https://troptionslive.unykorn.org/sports` | ✅ Active |
| `hotrcw.com` | `https://troptionslive.unykorn.org/` | ✅ Active |
| `troptions.io` | `https://troptions.unykorn.org` | ✅ Active |

### Parked (Do Not Redirect — NXDOMAIN)

| Domain | Intended Target | Blocker |
|--------|---------------|---------|
| `therealestateconnections.com` | `aurora.unykorn.org` | Site not deployed |
| `green-n-go.solar` | `impact.unykorn.org` | Site not deployed |

### Internal Infrastructure

| Host | URL | Status |
|------|-----|--------|
| Deal Room | `https://fthtrading.github.io/T-VEX-8-/` | ✅ Live |
| Exchange OS | `https://troptionslive.unykorn.org/exchange-os` | ✅ Live (XRPL mainnet read) |
| Sports / WC26 | `https://troptionslive.unykorn.org/sports` | ✅ Live |
| University | `https://fthedu.unykorn.org/` | ✅ Live |
| Aurora | `https://aurora.unykorn.org` | ⏳ Repo pushed; Pages enable pending |
| Impact | `https://impact.unykorn.org` | ⏳ Repo pushed; Pages enable pending |

---

## 8. SECURITY & SEED STATUS

| Identifier | Type | Status | Action |
|------------|------|--------|--------|
| `FTZjiNL-6TRwRSsIZeWUxvFh83RqFI` | **POTENTIAL SEED / API KEY** | UNVERIFIED | 🔒 **DO NOT PASTE AGAIN** — search local `.env` files only |
| `TXORGJ4-P2K2O-MFVTJA` | **POTENTIAL SEED / API KEY** | UNVERIFIED | 🔒 **DO NOT PASTE AGAIN** — search local `.env` files only |
| `rfbZz...` seed | Family Seed (`sn...`) | UNKNOWN LOCATION | 🟡 Search local files for address match; do not reveal seed content |

---

## 9. RESERVE & TREASURY HEALTH

| Wallet | Current XRP | Minimum Needed | Gap | Priority |
|--------|-------------|------------------|-----|----------|
| `rJLMST...` (Issuer) | ~1.20 | ≥11.00 | **~10 XRP** | **CRITICAL** |
| `rNX4fa...` (Distribution) | ~3.30 | ≥5.00 (tx buffer) | **~2 XRP** | HIGH |
| `rBU6ex...` (AMM) | ~1.01 | ≥1.00 (base) | ~0 | LOW |
| **Total Production Liquid** | **~5.51** | **≥16.00** | **~11 XRP (~$18)** | |

---

## 10. RECOMMENDED ACTIONS

| Priority | Action | Cost | Impact |
|----------|--------|------|--------|
| **1** | Send 10 XRP to `rJLMST...` from `rfbZz...` **(only if you own the seed)** | 0 | Unlocks mainnet issuer operations |
| **2** | Send 2 XRP to `rNX4fa...` from `rfbZz...` **(if owned)** | 0 | Unlocks distribution buffer |
| **3** | If `rfbZz...` is NOT yours, buy 11 XRP and send to `rJLMST...` | ~$18 | Unlocks issuer |
| **4** | Print & send Judson term sheet | Time | **$10K cash** |
| **5** | Commit & push Exchange OS Batch UI | 30 min | Demo surface for all sales |
| **6** | Enable Aurora/Impact GitHub Pages | 2 min | Public subdomains live |

---

## 11. GOVERNANCE SYNC

Update `T-VEX-8-/data/governance-state.json` with this block:

```json
{
 "wallet_registry": {
 "version": "2026-05-21",
 "xrpl_mainnet": {
 "production_issuer": "rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ",
 "distribution_treasury": "rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt",
 "amm_pool": "rBU6exSQHkrTog6n1F5RX8gzcUrXoniGcp",
 "deprecated_default": "rPF2M1QjdVh1hkNgmMMTkT9qMU7tA7Wds3",
 "unknown_ops": "rfbZzM6SGZHbfxrg85vyeKSEMMQCfNXTNw",
 "external_funder": "rnJrjec2vrTJAAQUTMTjj7U6xdXrk9N4mT"
 },
 "stellar_mainnet": {
 "issuer": "GB4FHGFUTLLMS3SC5RWRK6RYBGDIUQ5NR7IGN5TWAA3QVHULJ34JGEG4",
 "distribution": "GBH4YY6EKSIM3LEHUQHEXFDZKMLON64HKMCB2K7CCOXGNCIVGH5GGVWC"
 },
 "testnet": {
 "batch_test": "rGaiC1bw8uND7Z9XzzpcAWyAuH72p82HES"
 },
 "issuer_balance_status": "HALT_INSUFFICIENT_RESERVE",
 "issuer_funding_target_xrp": 11,
 "fee_sweep_wallet": "rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt"
 }
}
```

---

**Document:** `T-VEX-8-/OPERATIONS/WALLET_ADDRESS_REGISTRY.md`
**Classification:** PUBLIC — Address metadata only. No seeds.
**Author:** Compiled from T-VEX-8 thread analysis
**Date:** 2026-05-21
