# Operator Assistant Boundaries (UNYKORN)

## What the AI assistant CAN do

- Read **public** XRPL/Stellar/Ethereum explorers and summarize balances, txs, offers.
- Build and run **unsigned** transaction JSON (batch, NFT mint plans, escrow, checks).
- Maintain `OPERATIONS/`, deal room, Exchange OS UI, compliance docs.
- Run `npm run xrpl:operator` **on your machine** when you approve — reads env locally, never sends seeds to the model.
- Integrate **Finn voice** to read status files aloud and offer menu choices.

## What the AI assistant CANNOT do

- Accept or store `sn...` seeds, private keys, or API secrets in chat.
- Sign mainnet transactions without **you** running local CLI with `.env`.
- Move XRP/IOU from your wallets remotely.

## Your three signing roles

| Role | Address | Seed env var |
|------|---------|--------------|
| Issuer | `rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ` | `XRPL_ISSUER_SEED` |
| Ops | `rfbZzM6SGZHbfxrg85vyeKSEMMQCfNXTNw` | `XRPL_OPS_SEED` |
| Fee destination | `rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt` | (receive only) |

## Mint / NFT policy

- **Issuer XRP ≥ 10** before large mints (currently ~1.20 — halted).
- Use **authorized minter** hot wallet for NFT series when implemented — preserves issuer reserve.
- All mint metadata: `OPERATIONS/NFT_METADATA_TEMPLATE.md`.

## Verbal operator flow (Finn)

1. You: “Run ledger audit.”
2. Finn runs `npm run xrpl:ledger-audit` locally, speaks summary from JSON.
3. You: “Fund issuer” → Finn explains paths, does **not** ask for seed in speech.

This is **your** system; the assistant is the control layer, not the custodian.
