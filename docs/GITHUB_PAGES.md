# GitHub Pages — T-VEX-8 Deal Room

**Default URL:** https://fthtrading.github.io/T-VEX-8-/

## Asset-path audit (2026-05-21)

| Check | Result |
|-------|--------|
| Root-absolute assets (`/assets/...`, `/images/...`) | **None found** |
| `fetch('data/governance-state.json')` | **Relative** — works under `/T-VEX-8-/` |
| External CSS | Google Fonts CDN only (OK) |
| Inline styles in `index.html` | OK |

**Verdict:** Safe to enable Pages without path rewrites.

## Enable Pages

1. Repo → **Settings** → **Pages**
2. Source: **GitHub Actions** (workflow `.github/workflows/pages.yml` already present)
3. Push to `main` or run workflow manually
4. Confirm deployment at https://fthtrading.github.io/T-VEX-8-/

## Optional custom domain

Create repo root file `CNAME` (only when DNS is ready):

```text
t-VEX.unykorn.org
```

DNS: `CNAME` record `t-VEX` → `fthtrading.github.io`

Then enable **Enforce HTTPS** in Pages settings.

## Recommended repo hygiene

- Add empty `.nojekyll` at repo root if Jekyll ever interferes with `_` paths
- Do not upload secrets or `.env` files (whole-repo artifact upload)
