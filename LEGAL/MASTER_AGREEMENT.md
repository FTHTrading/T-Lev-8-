# MASTER PLATFORM, LAUNCHPAD & TECHNOLOGY INTEGRATION AGREEMENT

**Parties:**
- TROPTIONS, INC. (Wyoming corporation) ("TROPTIONS")
- LEV8 TECHNOLOGIES, LLC (Wyoming limited liability company) ("LEV8")

**Effective Date:** [PENDING EXECUTION]

**Status:** Draft v1.3 — Option A + TROPTIONS contract ownership — Awaiting independent securities counsel review

---

## RECITALS

A. TROPTIONS operates token launch, exchange, and event-commerce infrastructure. LEV8 develops the ELEVATE ($LEV8) consumptive-utility protocol for SEO/R2O settlement.

B. The parties previously circulated a non-binding MOU dated May 16, 2026. **Any MOU term describing a "reimbursement" of platform funds from issuer treasury, marketing budget, Day-1 trading proceeds, or "available project funds" is rejected and superseded** by this Agreement.

C. The parties intend a **fee-for-service and revenue-share** relationship, not a guaranteed-return investment, demand loan, or wash-trading arrangement.

---

## ARTICLE 1 — EXCLUSIVITY

1.1 **Launchpad Exclusivity.** For six (6) months following the Public Sale Date, LEV8 shall use TROPTIONS as its exclusive Solana launchpad for initial liquidity and primary launchpad marketing, subject to Section 1.3.

1.2 **Right of First Refusal.** For twelve (12) months following Public Sale, TROPTIONS has a right of first refusal on any Additional Token issued by LEV8 on terms no less favorable than any third-party offer.

1.3 **Carve-Outs.** LEV8 may list on centralized exchanges and non-TROPTIONS DEX pools without restriction. Exclusivity suspends if TROPTIONS fails to achieve **$100,000** LEV8-attributed volume and **500 unique wallets** within ninety (90) days after Public Sale, following thirty (30) days' notice.

---

## ARTICLE 2 — FINANCIAL TERMS (REDLINED — MOU §1.02 REJECTED)

### 2.1 Supersession of MOU Economics

The MOU provision stating that TROPTIONS's $10,000 payment "shall be reimbursed… after the first day of public token trading from available project funds, marketing budget, or initial fee revenue" is **void and of no effect**. No obligation to reimburse TROPTIONS from:

- issuer treasury or DAO reserves;
- LEV8 marketing budgets;
- Day-1, Day-0, or pre-sale investor proceeds;
- token sale proceeds; or
- any source whatsoever

shall exist.

### 2.2 Platform Integration Fee — Option A (Operative Term)

**[REDLINE — MARKET STANDARD]**

Upon (i) execution of this Agreement and (ii) satisfaction of all Conditions Precedent in Article 3, **LEV8 shall pay TROPTIONS** a non-refundable **Platform Integration Fee** of **Ten Thousand U.S. Dollars ($10,000.00)** (the "Integration Fee"), due within **five (5) business days** of execution.

| Principle | Requirement |
|-----------|-------------|
| **Direction of payment** | **LEV8 → TROPTIONS** (issuer pays platform — same as tier-1/tier-2 listing economics) |
| **Characterization** | Service revenue for launchpad integration, liquidity setup, and initial co-marketing — **not** an investment, loan, or reimbursable advance |
| **Non-refundable** | Integration Fee is **earned upon receipt**; no offset, clawback, or reimbursement from treasury, marketing budget, Day-1 proceeds, or Net Fees |
| **Scope** | Solana SPL integration, Exchange OS listing, Meteora/Jupiter routing support, and Schedule E co-marketing (TROPTIONS-delivered) |
| **LEV8 costs** | Audit, Wyoming filings, and issuer-side marketing are **LEV8's responsibility** — not funded by TROPTIONS |
| **Prohibited** | TROPTIONS paying LEV8 with guaranteed recoup; MOU §1.02 structure |

### 2.3 Optional Treasury Purchase (At-Risk Only)

**[REDLINE — IF TOKEN PURCHASE DESIRED]**

TROPTIONS may, in its **sole discretion**, purchase $LEV8 tokens on the open market after Public Sale for treasury or inventory purposes.

- **No reimbursement**, price guarantee, liquidity backstop, or return of principal.
- Any purchase is **at risk of total loss**.
- TROPTIONS shall disclose holdings in its public proof room within **twenty-four (24) hours**.
- Marketing shall **not** represent such purchase as "exchange investment" or guaranteed demand.

**[DELETE IF UNUSED — MOU-style mandatory purchase with reimbursement]**

### 2.4 Net Fees and Revenue Share

"**Net Fees**" means gross trading, launchpad, and integration fees attributable to $LEV8 activity on TROPTIONS-operated platforms, less on-chain transaction costs, chargebacks, refunds, and taxes. No deduction for overhead, salaries, or unrelated expenses.

| Period | TROPTIONS | LEV8 |
|--------|-----------|------|
| Months 1–6 | 60% | 40% |
| Months 7–12 | 50% | 50% |
| Month 13+ | 40% | 60% |

Payments monthly, within fifteen (15) business days after month-end, with on-chain export and verification rights.

### 2.5 Prohibited Structures (Market Red Flags)

Neither party shall propose or implement:

1. **Guaranteed reimbursement** of platform capital from issuer or investor funds;
2. **Risk-free "investment"** labeling for any TROPTIONS capital deployment;
3. **Circular volume** where TROPTIONS buys tokens, markets "exchange invested," and is made whole from project treasury (wash-trading appearance);
4. **Underwriter compensation** tied to guaranteed return of principal plus retained tokens without risk disclosure.

Violation is a **material breach** and triggers the Regulatory Kill Switch (Article 4).

### 2.6 Alternative Structures (Schedule B)

If the parties renegotiate economics, only the structures in **Schedule B** (Flat Integration Fee, At-Risk Purchase, Revenue-Share Only, LP Seed) are permitted templates. MOU §1.02 format is **not** a Schedule B option.

---

## ARTICLE 3 — CONDITIONS PRECEDENT

No payment, listing, or integration obligation arises until LEV8 delivers and TROPTIONS accepts:

1. Independent securities counsel opinion ($LEV8 not an investment contract under *Howey*);
2. Operating Agreement reconciliation (consumptive utility vs. securities legend);
3. Wyoming Utility Token Act Notice of Intent (W.S. § 34-29-106);
4. Tier-1 smart contract audit (zero unresolved Critical/High);
5. Mint authority verification (renounced or ≥3-of-N multisig with TROPTIONS-observable key);
6. **$25,000 USDC** legal defense escrow;
7. MSB / money-transmitter analysis;
8. Token address, treasury, and pool parameter disclosure.

---

## ARTICLE 4 — REGULATORY KILL SWITCH

TROPTIONS may immediately suspend trading, freeze liquidity, withhold fee distributions, and draw defense escrow upon SEC inquiry, Wells notice, state enforcement, or counsel-advised material regulatory risk. See `REGULATORY_KILL_SWITCH.md`. On-chain implementation: `FTHTrading/rwa-realestate` — `FTHEnforcer.triggerKillSwitch()`.

---

## ARTICLE 5 — INDEMNIFICATION

LEV8 indemnifies TROPTIONS for claims arising from (a) unregistered securities characterization of $LEV8, (b) SEO/R2O real estate compliance, and (c) breach of Article 2.5 or Article 6, subject to definitive limitation caps in full agreement.

---

## ARTICLE 6 — SMART CONTRACT OWNERSHIP AND AUDIT (NON-NEGOTIABLE)

### 6.1 TROPTIONS Infrastructure Required

All smart contracts, token programs, oracle integrations, NFT collateral registries, and on-chain enforcement logic for $LEV8 and SEO/R2O shall be **deployed, owned, upgraded, and maintained by TROPTIONS** using TROPTIONS' existing audited stack (`FTHTrading/rwa-realestate`: TruthEngine, TEVCalculator, FTHEnforcer, ComplianceRegistry, RWAToken) and Solana launch infrastructure (`launch.unykorn.org`). **LEV8 shall not deploy, control, or administer** any $LEV8-related on-chain program without TROPTIONS' prior written consent.

### 6.2 No Acceptance of Third-Party Contracts

TROPTIONS shall not integrate, list, or interact with smart contracts authored or controlled by LEV8, Judson Charles, Inc., Elev8 Management, LLC, Elev8 Holdings, LLC, or affiliates unless each contract:

(a) has a Tier-1 audit (OtterSec, Trail of Bits, CertiK, or equivalent) with zero unresolved Critical/High findings;  
(b) is reviewed and approved by TROPTIONS' technical team; and  
(c) is assigned to TROPTIONS under `LEGAL/IP_ASSIGNMENT_AGREEMENT.md`.

**White Paper pseudocode and Appendix C snippets do not constitute deliverable contracts.**

### 6.3 Division of IP

| Category | Owner |
|----------|--------|
| On-chain code, program IDs, upgrade authority | **TROPTIONS, INC.** |
| SEO/R2O legal templates, state memos, sandbox policy | **LEV8** (if gates cleared) |
| Marketing, KOL relationships | **LEV8** |
| Exchange OS, liquidity, event-commerce rails | **TROPTIONS** |

### 6.4 Audit and Deployment Costs

$LEV8 SPL deployment shall occur via **launch.unykorn.org** under TROPTIONS control. **LEV8 bears** Tier-1 audit costs for any net-new modules (cap **$15,000** unless TROPTIONS approves in writing). Such costs are **not** credits against the Platform Integration Fee paid to TROPTIONS.

### 6.5 DAO / Governance Limitation

Any future LEV8 DAO, LLC or token vote shall **not** override: (i) TROPTIONS kill switch, (ii) fee split in Article 2.4, or (iii) TROPTIONS contract ownership without TROPTIONS written consent.

### 6.6 Hard Walk Condition

If LEV8 insists that unaudited LEV8-controlled contracts be used in production, TROPTIONS may terminate and activate Solo Mode without liability.

---

## SCHEDULE B — PERMITTED ALTERNATIVE ECONOMICS (MARKET STANDARD)

| Option | Structure | Reimbursement | Typical Market |
|--------|-----------|---------------|----------------|
| **A — Flat Integration Fee** | LEV8 pays TROPTIONS $10K–$25K non-refundable listing/integration fee | None (fee earned by platform) | Tier-2 CEX / launchpad listing |
| **B — At-Risk Purchase** | TROPTIONS buys $LEV8 post-launch at market; holds as inventory | **None** | Treasury / market-making (disclosed) |
| **C — Revenue Share Only** | Zero upfront; TROPTIONS earns fee % only | N/A | Meteora/Jupiter-style neutrality |
| **D — LP Seed** | TROPTIONS seeds $LEV8/USDC pool; earns LP fees | **None**; IL risk borne by TROPTIONS | DeFi liquidity programs |
| **E — Deprecated Advance** | TROPTIONS pays LEV8 $10K; fee recoup from Net Fees | **Do not use** — resembles loan; rejected v1.2 |

**Operative (v1.2):** **Option A** — LEV8 pays TROPTIONS $10,000 non-refundable Integration Fee + Article 2.4 revenue share.

**Rejected:** MOU "on-chain investment" with Day-1 reimbursement — **demand loan / unregistered underwriting**; not accepted by tier-1 exchanges, Solana launchpads, or institutional VCs.

---

## EXECUTION VAULT CROSS-REFERENCE

| Document | Path |
|----------|------|
| Term Sheet (external) | `STRATEGIC/TERM_SHEET_FOR_JUDSON.md` |
| MOU analysis | `ANALYSIS/SOURCE_PDF_FINDINGS.md` |
| Negotiation position | `STRATEGIC/UNIFIED_NEGOTIATION_POSITION.md` |
| Market comparison (this analysis) | `LEGAL/MOU_10K_MARKET_STANDARD_ANALYSIS.md` |

---

*This draft does not constitute legal advice. Execution requires independent counsel for both parties.*
