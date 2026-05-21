# Legacy Domain Redirects — Verified Targets

**Last verified:** 2026-05-21 (HTTP HEAD)

## Live targets (safe to 301)

| Legacy domain | Redirect to | Status |
|---------------|-------------|--------|
| `troptionsxchange.io` / `.com` | https://troptionslive.unykorn.org/exchange-os | ✅ 200 |
| `troptions-university.com` | https://fthedu.unykorn.org/ | ✅ 200 (11 tracks, 36 courses — already built) |
| `troptionstelevisionnetwork.tv` | https://troptionslive.unykorn.org/sports | ✅ 200 |
| `hotrcw.com` | https://troptionslive.unykorn.org/ | ✅ 200 |

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

## Cloudflare bulk redirect rules

```text
(http.host eq "troptionsxchange.io" or http.host eq "www.troptionsxchange.io")
  → 301 https://troptionslive.unykorn.org/exchange-os

(http.host eq "troptions-university.com" or http.host eq "www.troptions-university.com")
  → 301 https://fthedu.unykorn.org/

(http.host eq "troptionstelevisionnetwork.tv" or http.host eq "www.troptionstelevisionnetwork.tv")
  → 301 https://troptionslive.unykorn.org/sports

(http.host eq "hotrcw.com" or http.host eq "www.hotrcw.com")
  → 301 https://troptionslive.unykorn.org/
```

## Wrong targets (do not use)

| Wrong | Why |
|-------|-----|
| `exchange.unykorn.org` | Subdomain does not resolve |
| `troptions.unykorn.org/university` | Use **fthedu.unykorn.org** |
| `ttn.unykorn.org` | Subdomain does not resolve — use **troptionslive…/sports** |

**Note:** `troptionsexchange.unykorn.org/exchange-os` also returns 200; legacy Bryan domains should use **troptionslive** per live portal map.
