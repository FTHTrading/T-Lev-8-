# T-VEX-8 Deal Room & Execution Protocol

**Status:** Pre-Execution — Governor active (default `SOLO_LAUNCH`)  
**Governing Law:** Wyoming  
**Live Site:** https://fthtrading.github.io/T-VEX-8-/  
**Ecosystem map:** [ECOSYSTEM.md](./ECOSYSTEM.md)  
**AI agents:** [AGENTS.md](./AGENTS.md) → [PROTOCOL_GOVERNANCE_PROMPT.md](./AI_SYSTEM/PROTOCOL_GOVERNANCE_PROMPT.md)

---

## Quick Start

| Who | Action |
|-----|--------|
| **Bryan** | Send [JUDSON_EMAIL_FINAL.md](./STRATEGIC/JUDSON_EMAIL_FINAL.md) + term sheet PDF |
| **AI / analyst** | Load `AI_SYSTEM/PROTOCOL_GOVERNANCE_PROMPT.md` |
| **Engineering** | [72_HOUR_PLAYBOOK](./OPERATIONS/72_HOUR_PLAYBOOK.md) or [QUICKSTART](./LAUNCH_NOW/QUICKSTART.md) |

```bash
git add . && git commit -m "chore: update gates" && git push origin main
```

Enable **GitHub Pages:** Settings → Pages → Source: **GitHub Actions**

---

## Repository Map

| Directory | Purpose |
|-----------|---------|
| [ECOSYSTEM.md](./ECOSYSTEM.md) | **Master index** — full project map |
| [AI_SYSTEM/](./AI_SYSTEM/) | Protocol Governor, Legal Architect, reminders, kill switch monitor |
| [LEGAL/](./LEGAL/) | Master Agreement, kill switch, listing policy, UNYKORN framework |
| [STRATEGIC/](./STRATEGIC/) | Term sheet, Judson email, negotiation (internal: Aurora brief) |
| [COMPLIANCE/](./COMPLIANCE/) | Gates, Howey worksheet, state matrix, Judson checklist PDF |
| [ANALYSIS/](./ANALYSIS/) | Valuation, source PDF findings (internal) |
| [PIPELINE/](./PIPELINE/) | Active partner tracker (VEX) |
| [OPERATIONS/](./OPERATIONS/) | 72-hour execution + [Next Steps Protocol v1.0](./OPERATIONS/NEXT_STEPS_PROTOCOL_v1.0.md) |
| [LAUNCH_NOW/](./LAUNCH_NOW/) | Aurora 15-minute mint guide |
| [data/](./data/) | `governance-state.json` for deal room UI |
| [INTEGRATION/](./INTEGRATION/) | \$VEX full-stack map (launcher, exchange, sports) |
| [SITE_UPDATES/](./SITE_UPDATES/) | Canonical markdown snapshots for deal room |
| [IPFS/](./IPFS/) | Execution manifest |

**Smart contract implementation:** [FTHTrading/rwa-realestate](https://github.com/FTHTrading/rwa-realestate) — `TVEXGateManager.sol`, `FTHEnforcer` kill switch, compliance registry extensions.

---

## Protocol Governor (algorithmic)

```
gates_cleared == 7  → PARTNER_EXECUTE
gates_cleared >= 5  → PARTNER_NEGOTIATE
gates_cleared >= 3  → HOLD_PIPELINE
else                → SOLO_LAUNCH (default)
```

**VEX today:** 0/7 gates · risk 8.5 · mode **SOLO_LAUNCH** after timeout/walk-away

---

## Conditions Precedent

**0/8 cleared** on deal room UI (7 gates + token disclosure). See [CONDITIONS_PRECEDENT.md](./COMPLIANCE/CONDITIONS_PRECEDENT.md).

---

## Deploy

```powershell
cd C:\Users\Kevan\Documents\UNYKORN_Ecosystem\T-VEX-8-
.\deploy.ps1
```

See [DEPLOY.md](./DEPLOY.md).

---

*TROPTIONS, INC. — Not legal advice.*
