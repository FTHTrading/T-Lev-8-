# Go Live + Revenue (TROPTIONS XRPL)

**You confirmed:** ops seed is on this machine (intentional). **Do not paste seeds into chat or Git.**

## Wallet roles (use the right key for each job)

| Role | Address | Use for |
|------|---------|---------|
| Issuer | `rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ` | Token/NFT issuance, trust lines (needs more XRP reserve) |
| Distribution / fees | `rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt` | IOU treasury, **all platform fee sweeps** |
| Ops / spend | `rfbZzM6SGZHbfxrg85vyeKSEMMQCfNXTNw` | Small XRP ops, batch demos, merchant pilots (~12 XRP + RLUSD) |
| AMM | `rBU6exSQHkrTog6n1F5RX8gzcUrXoniGcp` | Liquidity (read-only unless LP keys separate) |

## Local `.env` (rwa-realestate/xrpl/.env` — never commit)

```env
XRPL_ISSUER_ADDRESS=rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ
XRPL_FEE_WALLET=rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt
XRPL_OPS_ADDRESS=rfbZzM6SGZHbfxrg85vyeKSEMMQCfNXTNw
XRPL_OPS_SEED=<your family seed — local only>
XRPL_ISSUER_SEED=<issuer seed if separate — local only>
MAINNET_SPEND_ENABLED=true
DRY_RUN=false
```

**troptions** (Cloudflare / local): `EXCHANGE_OS_XRPL_MAINNET_ENABLED=true`, `TROPTIONS_XRPL_ISSUER`, `TROPTIONS_XRPL_FEE_WALLET` as above.

## Verify (no secrets printed)

```powershell
cd C:\Users\Kevan\Documents\UNYKORN_Ecosystem\rwa-realestate
npm run xrpl:go-live-check
npm run xrpl:ledger-audit
npm run xrpl:phases
```

## Fastest cash (30 days)

1. **Exchange OS Batch tab** — demo Atomic Launch + Merchant Bundle to Judson / WC26 (`/exchange-os/batch`).
2. **Merchant onboarding** — $50 USDC-style fee in `INDEPENDENT` batch (scenario 02).
3. **Atomic launch** — 1.5% on NFT/MPT mint+list (scenario 01) once issuer reserve funded.
4. **Integration escrow** — GivBux/LEV8 only with cash upfront (existing term sheets).

## ETH / Base USDT

If a flow needs ETH gas: sell Base USDT via your existing off-ramp — **not** wired in this repo. XRPL revenue does not require ETH.

## Issuer reserve

`rJLMST…` has ~1.2 XRP — **below** 11 XRP gate for heavy issuance. **Ops wallet** can still run small batches; fund issuer when you mint at scale.
