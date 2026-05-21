# GivBux Phoenix Structure — Clean Entity (Recommended)

**Problem:** Contracting with **GivBux Inc. (OTC: GBUX)** ties TROPTIONS to SEC-scrutinized shell, $7M deficit, defaults, and 2019 founder order.  
**Solution:** License technology to a **new, independently capitalized entity** with no assumption of legacy liabilities.

---

## 1. Target structure

```
Kenyatto ("Ken") Jones + qualified investors (if any)
              │
              ▼
    NEWCO: e.g. "GivBux Technologies LLC" (Wyoming/NV — counsel picks)
              │
              ├── Pays TROPTIONS Integration Fees (escrow)
              ├── Holds white-label license (non-exclusive default)
              └── Operates consumer app + merchant relationships
              
    LEGACY: GivBux Inc. (GBUX) — no TROPTIONS contract
              │
              └── Wind down, sold for parts, or dormant (no tech license)
```

**Public statement (if needed):**

> TROPTIONS does not partner with GivBux Inc. (OTC: GBUX). We license infrastructure to [NEWCO Legal Name], an independent technology licensee.

---

## 2. NEWCO requirements (non-negotiable)

| Requirement | Why |
|-------------|-----|
| **Independent capitalization** | Wire from NEWCO account; not pass-through from insolvent parent |
| **No automatic liability assumption** | NEWCO does not assume GivBux Inc. debts, MLM obligations, or SEC liabilities |
| **Separate bank / escrow** | Phase 0–1 fees in third-party escrow, release on milestones |
| **Ken role** | Officer of NEWCO ok; **personal guarantee** still required if Ken is control person |
| **MLM prohibition** | NEWCO charter + license: no recruitment commissions |
| **IP** | All code owned by TROPTIONS; NEWCO gets revocable license only |

---

## 3. Successor liability traps (reject if present)

| Red flag | Action |
|----------|--------|
| NEWCO is sole asset of GivBux Inc. with no new money | Walk — sham successor |
| Same bank account as GivBux Inc. | Walk — commingling |
| Assignment of all GivBux Inc. contracts without creditor consent | Counsel review — may trigger defaults |
| Press release implying "GivBux Inc. relaunch" without NEWCO distinction | Fix messaging or walk |

---

## 4. Comparison: Phoenix vs legacy shell

| Factor | Phoenix (NEWCO) | GivBux Inc. direct |
|--------|-----------------|---------------------|
| SEC taint on counterparty | Lower (new entity) | **High** |
| Fraudulent conveyance risk | Lower if NEWCO funded | **High** |
| Reputational link | Severable in public | Sticky |
| Contract complexity | Medium (formation) | Lower but riskier |
| TROPTIONS recommendation | **Default** | Only + guarantee + indemnity |

---

## 5. Implementation steps (internal)

1. Counsel drafts NEWCO formation + operating agreement (MLM prohibition).  
2. TROPTIONS licenses to NEWCO only (`LEGAL/GIVBUX_TERM_SHEET_KEN_JONES.md`).  
3. Escrow agent holds Phase 0 ($50K Legal Hold).  
4. No production API keys until escrow + NDA + structure sign-off.  
5. Legacy app sunset; new shell uses TROPTIONS Wallet SDK.  

---

## 6. If Ken refuses Phoenix

Fall back to **Option B** in `LEGAL/GIVBUX_TERM_SHEET_KEN_JONES.md`:

- Contract with GivBux Inc. **plus** Ken Jones **personal guarantee**  
- Broad indemnity (2019 order, MLM, pre-2026 ops)  
- Vendor-only / no successor liability acknowledgment  
- Escrow for all phase payments  

**Still no equity. Still no free work.**

---

## 7. TROPTIONS money flow (Phoenix path)

| Stream | Recipient |
|--------|-----------|
| Phase 0–3 fixed fees | TROPTIONS treasury |
| Phase 4 ops retainer | TROPTIONS |
| % gross crypto volume | TROPTIONS (5% Ken-Jones sheet) |
| Merchant / exchange spread | Per rev-share table |

Legacy GBUX shareholders **do not** receive TROPTIONS equity or revenue share unless separately contracted (not recommended).
