# IPFS EXECUTION MANIFEST

## Document Registry

| # | Document | Version | SHA-256 | IPFS CID | Status | Date |
|---|----------|---------|---------|----------|--------|------|
| 1 | MASTER_AGREEMENT.md | 1.0-draft | pending | pending | Pre-Execution | 2026-05-20 |
| 2 | TOKEN_LISTING_POLICY.md | 1.0 | pending | pending | Draft | 2026-05-20 |
| 3 | REGULATORY_KILL_SWITCH.md | 1.0 | pending | pending | Pre-Execution | 2026-05-20 |
| 4 | LEGAL_OPINION.pdf | &#x2014; | &#x2014; | &#x2014; | Awaiting Gate | &#x2014; |
| 5 | AUDIT_REPORT.pdf | &#x2014; | &#x2014; | &#x2014; | Awaiting Gate | &#x2014; |

## Pinning Instructions

1. Generate SHA-256: `sha256sum [filename]`
2. Upload to Pinata: `pinata.pinFileToIPFS(filepath)`
3. Record CID in this manifest
4. Verify on gateway: `https://gateway.pinata.cloud/ipfs/[CID]`
5. Notarize on Solana: `solana memo [CID] [tx]`

## Verification Commands

```bash
# Generate hash
sha256sum LEGAL/MASTER_AGREEMENT.md

# Pin to IPFS
curl -X POST "https://api.pinata.cloud/pinning/pinFileToIPFS" \
  -H "Authorization: Bearer [JWT]" \
  -F "file=@LEGAL/MASTER_AGREEMENT.md"

# Verify
ipfs cat [CID] | sha256sum
```

## Status: ACTIVE — All documents awaiting execution

**Next Action:** Populate with actual CIDs upon document finalization
