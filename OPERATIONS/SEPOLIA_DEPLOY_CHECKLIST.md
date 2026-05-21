# Sepolia Gate Manager — Deploy Checklist

**Purpose:** Live on-chain proof for deal room + all partner negotiations (LEV8, GivBux, sponsors).  
**Repo:** `rwa-realestate` · **Pins to:** `T-Lev-8-/data/governance-state.json`

---

## Prerequisites

- [ ] Sepolia burner wallet funded (≥ 0.05 ETH recommended)
- [ ] Alchemy (or other) Sepolia RPC URL
- [ ] `ETHERSCAN_API_KEY` (optional, for verify)

```powershell
cd "C:\Users\Kevan\Documents\UNYKORN_Ecosystem\rwa-realestate"
copy .env.tlev8.example .env
# Edit: SEPOLIA_RPC_URL, PRIVATE_KEY, ETHERSCAN_API_KEY
```

**Never commit `.env`.**

---

## Deploy

```powershell
cd "C:\Users\Kevan\Documents\UNYKORN_Ecosystem\rwa-realestate"
npx hardhat compile
npx hardhat run scripts/tlev8/deploy_gate_manager.js --network sepolia
node scripts/tlev8/pin_to_governance.js
```

---

## Capture (paste into deal room / notes)

| Field | Value |
|-------|-------|
| Contract address | `0x...` from deploy output |
| Deployer | `0x...` |
| Network | sepolia |
| Etherscan | https://sepolia.etherscan.io/address/`0x...` |
| Deploy artifact | `rwa-realestate/deployments/tlev8-gate-manager-sepolia.json` |
| Pinned file | `T-Lev-8-/data/governance-state.json` → `on_chain.gate_manager_sepolia` |

---

## Verify governance JSON

```json
"on_chain": {
  "gate_manager_sepolia": "0xYOUR_ADDRESS",
  "last_deploy": {
    "network": "sepolia",
    "deployer": "0x...",
    "at": "ISO timestamp"
  }
}
```

Commit and push `T-Lev-8-` after pin (no private keys in repo).

---

## Optional: Etherscan verify

```powershell
npx hardhat verify --network sepolia DEPLOYED_ADDRESS
```

---

## Post-deploy smoke

```powershell
npx hardhat run scripts/tlev8/verify_gates.js --network sepolia
```

---

## If deploy fails

| Error | Fix |
|-------|-----|
| Insufficient funds | Fund burner |
| Invalid key | Check `PRIVATE_KEY` format (0x prefix) |
| RPC error | Rotate Alchemy key |
| Pin script missing JSON | Re-run deploy script first |

---

**Do not pause this for GivBux.** Sepolia strengthens every revenue lane.
