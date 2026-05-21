# XRPL Wallet Inventory (TROPTIONS)

**Last ledger audit:** Run `npm run xrpl:ledger-audit` in `rwa-realestate`.

## Canonical production wallets (Wallet Hub / Exchange OS)

| Role | Address | Ledger role |
|------|---------|-------------|
| **Issuer** | `rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ` | Issues TROPTIONS, USDC, USDT, DAI, EURC obligations to distribution |
| **Distribution** | `rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt` | Holds IOUs, LP shares, **fee sweep destination** |
| **AMM pool** | `rBU6exSQHkrTog6n1F5RX8gzcUrXoniGcp` | AMM liquidity account |

Explorer: [xrpscan issuer](https://xrpscan.com/account/rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ) · [distribution](https://xrpscan.com/account/rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt)

## Misaligned address in scripts (fix env)

| Address | Where used | Status |
|---------|------------|--------|
| `rPF2M1QjdVh1hkNgmMMTkT9qMU7tA7Wds3` | `rwa-realestate/xrpl/*` defaults, old governance JSON | **NOT** live issuer — ~3 XRP, no trust lines |

Set `XRPL_ISSUER_ADDRESS=rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ` and `XRPL_FEE_WALLET=rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt` in `.env` (never commit seeds).

## User-reported wallet (public ledger)

| Field | Value |
|-------|-------|
| Address | `rfbZzM6SGZHbfxrg85vyeKSEMMQCfNXTNw` |
| Balance | ~12 XRP |
| Trust lines | RLUSD (not TROPTIONS) |
| Inbound | 20 XRP from `rnJrjec2vrTJAAQUTMTjj7U6xdXrk9N4mT`, dest tag `1001` |

**Not** issuer, distribution, or fee treasury. Control requires local `sn...` seed — never paste seeds in chat.

## Testnet

| Address | Purpose |
|---------|---------|
| `rGaiC1bw8uND7Z9XzzpcAWyAuH72p82HES` | Dev wallet (`xrpl/testnet-wallet.json`, gitignored) |

Batch submit on testnet: `temDISABLED` until Batch amendment is active on altnet.

## Security

- Seeds live only in local `.env`, password manager, or HSM.
- AI cannot search your machine or spend funds.
- Rotate any credential ever pasted into chat.
