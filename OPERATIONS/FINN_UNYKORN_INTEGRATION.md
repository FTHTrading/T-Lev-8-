# Finn ↔ UNYKORN Integration

**Finn repo:** https://github.com/FTHTrading/Finn  
**Local:** `C:\Users\Kevan\Finn`

Finn is the **verbal + visual operator** for UNYKORN. He does not hold XRPL seeds in the cloud — he runs local tools against your repos.

## Capabilities wired

| You say (to Finn) | What runs |
|-------------------|-----------|
| "Audit all XRPL wallets" | `unykorn.xrpl.audit` → `npm run xrpl:ledger-audit` |
| "Go-live check" | `unykorn.xrpl.golive` |
| "Deal room status" | `unykorn.governance` |
| "Ask the GPU brain …" | Genesis → Ollama (5090) → NIM |
| Quantum tasks | Existing QBR tools (silent, operator-only) |

## Start

```powershell
C:\Users\Kevan\Finn\scripts\Start-UnykornFinnStack.ps1
cd C:\Users\Kevan\Finn
python run.py
```

## XRPL wallets (canonical)

| Role | Address |
|------|---------|
| Issuer | `rJLMSTy77hTxqgDw9WMxCnYC8m5vhqN3FQ` |
| Distribution / fees | `rNX4faQ35SdtE4rDoEg8YeVLQKQ57AYyCt` |
| Ops signer | `rfbZzM6SGZHbfxrg85vyeKSEMMQCfNXTNw` |

See `UNYKORN_CONTROL_PLANE.md` and `WALLET_ADDRESS_REGISTRY.md`.
