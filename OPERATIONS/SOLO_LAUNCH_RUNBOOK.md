# SOLO_LAUNCH Runbook — TROPTIONS Only

**Trigger:** Judson insists on MOU reimbursement, VEX contract ownership, or 55% insider allocation.  
**Do not execute** while active negotiation is in progress unless a hard walk condition fires.

---

## Hour 0: Arm kill switch

1. Confirm `FTHEnforcer.sol` compiles in `rwa-realestate` (`npx hardhat compile`).
2. Deploy `TVEXGateManager` to Sepolia (solo use — no VEX partner address required for committee internal testing).
3. Update `T-VEX-8-/data/governance-state.json`:

```json
{
  "default_mode": "SOLO_LAUNCH",
  "active_partner": {
    "mode": "SOLO_LAUNCH",
    "name": "VEX Technologies, LLC — pipeline closed"
  },
  "solo": {
    "token": "AURORA",
    "status": "active"
  }
}
```

4. Commit and push governance state (internal visibility on deal room).

---

## Hour 1: Token config (no VEX input)

| Field | Value |
|-------|--------|
| Token | `$AURORA` (not `\$VEX`) |
| Supply | 100M fixed |
| Chain | Solana — devnet first; mainnet only after internal Launch Committee GO |
| Contract owner | TROPTIONS multisig (Article 6 default) |
| Mint | https://launch.unykorn.org |

---

## Hour 2: Schedule E bypass

- Use existing TROPTIONS sponsor tiers ($500 / $2,500 / $10,000).
- World Cup 2026 Atlanta remains anchor: https://troptionslive.unykorn.org/sports
- Remove VEX co-branding from any public troptionslive copy.

---

## Hour 4: Launch surfaces

- `aurora.unykorn.org` → deploy `sites/aurora/index.html` (see `sites/DEPLOY.md`) or redirect to `launch.unykorn.org` until site is live.
- Deal room: https://fthtrading.github.io/T-VEX-8-/
- Hero message: **TROPTIONS infrastructure. World Cup Atlanta. Live now.**

---

## Hour 24: Exchange listing

- List on TROPTIONS Exchange OS: https://troptionslive.unykorn.org/exchange-os
- Internal DEX only — no BitMart/Poloniex diligence required for solo path.

---

## Economics (solo)

| Item | Solo |
|------|------|
| Integration Fee | $0 (N/A) |
| Fee share | 100% TROPTIONS |
| Partner gates | N/A |

---

## Risks

- Smaller audience (no Judson legal distribution list).
- Faster path to mainnet if committee approves.
- Full contract ownership retained.

---

## Hard rule

If SOLO_LAUNCH executes, **do not re-engage VEX under old terms.** Any new deal starts at **Option C** (zero upfront, fee share only) plus cleared gates and new Master Agreement.

**Internal only:** Do not email Aurora comparison or nuclear-option docs to Judson.
