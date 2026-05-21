# Legacy Domain Redirects — Verified Targets

**Last verified:** 2026-05-21 (HTTP HEAD)

## Live targets (safe to 301)

| Legacy domain | Redirect to | Status |
|---------------|-------------|--------|
| `troptionsxchange.io` / `.com` | https://troptionslive.unykorn.org/exchange-os | ✅ 200 |
| `troptions-university.com` | https://fthedu.unykorn.org/ | ✅ 200 (11 tracks, 36 courses — already built) |
| `troptionstelevisionnetwork.tv` | https://troptionslive.unykorn.org/sports | ✅ 200 |
| `hotrcw.com` | https://troptionslive.unykorn.org/ | ✅ 200 |
| `troptions.io` | https://troptions.unykorn.org/troptions | ✅ 200 |

## Park until subdomain is live (do not 301 to dead host)

| Subdomain | HTTP check | Interim for legacy brand |
|-----------|------------|--------------------------|
| `aurora.unykorn.org` | ❌ 404 / NXDOMAIN | `therealestateconnections.com` → **launch.unykorn.org** only |
| `impact.unykorn.org` | ❌ 404 / NXDOMAIN | `green-n-go.solar` → **troptions.unykorn.org/troptions** only |

## Park until DNS exists (do not 301 yet)

| Legacy domain | Planned target | Status |
|---------------|----------------|--------|
| `therealestateconnections.com` | https://launch.unykorn.org (Aurora mint) **or** future `aurora.unykorn.org` | ❌ `aurora.unykorn.org` NXDOMAIN |
| `green-n-go.solar` | https://troptions.unykorn.org/troptions (impact placeholder) | ❌ `impact.unykorn.org` NXDOMAIN |

## Aurora naming

| Purpose | URL |
|---------|-----|
| **Token mint / demo** | https://launch.unykorn.org ✅ |
| **RWA brand site (future)** | `aurora.unykorn.org` — not deployed |

## Cloudflare Page Rules (301 — Pro/Business)

Free plan: only 3 Page Rules — use **Worker** below instead.

| URL pattern | Forward to |
|-------------|------------|
| `*troptionsxchange.io/*` | https://troptionslive.unykorn.org/exchange-os |
| `*troptions-university.com/*` | https://fthedu.unykorn.org/ |
| `*troptionstelevisionnetwork.tv/*` | https://troptionslive.unykorn.org/sports |
| `*hotrcw.com/*` | https://troptionslive.unykorn.org/ |
| `*troptions.io/*` | https://troptions.unykorn.org/troptions |

**Zone settings (all legacy zones):** SSL Full (strict) · Always Use HTTPS ON · Automatic HTTPS Rewrites ON

## Cloudflare Worker (Free plan — all 5+ domains)

See `REBRAND/cloudflare-worker-legacy-redirects.js` — attach route `*domain.com/*` per zone.

## DNS health check (run before adding redirects)

```bash
curl -I https://troptionslive.unykorn.org/exchange-os
curl -I https://fthedu.unykorn.org/
curl -I https://troptionslive.unykorn.org/sports
curl -I https://troptions.unykorn.org/troptions
curl -I https://aurora.unykorn.org
curl -I https://impact.unykorn.org
# Park aurora/impact until 200 OK
```

## Wrong targets (do not use)

| Wrong | Why |
|-------|-----|
| `exchange.unykorn.org` | Subdomain does not resolve |
| `troptions.unykorn.org/university` | Use **fthedu.unykorn.org** |
| `ttn.unykorn.org` | Subdomain does not resolve — use **troptionslive…/sports** |

**Note:** `troptionsexchange.unykorn.org/exchange-os` also returns 200; legacy Bryan domains should use **troptionslive** per live portal map.

## Future builds (parked subdomains)

| Host | Brand | Build spec (when ready) |
|------|-------|-------------------------|
| `aurora.unykorn.org` | Real estate / RWA | Property funnel, `.troptions` NFT collateral, TTN Local open houses — stack: rwa-realestate + launch.unykorn.org |
| `impact.unykorn.org` | Green-N-Go / ESG | Solar ROI tracker, carbon credits, project funding — reuse Apostle/IPFS proof layer |

Do not 301 legacy traffic here until HTTP 200 on these hosts.
