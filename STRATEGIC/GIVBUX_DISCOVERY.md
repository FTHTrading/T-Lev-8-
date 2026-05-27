# GivBux Discovery — Due Diligence Log

**Counterparty:** GivBux, Inc. (OTC: GBUX) · CIK 0001169138  
**Control person:** Kenyatto ("Ken") Jones — see `GIVBUX/GIVBUX_FOUNDER_DILIGENCE.md`  
**TROPTIONS posture:** Internal option track — **no outbound email required**  
**Founder-direct term sheet:** `LEGAL/GIVBUX_TERM_SHEET_KEN_JONES.md` (preferred over corporate sheet when Ken is counterparty)  
**Phoenix structure:** `STRATEGIC/GIVBUX_PHOENIX_STRUCTURE.md`  
**Master ops map:** `STRATEGIC/TROPTIONS_INFRA_MONETIZATION.md`

---

## 1. Red flag summary (pre-answers)

| Check | Finding | Risk |
|-------|---------|------|
| OTC status | Pink / limited disclosure | High |
| Super App v2 site | Dead since 2024 PR | Critical |
| May 2024 roadmap | Undelivered | Critical |
| Cash (Sept 2024 10-Q) | ~$64K | Critical |
| Engineering | No public API / GitHub | Scope creep — you become their dev shop |
| Ask | Full AI + XRPL + Solana + stablecoins | Massive — must be white-label configure, not greenfield |

**Hard rule:** No GitHub, `troptionslive`, or production API keys until **NDA + signed term sheet + Phase 0 cleared**.

---

## 2. Discovery email (send before any scoping)

**To:** [GivBux contact — record name/title below]  
**CC:** IR@GivBux.com (if not primary)  
**Subject:** TROPTIONS Infrastructure Partnership — Required Discovery (No Engineering Until Received)

```
Dear [Name],

Thank you for the conversation regarding a white-label deployment of TROPTIONS infrastructure (wallet, stablecoin rails, exchange, charity layer, and AI services) for the GivBux platform.

Before TROPTIONS allocates engineering or legal resources, we require written responses to the items below. We will not begin specification work, access reviews, or integration planning until this questionnaire is complete and reviewed by our counsel.

DISCOVERY QUESTIONNAIRE

1. Corporate & contacts
   a. Legal name and state of incorporation
   b. Name, title, and authority of signatory for a technology agreement
   c. Name of outside securities counsel

2. Users & product
   a. Current monthly active users (MAU) — iOS and Android, last 90 days
   b. Engineering headcount (FTE and contractors) and primary mobile stack
   c. Current app version in production stores and last release date

3. Budget & timeline
   a. Budget range allocated for external technology rebuild (USD)
   b. Target public relaunch date for "Super App" functionality
   c. Proof of funds or escrow mechanism for upfront integration fees

4. Regulatory
   a. MSB / FinCEN registration status for real-time crypto conversion (if any)
   b. Summary of open SEC comment letters or investigations (Dec 2024 and later)
   c. Status of Washington DFI 2019 consent order — ongoing obligations?

5. Merchants & data
   a. Identity of third-party merchant/cashback aggregator (under NDA if required)
   b. Assignability of merchant agreements to a TROPTIONS white-label entity
   c. User database size and last GDPR/CCPA privacy audit date

6. Affiliate / compensation model
   a. Confirm whether recruitment commissions ($149.95 signup / $29.95 mo) remain active
   b. Willingness to retire MLM-style affiliate structure in any relaunch

7. AI & technical scope
   a. Which "AI infrastructure" is required? (LLM support, vision, voice, recommendations, fraud)
   b. Chains and tokens required day one (Solana, XRPL, USDC, RLUSD, others)
   c. Custody model: GivBux custodial vs non-custodial vs hybrid

8. Commercial
   a. Exclusivity expectations (global vs non-exclusive white-label)
   b. Acceptance of TROPTIONS ownership of smart contracts and middleware (license-only to GivBux)
   c. Rejection of GBUX equity as payment — cash fees only

Please attach the most recent 10-K or 10-Q and a capitalization table showing outstanding converts and defaulted notes.

TROPTIONS will respond with a fixed-fee phase proposal only after review.

Regards,
[Name]
FTH Trading / TROPTIONS, Inc.
```

---

## 3. Answer log (fill when received)

| # | Question | Their answer | Risk note | Verified? |
|---|----------|--------------|-----------|-----------|
| 1a | Legal entity | | | ☐ |
| 1b | Signatory authority | | | ☐ |
| 2a | MAU | | | ☐ |
| 2b | Eng headcount | | | ☐ |
| 3a | Budget range | | **Walk if <$75K Phase 0** | ☐ |
| 3c | Proof of funds | | | ☐ |
| 4a | MSB / FinCEN | | | ☐ |
| 4b | SEC investigations | | | ☐ |
| 5a | Aggregator identity | | **Walk if refused** | ☐ |
| 6a | MLM still active? | | **Walk if yes + no retire** | ☐ |
| 8b | Accept TROPTIONS owns IP | | **Walk if no** | ☐ |
| 8c | Cash only (no GBUX stock) | | **Walk if equity offered** | ☐ |

**Contact from GivBux:** _________________________ **Date contacted:** __________

**Who has decision rights?** _________________________

**Budget mentioned on first call?** ☐ Yes ☐ No — Amount: __________

**Aware of T-VEX-8 / WC26 stack?** ☐ Yes ☐ No

**Exclusivity requested?** ☐ Yes ☐ No — **If yes, fee multiplier: 3×**

---

## 4. Competitive reality (internal)

| Feature | GivBux claims | TROPTIONS |
|---------|---------------|-----------|
| Mobile wallet | iOS/Android | Exchange OS + launch rails |
| Cashback 100+ | Retailers | Sponsor tiers + QR drops |
| Charity auto-% | 501(c)(3) | Impact + Apostle proof |
| Crypto exchange | v2 "coming" (2024) | **Live** — exchange-os |
| AI | v2 promise | DONK / x402 / Finn paths |
| Stablecoins | None stated | USDC/USDT + USDF/XRPL |

**Positioning:** Licensing sale — you are ahead technically. They need a transplant, not a co-build.

---

## 5. Internal decision matrix (after answers)

| Outcome | Criteria |
|---------|----------|
| **Proceed to term sheet** | Phase 0 fundable; signatory clear; MLM retired or firewalled; aggregator named; cash only |
| **Negotiate harder** | Budget $75K–$150K total — scope to Phase 0–1 only |
| **Walk** | Equity offer; contract ownership demand; no wire; MLM retained; SEC filing "help" requested |

---

## 6. Pipeline priority (unchanged)

| Track | Priority |
|-------|----------|
| VEX / Judson term sheet | **Continue** — known counterparty |
| Sepolia gate deploy | **Continue** — strengthens all negotiations |
| GivBux build | **Blocked** until discovery + Phase 0 |
| Aurora/impact Pages | Lower than GivBux **only if GivBux pays** |

---

## 7. Next internal actions

1. Send discovery email (Section 2).  
2. Request 2025 10-K / latest 10-Q.  
3. UCC lien search (Nevada).  
4. If answers acceptable → execute `LEGAL/GIVBUX_TERM_SHEET.md`.  
5. Never attach Aurora/VEX comparison tables to GivBux correspondence.
