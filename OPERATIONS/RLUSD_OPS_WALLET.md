# RLUSD on Ops Wallet (`rfbZz…`)

## Current state (public ledger)

| Field | Value |
|-------|-------|
| Trust line limit | 1,000,000 RLUSD |
| **Actual balance** | **~11.82 RLUSD** (not $1M) |
| Native XRP | ~12 XRP |
| Created | TrustSet succeeded (reserve ~0.2 XRP) |

**Trust line = permission ceiling.** Balance = what Ripple has sent you.

## Policy

- **Keep RLUSD on `rfbZz…` (ops)** — do not add RLUSD trust lines to `rJLMST…` (issuer).
- Issuer should only issue **your** IOUs (TROPTIONS, USDC gateway lines, etc.).

## Scripts (`rwa-realestate`)

```powershell
# Check (will print existing line and exit)
npm run xrpl:ledger-audit

# New trust line on ops wallet only (requires XRPL_OPS_SEED + MAINNET_SPEND_ENABLED)
node xrpl/scripts/create-trustline.js
```

## Recommended next step for revenue

**Option 2:** Trade ~11.82 RLUSD → XRP on XRPL DEX, send XRP to `rJLMST…` to raise issuer reserve above 11 XRP for batch issuance at scale.

Ops wallet signs; treasury IOUs stay on `rNX4fa…`.
