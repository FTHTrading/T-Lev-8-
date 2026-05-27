# Aurora / VEX (\$VEX) — White Paper vs TROPTIONS Built Stack

**Source:** VEX White Paper v1.0 draft 3.7 (2026-04-05) — extracted to `STRATEGIC/VEX_WHITEPAPER_EXTRACT.txt`  
**Aurora portal:** https://aurora.unykorn.org (GitHub: `FTHTrading/aurora-site`)

---

## Executive summary

Judson’s white paper describes a **full housing utility protocol** (SEO + R2O + DAO + oracle settlement + sandbox KYC). TROPTIONS has already built **most of the horizontal infrastructure** that protocol needs — mint, exchange, stablecoins, XRPL, AI, proof, compliance gates, event commerce — but **not** the VEX-specific Solana programs (SEO repayment, R2O Risk Reward escrow, property FMV oracle on-chain).

**Rough completion:** ~**55–65%** of total technical surface area (infrastructure-heavy). ~**25–35%** of VEX-specific product surface (contracts + DApp + production oracles).

---

## White paper module map

| # | VEX requirement (WP §) | TROPTIONS / Aurora asset | Status | Notes |
|---|---------------------------|--------------------------|--------|-------|
| 1 | SPL utility token, Meteora launch (§9, §13) | `solana-launcher`, `launch.unykorn.org`, Meteora/Jupiter in stack doc | **Built** | \$VEX mint is configuration, not greenfield |
| 2 | SEO on-chain + repayment in \$VEX (App A, §4.6) | `T-Build` SEO routes + placeholders; `rwa-realestate` FTH layer | **Partial** | Pseudocode in WP; no deployed Anchor `VEX_seo` |
| 3 | R2O option + vesting + Risk Reward algo (App B, §4.6) | `T-Build` R2O escrow placeholders; risk engine | **Partial** | FMV “AI algorithm” = needs oracle + policy engine |
| 4 | Oracle USD↔\$VEX settlement (§2, §4.6) | Chainlink refs in WP; DONK/x402 + PayOps in `troptions` | **Partial** | Property FMV oracle not production |
| 5 | Property registry / title linkage (§4.6) | `rwa-realestate` Truth Engine + County Recorder oracle | **Partial** | Contracts compile; feeds not wired |
| 6 | KYC/AML sandbox (§15) | `kycOnboardingEngine`, T-Build risk CRITICAL on missing provider | **Partial** | Pattern exists; live Sumsub/Persona TBD |
| 7 | Sponsor origination rewards (§5.1) | Sponsor tiers, PayOps, `troptionslive` QR merchant OS | **Built** | Map sponsor fees to \$VEX grants |
| 8 | Professional service incentives (§5.2) | x402 receipts, Apostle 7332, diligence fees | **Built** | Per-service ATP/x402, not pooled treasury |
| 9 | DAO governance, vote-escrow stake (§7, §10) | `TVEXGateManager`, governance JSON, Launch Committee | **Partial** | 8 gates on-chain; full DAO UI not shipped |
| 10 | DApp nationwide scaling (§6.2) | `T-Build` Partner Launch OS, deal room | **Partial** | Shell + gates; SEO/R2O wizards stubbed |
| 11 | Compliance sandbox + counsel kill switch (§15) | `FTHEnforcer.sol`, `TVEXGateManager`, Master Agreement v1.3 | **Built** | Sepolia deploy pending `.env` |
| 12 | No pooled treasury / direct fees (§Exec) | x402 + sponsor rails align | **Built** | Matches TROPTIONS negotiation position |
| 13 | TTN / education / community (§11–12) | `troptionslive.unykorn.org/sports`, `fthedu` | **Built** | WC26 Atlanta anchor |
| 14 | XRPL settlement / liquidity (implied multi-rail) | `troptions` XRPL scripts, `Troptions-L1` bridge-xrpl, Exchange OS | **Built** | Sub-cent settlement path documented |
| 15 | Stablecoin rails (USDC/USDT) | `fth-stablecoin-rail`, USDF multi-chain, vault contracts | **Built** | Production wiring per partner |
| 16 | AI integration (FMV, compliance, marketing) | Finn/needai, DONK, x402 gateway, Atlas RAG | **Built** | Needs domain-tuned FMV model for R2O |
| 17 | Proof / audit trail | Apostle Chain 7332, IPFS, Proof Room engines | **Built** | Court-admissible anchoring pattern |
| 18 | Charity / impact layer | `impact.unykorn.org`, auto-give % (GivBux overlap) | **Partial** | Landing only until Pages live |

---

## What “Aurora” is in TROPTIONS terms

| Name | Role |
|------|------|
| **VEX / \$VEX** | Partner white-paper protocol (housing SEO/R2O) |
| **Aurora** | TROPTIONS-owned RWA + housing vertical (`aurora.unykorn.org`) |
| **rwa-realestate** | Truth → TEV → FTH + T-VEX-8 gates (Ethereum/Sepolia today) |
| **T-Build** | Partner Launch OS (mint, compliance, SEO/R2O UI stubs) |
| **Reserve path** | SOLO `$AURORA` if partner walks — same infra, different token |

Aurora is **not** a second greenfield stack; it is the **branded front door** to existing TROPTIONS infrastructure with housing-specific copy and gate enforcement.

---

## Critical gap list (VEX-specific)

1. **Anchor programs:** `VEX_seo`, `r2o_option_escrow`, vote-escrow governance (WP Appendix C) — placeholders only in `T-Build/packages/solana`.
2. **Property FMV oracle:** R2O Risk Reward requires area appreciation model + on-chain params — AI exists; **on-chain binding** does not.
3. **Production KYC provider:** Risk engine flags CRITICAL until Sumsub/Persona/Onfido live.
4. **Sepolia/mainnet gate manager:** Script ready; deploy blocked on `.env`.
5. **Meteora pool + liquidity policy:** Launch config, not autonomous from white paper.
6. **Legal recorded SEO/R2O → minted deed NFT:** Root NFT + IPFS in stack doc; **per-deal pipeline** not automated.

---

## Repos (inventory)

| Repo / path | Relevance |
|-------------|-----------|
| `C:\Users\Kevan\troptions` | PayOps, KYC, proof-room, XRPL scripts, sponsor engine |
| `C:\Users\Kevan\UnyKorn-X402-aws` | x402, Apostle, Stripe on-ramp, revenue ledger |
| `C:\Users\Kevan\solana-launcher` | SPL mint, IPFS metadata, x402 |
| `C:\Users\Kevan\fth-stablecoin-rail` | USDF / multi-chain settlement |
| `C:\Users\Kevan\Troptions-L1` | Rust XRPL bridge, stablecoin, RWA crates |
| `rwa-realestate` | FTH enforcer, gate manager, compliance |
| `T-Build` | Partner OS, risk, gates config |
| `T-VEX-8-` | Legal, deal room, negotiation |

See `T-Build/docs/inventory/FULL_REPO_INVENTORY.md` for file-level detail.

---

## Negotiation leverage (data-backed)

| Claim | Evidence |
|-------|----------|
| Infrastructure vs white paper | `troptionslive` sports commerce **live**; VEX DApp **nascent** per WP disclaimer |
| TROPTIONS owns contracts | Master Agreement Art. 6 + `rwa-realestate` deploy path |
| 8 gates enforceable | `TVEXGateManager.sol` + `pin_to_governance.js` |
| Time already invested | T-Build reuse docs: **~400+ hours** equivalent saved vs greenfield (see `TIME_SAVED_BY_REUSE.md`) |

**Do not send** this comparison table to Judson pre-term-sheet; use internally and in Aurora/GivBux partner decks only.
