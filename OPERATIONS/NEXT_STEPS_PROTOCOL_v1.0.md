# T-LEV-8 Next Steps Protocol

**TO:** Operations Agent / Bryan Stone / FTH Trading  
**FROM:** T-LEV-8 Protocol Governor  
**RE:** 72-Hour Execution Sequence (Judson Outreach → Contract Deploy → Decision Branch)  
**VERSION:** 1.0  
**STATE:** Repos synced · Option A term sheet ready · Gate manager compiled · Sepolia deploy pending `.env`

---

## I. IMMEDIATE 24-HOUR ACTIONS (Hour 0–24)

### 1.1 Complete environment setup (blocked until `.env` exists)

**Repo:** `C:\Users\Kevan\Documents\UNYKORN_Ecosystem\rwa-realestate`  
**File:** `.env` (copy from `.env.example` — **never commit**)

```env
SEPOLIA_RPC_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
PRIVATE_KEY=YOUR_BURNER_KEY_NO_0x_PREFIX_IN_FILE_OK
ETHERSCAN_API_KEY=YOUR_KEY
# Optional: grant COUNSEL_ROLE to production multisig after deploy
COUNSEL_MULTISIG=0xYourGnosisSafe
```

```powershell
cd "C:\Users\Kevan\Documents\UNYKORN_Ecosystem\rwa-realestate"
Copy-Item .env.example .env
# Edit .env with real values, then:
npx hardhat run scripts/tlev8/deploy_gate_manager.js --network sepolia
```

**Success output to capture:**

```
Deploying TLEV8GateManager with: 0x...
TLEV8GateManager deployed to: 0x...
Granted COUNSEL_ROLE to: 0x...   # if COUNSEL_MULTISIG set
Wrote .../deployments/tlev8-gate-manager-sepolia.json
```

**Pin address in deal room:**

```powershell
cd "C:\Users\Kevan\Documents\UNYKORN_Ecosystem\rwa-realestate"
node scripts/tlev8/pin_to_governance.js
```

Or manually set in `T-Lev-8-/data/governance-state.json`:

```json
"on_chain": {
  "gate_manager_sepolia": "0x...",
  "gate_manager_mainnet": null,
  "rwa_repo": "https://github.com/FTHTrading/rwa-realestate"
}
```

**Verify on Sepolia:** `https://sepolia.etherscan.io/address/0x...`

---

### 1.2 Export term sheet v1.2 PDF

```powershell
cd "C:\Users\Kevan\Documents\UNYKORN_Ecosystem\T-Lev-8-"
Start-Process "STRATEGIC\TERM_SHEET_v1.2.html"
# Browser: Ctrl+P → Save as PDF → STRATEGIC\TROPTIONS_LEV8_Term_Sheet_v1.2.pdf
```

**Pre-send checklist (fail = do not send):**

- [ ] Section 3: **LEV8 pays TROPTIONS** $10,000 Platform Integration Fee  
- [ ] No "reimbursement," "Day-1 project funds," or MOU §1.02 language  
- [ ] No "$20,000 Net Fee recoup" / Advance recoup clause  
- [ ] Section 3A: TROPTIONS owns smart contracts  
- [ ] Tiered fee share 60/40 → 50/50 → 40/60 present  

Optional second attachment: export `COMPLIANCE/CONDITIONS_CHECKLIST_FOR_JUDSON.md` → PDF.

---

### 1.3 Send Judson outreach (Option A framing)

| Field | Value |
|-------|--------|
| **Subject** | T-LEV-8 Partnership — Definitive Terms (MOU Superseded) |
| **To** | jleibee@judsoncharles.com |
| **Cc** | vladvc935@gmail.com |
| **Body** | `STRATEGIC/JUDSON_EMAIL_FINAL.md` |
| **Attach** | `TROPTIONS_LEV8_Term_Sheet_v1.2.pdf` |

After send, update `data/governance-state.json`:

```json
"term_sheet_sent": "2026-05-21"
```

**Do not attach:** Aurora brief, comparison table, source PDF findings.

---

## II. HOUR 24–48 — MONITOR & DOCUMENT

### 2.1 Gate manager smoke test (Sepolia)

```powershell
$env:GATE_MANAGER="0x..."   # from deploy output
$env:PARTNER="0x0000000000000000000000000000000000000001"
npx hardhat run scripts/tlev8/verify_gates.js --network sepolia
# Expected: exit code 1 (partner not approved) — confirms contract live
```

### 2.2 Deal room verification

- https://fthtrading.github.io/T-Lev-8-/ — Governor shows `PARTNER_NEGOTIATE`, `0/8` gates  
- GitHub Pages rebuild may lag 1–2 min after push  

### 2.3 Internal log

Record in `PIPELINE/PARTNER_PIPELINE.md`: term sheet sent date, deploy tx hash, deployer address.

---

## III. HOUR 48–72 — DECISION BRANCH

| Judson response | Action | Governor mode |
|-----------------|--------|----------------|
| Accepts Option A | Schedule Master + IP Assignment; request Gate 1 & 2 | `PARTNER_NEGOTIATE` → path to `PARTNER_EXECUTE` |
| "Can't pay $10K" | Offer Option C (50/50 flat, higher KPIs) — `JUDSON_REJECTION_SCRIPTS.md` Branch 2 | `PARTNER_NEGOTIATE` |
| Demands MOU reimbursement | Branch 3 — **WALK** | `SOLO_LAUNCH` (72h clock) |
| Demands LEV8-owned contracts | Branch 4 — **WALK** | `SOLO_LAUNCH` |
| 55% insider fixed | Branch 5 — **WALK** | `SOLO_LAUNCH` |
| Silence >14 days | Branch 6 — close loop | `SOLO_LAUNCH` |

### Solo Mode activation (PowerShell)

```powershell
cd "C:\Users\Kevan\Documents\UNYKORN_Ecosystem\T-Lev-8-"
$data = Get-Content "data/governance-state.json" -Raw | ConvertFrom-Json
$data.active_partner.mode = "SOLO_LAUNCH"
$data.default_mode = "SOLO_LAUNCH"
$data.solo.status = "active"
$data.updated = (Get-Date).ToUniversalTime().ToString("o")
$data | ConvertTo-Json -Depth 10 | Set-Content "data/governance-state.json" -Encoding utf8
git add data/governance-state.json
git commit -m "system: Solo Mode activated — partner pipeline stalled"
git push origin main
```

Aurora mint: `https://launch.unykorn.org` (internal only — do not market to Judson).

---

## IV. CROSS-REPO STATUS BOARD

| Item | Repo | Status |
|------|------|--------|
| Option A term sheet | T-Lev-8- | ✅ |
| Article 6 contract ownership | T-Lev-8- | ✅ |
| IP Assignment template | T-Lev-8- | ✅ |
| `TLEV8GateManager.sol` compile | rwa-realestate | ✅ |
| Sepolia deploy | rwa-realestate | ☐ `.env` required |
| Governance address pinned | T-Lev-8- | ☐ after deploy |
| PDF exported | T-Lev-8- | ☐ browser print |
| Judson email sent | — | ☐ |
| `term_sheet_sent` in JSON | T-Lev-8- | ☐ |

---

## V. FILE INDEX

| Purpose | Path |
|---------|------|
| This protocol | `OPERATIONS/NEXT_STEPS_PROTOCOL_v1.0.md` |
| Short checklist | `OPERATIONS/72_HOUR_EXECUTION.md` |
| Governor rules | `AI_SYSTEM/PROTOCOL_GOVERNANCE_PROMPT.md` |
| Email body | `STRATEGIC/JUDSON_EMAIL_FINAL.md` |
| Response scripts | `STRATEGIC/JUDSON_REJECTION_SCRIPTS.md` |
| Deploy | `rwa-realestate/scripts/tlev8/deploy_gate_manager.js` |
| Verify gates | `rwa-realestate/scripts/tlev8/verify_gates.js` |
| Pin address | `rwa-realestate/scripts/tlev8/pin_to_governance.js` |

---

*Protocol Governor v1.0 — execution subject to Bryan Stone written waiver only.*
