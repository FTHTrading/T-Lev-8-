# Next 48 Hours — Exact Order

| Step | Task | Time | Blocker |
|------|------|------|---------|
| 1 | Enable GitHub Pages on `FTHTrading/T-Lev-8-` | 2 min | You (Settings UI) |
| 2 | Deploy Cloudflare Worker (5 domains) | 5 min | You (dashboard) |
| 3 | Create `rwa-realestate/.env` + Sepolia deploy | 15 min | Burner key |
| 4 | Print PDF + send Judson | 10 min | You |
| 5 | SOLO_LAUNCH only if Judson walks | — | `OPERATIONS/SOLO_LAUNCH_RUNBOOK.md` |

**Do not build T-Build launch-committee panel until Judson responds.**

---

## Step 1 — GitHub Pages

Settings → Pages → Source: **GitHub Actions**  
Live URL: https://fthtrading.github.io/T-Lev-8-/  
Audit: `docs/GITHUB_PAGES.md` (passed)

---

## Step 2 — Cloudflare Worker

Paste `REBRAND/cloudflare-worker-legacy-redirects.js` → Workers → Custom Domains (apex + www for each zone).

---

## Step 3 — Sepolia

```powershell
cd "C:\Users\Kevan\Documents\UNYKORN_Ecosystem\rwa-realestate"
# Create .env from .env.example
npx hardhat run scripts/tlev8/deploy_gate_manager.js --network sepolia
node scripts/tlev8/pin_to_governance.js
```

Updates `data/governance-state.json` → `on_chain.gate_manager_sepolia`.

---

## Step 4 — Judson

1. Print `STRATEGIC/TERM_SHEET_v1.2.html` → PDF  
2. Send `STRATEGIC/JUDSON_EMAIL_FINAL.md`  
3. Set `active_partner.term_sheet_sent` in `data/governance-state.json`

Checklist: `STRATEGIC/TERM_SHEET_PRE_SEND_VALIDATION.md`

---

## Optional — Aurora / Impact sites

`sites/aurora/index.html` and `sites/impact/index.html` — see `sites/DEPLOY.md`.  
Activate legacy redirects only after `curl -I` shows 200 on subdomains.
