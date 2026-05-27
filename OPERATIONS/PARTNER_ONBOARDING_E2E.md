# Partner Launch on TROPTIONS / T-VEX-8 — End-to-End Operations

**Owner:** FTH Trading / TROPTIONS  
**Deal room:** https://fthtrading.github.io/T-VEX-8-/  
**Canonical repos:** `C:\Users\Kevan\troptions` · `C:\Users\Kevan\solana-launcher` · `C:\Users\Kevan\GitHub_Audit\T-VEX-8-`  
**Updated:** 2026-05-27

---

## 0. Who is launching on whom (read first)

| Party | Role |
|-------|------|
| **TROPTIONS / FTH (you)** | Platform operator — T-VEX-8 gates, Exchange OS, launcher, sports rails |
| **Partner (e.g. VEX DAO / Technologies)** | Asks to **use your system** for token, compliance, distribution, optional DEX/CEX |
| **T-VEX-8** | Negotiation + proof UI — **not** the blockchain; it reads `data/governance-state.json` |
| **Aurora** | Your **solo reserve** token if partner fails gates — not the partner product |

**Correction:** You do not "onboard TROPTIONS onto T-VEX-8." You **onboard the partner onto TROPTIONS infrastructure**, tracked in T-VEX-8.

---

## 1. What is actually built (honest)

### Production-ready today

| Capability | Surface | Evidence |
|------------|---------|----------|
| Deal room + 8 gates | [T-VEX-8](https://fthtrading.github.io/T-VEX-8-/) | `governance-state.json` |
| Token launcher (SPL) | https://launch.unykorn.org | `solana-launcher` |
| Exchange OS UI | https://troptionslive.unykorn.org/exchange-os | `troptions` build passes |
| Partner onboarding UI | `/exchange-os/partner-onboarding` | 12-stage pattern |
| Sports / event commerce | `/sports` | WC2026 Atlanta network |
| GoatX mint (mainnet) | Solscan | Mint live; **LP not seeded** |
| x402 intelligence | Exchange OS | Live per status matrix |
| Legal drafts | `T-VEX-8-/LEGAL/` | Master Agreement, Kill Switch, Listing Policy |
| CEX contracts (VEX) | Desktop pack `03-Exchange-Listings/` | Poloniex + BitMart |

### Not ready for "100% unattended" launch

| Gap | Impact | Fix |
|-----|--------|-----|
| **0/8 gates cleared** | No wire, no mainnet flags | Close gates per Section 3 |
| **Exchange OS mainnet flags off** | XRPL/Solana execution gated | Cloudflare secrets after checklist |
| **Launch Registry / admin** | Missing | Manual tracker + build `/admin/exchange` |
| **In-app Solana LP** | Stubbed | Use CLI `seed-raydium-lp.mjs` |
| **79 failing tests** | Risk on API routes | Triage `troptions` CI |
| **Trust wallet ~0.016 SOL** | Cannot seed Raydium LP | Fund ≥6 SOL |
| **XRPL issuer HALT** | Low reserve | Fund issuer ~11 XRP target |
| **Execution vault IPFS** | SHA/CID pending | Pin after gate GO |
| **VEX Meteora LP** | WP says Meteora; CLI is Raydium | Script or manual Meteora run |

**Operational certainty = gates + checklist + funded wallets + CLI LP + counsel sign-off — not "flip a switch."**

---

## 2. The only three launch rails

Every partner uses one or more:

```
Rail A — CEX only        Poloniex / BitMart (VEX DAO signs; Troptions advises)
Rail B — Troptions DEX   Exchange OS + optional on-chain LP (Raydium/Meteora)
Rail C — Aurora reserve  You launch AURORA solo if partner fails (internal only)
```

VEX today: **A + B planned**, gated by **T-VEX-8 8/8** and capital.

---

## 3. Eight gates (T-VEX-8) — operational definition of "done"

| ID | Gate | Done when | Owner | VEX status |
|----|------|-----------|-------|-------------|
| G1 | Independent securities counsel opinion | Written opinion: not Howey security (counsel ≠ Judson) | Partner + Troptions counsel | Pending |
| G2 | OA reconciliation | 1933 legend removed/amended; utility intent clear | Partner | Pending |
| G3 | Wyoming Utility Token Act | Notice filed; SOS stamp to Troptions | Partner | Pending |
| G4 | Tier-1 smart contract audit | Final report, zero open Critical/High | Partner | Pending |
| G5 | Mint authority | Renounced OR ≥3-of-N multisig (TROPTIONS observer) | Joint | **Partial** — mint `3gga7FiVFf7ejacX7uh1zqGKL11PxmP6PHyNRmCi6Avv` exists; authority not verified in gate file |
| G6 | Legal defense escrow | $25k USDC in Troptions-designated escrow | Partner | Pending |
| G7 | MSB / MT analysis | FinCEN memo for partner flows | Troptions compliance | Pending |
| G8 | Token disclosure | Mint, program IDs, treasury multisig, pool params, CEX plan | Partner | **Partial** — mint + CEX PDFs in pack; Meteora params TBD |

Update `GitHub_Audit/T-VEX-8-/data/governance-state.json` when each closes → site governor recalculates mode.

---

## 4. End-to-end sequence (100% operational)

### Phase 1 — Intake (Day 0–3)

| Step | Action | System | Output |
|------|--------|--------|--------|
| 1.1 | Open partner row | `PIPELINE/PARTNER_PIPELINE.md` | CRM row |
| 1.2 | Collect packet | Email / vault | OA, WP, entity docs, signer IDs |
| 1.3 | KYB/KYC | Your AML policy | Pass/fail |
| 1.4 | Howey + state matrix | T-VEX-8 repo worksheets | Signed internal memo |
| 1.5 | Master Agreement + Kill Switch | `LEGAL/` | Executed counters |
| 1.6 | Assign rails | A/B/C | Written scope |

**VEX:** Packet partially in `Desktop/VEX-Troptions-Launch-Pack/`.

### Phase 2 — Technical validation (Day 3–10)

| Step | Action | Command / path |
|------|--------|----------------|
| 2.1 | Verify SPL mint | Helius/Solscan — supply, authorities, metadata |
| 2.2 | Run audit or accept sandbox disclosure | G4 |
| 2.3 | Register in partner onboarding | `troptionslive.../exchange-os/partner-onboarding` |
| 2.4 | Proof packet | Mint tx, authority report, legal PDFs |
| 2.5 | Add row | `04-Troptions-DEX-Launch/TOKEN-LAUNCH-REGISTER-TEMPLATE.csv` |

### Phase 3 — Liquidity (Day 7–21)

| Token | CEX liquidity | DEX LP |
|-------|---------------|--------|
| VEX | BitMart $30k lock + Poloniex fees | Meteora (per WP) — **assign owner** |
| GoatX (proof) | N/A | `node scripts/seed-raydium-lp.mjs --apply` after funding wallet |

```powershell
cd C:\Users\Kevan\solana-launcher
# Dry-run
node scripts/seed-raydium-lp.mjs --mint=3gga7FiVFf7ejacX7uh1zqGKL11PxmP6PHyNRmCi6Avv --sol=5 --tokens=100000000
# Live — only after SOL funded + gate GO
node scripts/seed-raydium-lp.mjs --apply --yes --mint=MINT --sol=5 --tokens=AMOUNT
```

Lock LP: UNCX / Streamflow — record tx in register.

### Phase 4 — Platform integration (Day 10–25)

| Step | Action | Blocker |
|------|--------|---------|
| 4.1 | List token on Exchange OS (truth labels) | Mainnet flag scoped |
| 4.2 | Solana tab / Jupiter route | Pool must exist |
| 4.3 | Optional: sports merchant pilot | Separate MOU |
| 4.4 | x402 / proof logging | Apostle testnet shim |
| 4.5 | Push governance JSON | Gates → site updates |

**Enable mainnet only via Cloudflare secrets** — see `troptions/docs/TROPTIONS_EXCHANGE_OS_MAINNET_READINESS_CHECKLIST.md`.

### Phase 5 — CEX track (parallel — VEX)

| Deadline | Action |
|----------|--------|
| Poloniex | 10k USDT + 10k VEX marketing (effective 16 May 2026) |
| BitMart | 30k USDT within 3 days of agreement; liquidity 1 biz day before **8 Jun 2026** |

TROPTIONS does not sign these — **VEX DAO LLC** does. Your risk is **reputation + infra** if you promote before gates close.

### Phase 6 — Post-launch (ongoing)

| Monitor | Tool |
|---------|------|
| Kill switch conditions | `LEGAL/REGULATORY_KILL_SWITCH.md` |
| BitMart price rules | Addendum — 50%/75% drop triggers |
| LP / authority | Helius alerts |
| Governance | Monthly partner report (Poloniex covenant mirrors this) |
| Documents | Git commit → Pages refresh |

---

## 5. Governor modes (how T-VEX-8 decides)

From live `index.html` logic:

| gates_cleared | Mode | Meaning |
|---------------|------|---------|
| 0–2 | **SOLO_LAUNCH** | Negotiate hard; Aurora reserve available |
| 3–4 | **HOLD_PIPELINE** | Conditional work only |
| 5–7 | **PARTNER_NEGOTIATE** | Term sheet + gate closure |
| 8 + execute | **PARTNER_EXECUTE** | Wire + mainnet scope after escrow |

**Current VEX:** 0/8 → **SOLO_LAUNCH** on site. Correct.

---

## 6. RACI (who does what)

| Task | TROPTIONS | Partner (VEX) | Counsel |
|------|-----------|----------------|---------|
| Gates G1,G2,G3,G4,G6 | Verify | Deliver | G1 independent |
| Mint / LP | CLI support | Fund + sign | — |
| Exchange OS listing | Operate platform | Provide disclosures | Approve copy |
| CEX listing | Advise optional | Sign + pay | — |
| Kill switch | Hold keys per agreement | Accept | — |
| Sports integration | Operate | Co-market | — |

---

## 7. Go / no-go (single decision)

**GO for limited mainnet (Exchange OS read + wallet + one pool):**

- [ ] ≥6 gates closed (minimum: G1, G2, G6, G7, G8, G5)
- [ ] G4 audit or signed sandbox waiver with liability cap
- [ ] LP exists OR explicit "CEX-only" disclosure
- [ ] Trust wallet / treasury funded
- [ ] Launch committee sign-off logged
- [ ] `governance-state.json` pushed

**NO-GO:**

- Wire before G6 escrow
- Mainnet flags before checklist
- BitMart liquidity deposit without MM plan
- Marketing "live on Troptions" with 0/8 gates

---

## 8. File map (where everything lives)

| Need | Path |
|------|------|
| Desktop legal + gameplan | `Desktop/VEX-Troptions-Launch-Pack/` |
| Deal room source | `GitHub_Audit/T-VEX-8-/` |
| Governor state | `T-VEX-8-/data/governance-state.json` |
| Partner pipeline | `T-VEX-8-/PIPELINE/PARTNER_PIPELINE.md` |
| DEX readiness audit | `05-Gameplan-and-Checklists/TROPTIONS-DEX-READINESS-AUDIT.md` |
| Master timeline | `05-Gameplan-and-Checklists/MASTER-GAMEPLAN.md` |
| Exchange OS checklist | `troptions/docs/TROPTIONS_EXCHANGE_OS_MAINNET_READINESS_CHECKLIST.md` |

---

## 9. Next 72 hours (Kevan)

1. Fund trust wallet **≥6 SOL** → seed **GoatX LP** (proves Rail B).  
2. Update `governance-state.json`: G8 partial, VEX mint address, BitMart date.  
3. Send Judson **term sheet** only after `STRATEGIC/TERM_SHEET_PRE_SEND_VALIDATION.md`.  
4. Fix G5 in pipeline doc ("no mint" → mint exists, verify authorities).  
5. BitMart **30k USDT** if proceeding CEX — only after G6 path clear.  
6. Triage **79** test failures in `troptions` before calling platform "certified."

---

*This document is operational guidance, not legal advice.*
