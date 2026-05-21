# TERM SHEET — GivBux White-Label Infrastructure (Distressed Vendor Model)

**Date:** [PENDING]  
**Status:** Draft for negotiation — **not legal advice**; counsel review required  
**Template basis:** `LEGAL/MASTER_AGREEMENT.md` v1.3 (Article 6 ownership, no reimbursement)  
**Parties:**
- **TROPTIONS, INC.** (Wyoming) — "TROPTIONS"
- **GIVBUX, INC.** (Nevada or as disclosed) — "GivBux"

---

## 1. Transaction summary

TROPTIONS will provide a **non-exclusive, revocable white-label license** to GivBux-branded instances of existing TROPTIONS infrastructure (wallet SDK, stablecoin rails, exchange API, charity split contracts, AI APIs, proof layer). TROPTIONS **builds, owns, and operates** all smart contracts, middleware, and AI models. GivBux retains customer relationships and SEC reporting obligations for its issuer entity.

**This is not a partnership, joint venture, or merger.** TROPTIONS is a technology vendor. GivBux is a distressed licensee with bad credit — price accordingly.

---

## 2. Fees (cash only — no GBUX equity)

| Phase | Deliverable | Fee (USD) | Payment terms |
|-------|-------------|-----------|---------------|
| **Phase 0 — Survival** | Due diligence, architecture v0.1, legal scrub plan, project charter | **$75,000** | **100% wire before any TROPTIONS engineering** |
| **Phase 1 — Foundation** | Wallet SDK (Solana); USDC/USDT + XRPL stablecoin rails; charity-split contracts (testnet) | **$150,000** | 50% at Phase 1 kickoff; 50% on testnet acceptance |
| **Phase 2 — Exchange** | White-label Exchange OS (`exchange.givbux.com` or subdomain); merchant API live | **$100,000** | Net-15 from acceptance |
| **Phase 3 — AI** | DONK/x402 APIs: support, merchant copy, fraud screening (usage-metered) | **$100,000** | 50% kickoff; 50% UAT sign-off |
| **Phase 4 — Operations** | Hosting, compliance monitoring, upgrades | **$25,000/mo** minimum 12 months | Monthly advance |
| **Transaction fee share** | Gross crypto transaction fees on GivBux-branded volume | **3%** to TROPTIONS | Monthly settlement, audited report |

**Minimum cash through Phase 3:** **$425,000** + Phase 4 + rev share.

**Walk if Phase 0 does not clear within 10 business days of execution.**

---

## 3. Revenue share (transaction layer)

| Period (cumulative GivBux-branded volume) | TROPTIONS | GivBux |
|------------------------------------------|-----------|--------|
| $0 – $5M | **60%** | 40% |
| $5M – $25M | **50%** | 50% |
| $25M+ | **40%** | 60% |

"Net Fees" = gross protocol fees attributable to GivBux white-label instance, less on-chain gas, chargebacks, refunds, and taxes. No deduction for GivBux overhead.

---

## 4. IP & ownership (Article 6 — non-negotiable)

1. All **smart contracts**, **middleware**, **AI models**, and **deployment configs** created or configured by TROPTIONS are owned by TROPTIONS (or assigned per `LEGAL/IP_ASSIGNMENT_AGREEMENT.md` pattern).  
2. GivBux receives a **non-exclusive, non-transferable, revocable** license for the term of payment.  
3. **No work-for-hire assignment** to GivBux.  
4. **No GBUX shares, warrants, or converts** as consideration.  
5. Pre-existing GivBux marks remain GivBux; new code remains TROPTIONS.

---

## 5. Exclusivity

| Tier | Terms |
|------|-------|
| **Default** | Non-exclusive — TROPTIONS may license same stack to others |
| **Exclusive (optional)** | Additional **$300,000** upfront + higher rev share floor — 24-month max |

---

## 6. Milestone gates (no pay, no ship)

| Gate | Criteria |
|------|----------|
| G0 | Phase 0 wire + discovery complete + NDA |
| G1 | Charity contracts on testnet; wallet SDK UAT |
| G2 | Exchange white-label live; 3 pilot merchants |
| G3 | AI endpoints UAT; fraud rules signed off |
| G4 | Production cutover; kill-switch tested |

Late payment **>15 days** → TROPTIONS may suspend API keys and invoke kill switch.

---

## 7. Compliance firewall

1. GivBux **warrants** disclosure of SEC comment letters, defaults, and 2019 WA order status.  
2. TROPTIONS **will not** integrate MLM/recruitment commission engines.  
3. TROPTIONS **will not** prepare or file GivBux SEC reports.  
4. GivBux retains all legacy consumer and regulatory liability.  
5. MSB/crypto conversion compliance remains **GivBux's** obligation; TROPTIONS provides tooling only.  
6. User data port requires **GDPR/CCPA scrub** — TROPTIONS not liable for legacy data practices.

---

## 8. Kill switch & termination

TROPTIONS may **immediately suspend** white-label access if:

- Payment default >15 days  
- Material breach of MLM prohibition  
- Undisclosed SEC investigation becomes known  
- GivBux insolvency, bankruptcy, or assignment for benefit of creditors  
- GivBux attempts to reverse-engineer or seize TROPTIONS infrastructure  

Upon termination: license ends; GivBux has **no** source code escrow rights unless separately purchased at fair market value.

---

## 9. Walk triggers (same discipline as LEV8)

| Trigger | Action |
|---------|--------|
| Cannot wire Phase 0 | **Walk** — no work |
| Demands contract ownership | **Walk** |
| Offers GBUX equity for fees | **Walk** |
| Asks TROPTIONS to fund OTC audit / SEC fixes | **Walk** |
| Insists on MLM layer | **Walk** — FTC exposure |
| Refuses aggregator disclosure under NDA | **Walk** |
| Exclusive demand without exclusive fee | **Counter or walk** |

---

## 10. Access & confidentiality

- No production repo, Exchange OS admin, or Apostle keys until Phase 0 + NDA + signatory verification.  
- GivBux receives **sandbox** credentials only through Phase 1.

---

## 11. Honest pitch (internal talking points)

> GivBux has brand decay and a technology deficit. TROPTIONS has live infrastructure. We will lease a white-label stack for **$425K+ cash**, **3% transaction share**, and **monthly ops**. We own the code. You own customer relationships and SEC obligations. If Phase 0 cannot wire, we cannot start. This is a technology transplant, not a partnership.

---

## 12. Document map

| Doc | Purpose |
|-----|---------|
| `COMPLIANCE/GIVBUX_OTC_RISK.md` | Risk memo |
| `STRATEGIC/GIVBUX_DISCOVERY.md` | Q&A log |
| `INTEGRATION/GIVBUX_ARCHITECTURE_v0.1.md` | Technical mapping |
| `LEGAL/MASTER_AGREEMENT.md` | Long-form precedent |

**Execution path:** Term sheet → counsel → Master Platform Agreement (GivBux schedule) → SOW per phase.
