# 72-Hour SOLO_LAUNCH Playbook (Aurora)

**Trigger:** `SOLO_LAUNCH` per `data/governance-state.json`  
**Owner:** Engineering + Bryan Stone (marketing approval)

---

## Hour 0 — Decision

- [ ] Confirm `gates_cleared < 5` or Day-30 timeout or Judson walk-away  
- [ ] Log decision in `STRATEGIC/RETROSPECTIVE_LOG.md`  
- [ ] Set `governance-state.json` → `mode: SOLO_LAUNCH`

---

## Hours 0–24 — Send / wait

| If not yet sent | Action |
|-----------------|--------|
| Term sheet pending | Send `JUDSON_EMAIL_FINAL` + PDFs first |
| Already sent, waiting | Monitor pipeline; no Aurora public announcement yet |

| If walk-away | Action |
|--------------|--------|
| Treasury clawback demanded | Close LEV8 track; start Hour 24 mint |

---

## Hours 24–48 — Mint + verify

| Step | Action | Doc |
|------|--------|-----|
| 1 | Infrastructure check | `LAUNCH_NOW/QUICKSTART.md` Step 1–3 |
| 2 | Mint AURORA 500M, revoke mint | launch.unykorn.org |
| 3 | Solscan verify | Record mint in `IPFS/EXECUTION_MANIFEST.md` |
| 4 | Devnet test (optional) | Jupiter quote smoke test |

---

## Hours 48–72 — Integrate + announce

| Step | Action |
|------|--------|
| 5 | Meteora AURORA/USDC seed liquidity |
| 6 | Exchange OS Solana tab + wallet adapters |
| 7 | Internal announcement (no LEV8 mention) |
| 8 | Update deal room: Aurora live, LEV8 pipeline closed |

---

## Do not

- Mention Judson/LEV8 in Solo marketing  
- Attach Aurora comparison to any partner email  
- Skip mint authority revoke on mainnet  

---

## Success criteria

- [ ] Live SPL mint on Solscan  
- [ ] Pool address published  
- [ ] Exchange OS shows AURORA pair  
- [ ] `governance-state.json` updated with `aurora_mint` address
