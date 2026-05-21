# 72-Hour Execution Checklist

## Priority 1 — Sepolia gate manager

```powershell
cd "C:\Users\Kevan\Documents\UNYKORN_Ecosystem\rwa-realestate"
# .env: SEPOLIA_RPC_URL, PRIVATE_KEY, optional COUNSEL_MULTISIG
npx hardhat run scripts/tlev8/deploy_gate_manager.js --network sepolia
```

Pin address in `T-Lev-8-/data/governance-state.json` → `on_chain.gate_manager_sepolia`.

## Priority 2 — Term sheet v1.2 PDF

1. Open `STRATEGIC/TERM_SHEET_v1.2.html` in browser → Print → Save as PDF  
2. Or: `pandoc STRATEGIC/TERM_SHEET_FOR_JUDSON.md -o STRATEGIC/TROPTIONS_LEV8_Term_Sheet_v1.2.pdf`

**Verify before send:**

- [ ] LEV8 **pays** TROPTIONS $10K Integration Fee  
- [ ] No MOU reimbursement / Day-1 treasury language  
- [ ] No "$20K Net Fee recoup" clause  
- [ ] Article 6 / contract ownership referenced  

## Priority 3 — Send Judson

- Body: `STRATEGIC/JUDSON_EMAIL_FINAL.md`  
- Attach: PDF + optional conditions checklist  
- Responses: `STRATEGIC/JUDSON_REJECTION_SCRIPTS.md`

## Priority 4 — Cross-repo

| Check | |
|-------|---|
| Deal room Option A | https://fthtrading.github.io/T-Lev-8-/ |
| `governance-state.json` | `PARTNER_NEGOTIATE` |
| `npx hardhat compile` | ✅ |
| Sepolia deploy | ☐ |
| PDF exported | ☐ |
| Email sent | ☐ |

## Solo trigger

See `data/governance-state.json` + `AI_SYSTEM/PROTOCOL_GOVERNANCE_PROMPT.md` — MOU reimbursement or LEV8 contract control demand → `SOLO_LAUNCH`.
