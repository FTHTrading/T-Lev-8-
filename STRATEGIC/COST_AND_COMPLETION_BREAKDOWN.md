# Cost & Completion Breakdown — Aurora / ELEVATE / GivBux-class build

**Purpose:** Explain what is already paid for in sunk engineering, what remains, and order-of-magnitude cost to finish.  
**Not a quote for Judson** — internal + partner (GivBux) planning.

---

## Completion scorecard

| Layer | Weight | % complete | Rationale |
|-------|--------|------------|-----------|
| Legal / deal room / gates | 15% | **90%** | Master Agreement, 8 gates, kill switch, term sheet |
| Solana mint + metadata | 10% | **85%** | Launcher + launch.unykorn.org |
| Exchange + stablecoin rails | 15% | **75%** | Exchange OS live; USDF/XRPL need partner wiring |
| Event commerce + sponsors | 10% | **80%** | troptionslive sports + QR merchant path |
| x402 / Apostle / AI | 15% | **70%** | Gateway built; FMV model needs RE tuning |
| RWA Truth/TEV/FTH (EVM) | 10% | **65%** | Contracts compile; oracles/feeds incomplete |
| LEV8 Anchor (SEO/R2O/DAO) | 20% | **15%** | Placeholders only |
| Housing DApp (end-to-end) | 15% | **25%** | T-Build stubs, no production SEO/R2O flow |

**Weighted overall:** ~**58%** complete toward a GivBux-scale “full system” ask.

---

## Sunk cost (already built) — engineering value

Estimates use internal reuse analysis (`T-Build/docs/build-plan/TIME_SAVED_BY_REUSE.md`) and inventory scan (2026-05-27).

| Asset bucket | Est. hours (equiv.) | Market rate band | Est. sunk value |
|--------------|---------------------|------------------|-----------------|
| troptions monorepo (PayOps, proof, KYC patterns, XRPL scripts) | 1,200–2,000 | $150–250/hr | **$180K–500K** |
| UnyKorn-X402-aws (Apostle, receipts, on-ramp) | 400–800 | $150–250/hr | **$60K–200K** |
| solana-launcher + Pinata + Stripe | 200–400 | $150–200/hr | **$30K–80K** |
| rwa-realestate + T-LEV-8 compliance | 300–500 | $175–275/hr | **$50K–140K** |
| T-Build Partner Launch OS (waves 1–5) | 400–600 | $150–225/hr | **$60K–135K** |
| T-Lev-8- legal/strategic/deal room | 150–250 | legal + eng blend | **$40K–100K** |
| fth-stablecoin-rail + Troptions-L1 (Rust) | 500–1,000 | $175–275/hr | **$85K–275K** |

**Total sunk (range):** ~**$505K – $1.43M** in replacement cost.  
Actual cash spend varies (founder time, contractors, infra). Use as **leverage narrative**, not audited financials.

---

## Remaining work — to reach “white paper complete”

| Workstream | Deliverable | Est. hours | Est. cost @ $200/hr |
|------------|-------------|------------|---------------------|
| Anchor SEO repayment program | Devnet → audit-ready | 120–200 | $24K–40K |
| Anchor R2O escrow + Risk Reward | FMV params + vesting | 150–250 | $30K–50K |
| Property FMV oracle integration | Chainlink + fallback AI | 80–120 | $16K–24K |
| KYC/AML production | Sumsub/Persona + webhooks | 60–100 | $12K–20K |
| Housing DApp v1 | Originate → repay → proof | 200–350 | $40K–70K |
| County/title oracle feeds | 1–2 pilot counties | 100–180 | $20K–36K |
| Meteora launch ops | Pool, liquidity policy | 40–80 | $8K–16K |
| Security audit (Solana programs) | Third-party firm | — | **$40K–120K** |
| Legal opinion / sandbox | Outside counsel | — | **$25K–75K** |

**Remaining eng + audit (ex legal):** ~**$190K – $356K**  
**All-in to production-grade LEV8 protocol:** ~**$255K – $450K** on top of sunk stack.

---

## Ongoing run-rate (monthly, post-launch)

| Item | Low | High |
|------|-----|------|
| Cloudflare + Pages + RPC (Alchemy/Helius) | $500 | $2,500 |
| KYC per active user | usage-based | $2–8/user |
| Apostle / x402 infra | $300 | $1,500 |
| Monitoring + counsel retainer | $2,000 | $8,000 |
| **Total ops** | **~$3K/mo** | **~$14K/mo** |

---

## How close are we?

| Milestone | Status |
|-----------|--------|
| Public deal room + term sheet | **Done** |
| Live sports / exchange surfaces | **Done** |
| Partner gate contract (Sepolia) | **Ready** — needs `.env` deploy |
| First SEO on-chain repayment | **Not started** |
| First R2O with Risk Reward | **Not started** |
| GivBux-style super-app integration | **Architecture only** — no GBUX API |

**Calendar realism:** 8–14 weeks to devnet-complete housing programs with existing team; +8–12 weeks audit/legal if parallelized.

---

## Pricing posture for partners (GivBux / LEV8)

| Model | When to use |
|-------|-------------|
| **Integration fee (Option A)** | $10K non-refundable + fee share — LEV8/Judson path |
| **White-label infra** | $150K–350K build + rev share — public fintech (GivBux) |
| **Per-rail metering** | x402 / ATP per API call — AI + settlement |
| **Sponsor tiers** | $500 / $2.5K / $10K — avoid MOU reimbursement |

Never agree to MOU §1.02-style treasury reimbursement or partner-owned core contracts.
