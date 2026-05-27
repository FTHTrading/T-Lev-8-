# Aurora & Impact — Subdomain Deploy

Deploy each folder as its **own GitHub Pages site** (recommended) or Cloudflare Pages.

## Option A — Separate GitHub repos (recommended)

### `aurora.unykorn.org`

1. Create repo `FTHTrading/aurora` (or `aurora-unykorn`)
2. Copy `sites/aurora/index.html` to repo root as `index.html`
3. Add `.nojekyll` at repo root
4. Enable Pages → GitHub Actions (use default `static` workflow or copy from T-VEX-8-)
5. DNS: `CNAME` `aurora` → `fthtrading.github.io` (or custom Pages URL)
6. Verify: `curl -I https://aurora.unykorn.org` → **200**
7. Then 301 `therealestateconnections.com` → `https://aurora.unykorn.org`

### `impact.unykorn.org`

Same steps with `sites/impact/index.html` and CNAME `impact`.

## Option B — Cloudflare Pages (single account)

Upload `sites/aurora` and `sites/impact` as two Cloudflare Pages projects; attach custom domains.

## Until DNS is live

| Legacy domain | Interim target |
|---------------|----------------|
| therealestateconnections.com | `launch.unykorn.org` |
| green-n-go.solar | `troptions.unykorn.org/troptions` |

Do not 301 to aurora/impact until `curl -I` returns 200.
