# Analysis of Source PDFs Received from Judson/Vlad

**Date:** 2026-05-20  
**Analyst:** T-VEX-8 Legal & Systems Review  
**Classification:** Internal — attorney work product; **do not send to Judson**

**Files reviewed:**

1. `VEX White Paper Version 1.0 draft 3.7 - 2026.04.05 (2).pdf`
2. `Operating Agreement (Wyoming) - VEX Technologies LLC (2).pdf`
3. `Troptions1.pdf` (MOU, May 16, 2026)

Full extract: `../VEX_SOURCE_DOCS_EXTRACT/` (UNYKORN_Ecosystem parent folder) or counsel data room.

---

## 1. VEX White Paper (v3.7)

**Status:** Conceptual / pre-launch

**Legal claim:** Token is "not a security" under Howey.

**Fatal contradiction:** The Operating Agreement for **VEX Technologies, LLC** treats membership interests as **unregistered securities under the 1933 Act**. A token issued by that entity cannot credibly be marketed as a "non-security" while the issuer's interests are documented as restricted securities.

**Tokenomics red flags:**

| Issue | Detail |
|-------|--------|
| Insider concentration | **55%** team and advisors |
| Float | **10%** initial liquidity at Meteora launch |
| Utility | **Optional** \$VEX for SEO/R2O (weak consumptive-use narrative) |
| Treasury | DAO treasury language conflicts with "no pooled treasury" themes elsewhere |
| Detail gaps | Section 9.2 "TBD"; 10.2 performance rewards "TBD" |

**On-chain reality:** No mint address, no deployed contracts, no audit in packet.

---

## 2. VEX Technologies LLC Operating Agreement

**Status:** Docusign executed; filed **March 18, 2026**  
**Jurisdiction:** Wyoming  
**Capitalization:** **$1,000** total (EVEX Holdings LLC **$700** / 70%; Vlad Chiriac **$300** / 30%)

**Smoking gun (cover page):**

> THE INTERESTS ACQUIRED PURSUANT TO THIS AGREEMENT HAVE NOT BEEN REGISTERED UNDER THE SECURITIES ACT OF 1933...

This documents that **membership interests are securities**. The LLC deploys the utility token and owns protocol IP (Art. 2.5). Issuer-level securities characterization bleeds into token analysis.

**Structure notes:**

- **Manager:** EVEX Management, LLC (California)
- **DAO:** VEX DAO, LLC — governance/treasury; LLC explicitly does **not** perform DAO functions
- **Tax Matters Partner:** Judson Leibee
- **Wyoming Utility Token Act:** Notice of Intent referenced — **no file stamp in packet**

**Authority / entity confusion:**

| Document | Party named |
|----------|-------------|
| MOU | "VEX PROJECT," Judson Charles, Inc. (CA), Vlad individual |
| OA | VEX Technologies, LLC (WY) |
| White Paper | Judson C. **Leibe** vs OA **Leibee** |

Risk: MOU signatory may lack authority to bind LLC; ultra vires / voidable commitments.

---

## 3. TROPTIONS MOU (May 16, 2026)

**Status:** **Non-binding** per Section 5.01 (except Article 3 confidentiality, **10 years**)

**Legal effect on economics:** None until definitive Transaction Documents.

**Counterparty issues:**

- Vlad Chiriac signed as "Developer / Authorized Representative" of "VEX PROJECT" (not a legal entity)
- No corporate resolutions attached
- TROPTIONS signature line **blank** in provided PDF — confirm whether fully executed

**Economic structure (unacceptable in binding form):**

- $10K on-chain purchase; reimburse **after first day of public trading** from **project funds, marketing budget, or initial fee revenue**
- Reads as **treasury clawback**, not fee-only recoupment

**Other MOU terms:**

- 50% fee share — undefined (gross/net, attribution)
- Exclusivity duration **blank** ("e.g., 12 months")
- VEX must promote Troptions on **every CEX** + "good faith" volume
- **California** governing law

---

## Conclusion

VEX is a **pre-product, pre-compliant, pre-revenue** concept with **$1,000** capitalization and a **fatal internal legal contradiction** between the OA and white paper. The MOU creates **no enforceable economic value** and substantial risk if treated as a floor for binding terms.

**Recommended posture:**

- External: Term sheet + Master path + seven gates (**no Aurora** in writing)
- Internal: Aurora as Plan B if gates stall or terms unreasonable
- **Do not** wire, list, or integrate until all conditions precedent are verified

**Related:** `../STRATEGIC/UNIFIED_NEGOTIATION_POSITION.md`, `../../VEX_FULL_LEGAL_SYSTEM_DEEP_DIVE.md`

---

*Prepared for TROPTIONS / FTH Trading internal use.*
