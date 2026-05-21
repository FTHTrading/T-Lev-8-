# Subdomain Activation — Aurora + Impact

## Repos (live on GitHub)

| Site | Repo | Default Pages URL |
|------|------|-------------------|
| Aurora | https://github.com/FTHTrading/aurora-site | https://fthtrading.github.io/aurora-site/ |
| Impact | https://github.com/FTHTrading/impact-site | https://fthtrading.github.io/impact-site/ |

## Your checklist (manual)

### 1. Enable GitHub Pages (both repos)

Settings → Pages → Build and deployment → **GitHub Actions**  
Then re-run the `Deploy to GitHub Pages` workflow if the first run failed (Pages must be enabled before deploy succeeds).

### 2. DNS (`unykorn.org` zone)

| Host | Type | Value |
|------|------|--------|
| `aurora` | CNAME | `fthtrading.github.io` |
| `impact` | CNAME | `fthtrading.github.io` |

GitHub repo already contains `CNAME` files (`aurora.unykorn.org`, `impact.unykorn.org`).

Verify:

```powershell
curl.exe -sI https://aurora.unykorn.org/
curl.exe -sI https://impact.unykorn.org/
```

Expect **200** before activating legacy redirects to these hosts.

### 3. Cloudflare Worker

Paste `CLOUDFLARE_WORKER_SCRIPT.js` (14 hostnames / 7 brands).  
Custom domains: apex + www for each zone you control.

**Order:** Deploy Aurora/Impact Pages **first**, then map `therealestateconnections.com` and `green-n-go.solar` on the worker (otherwise 301 → dead subdomain).

### 4. Worker domains (complete map)

| Hostname(s) | Target |
|-------------|--------|
| troptionsxchange.io (+ www) | troptionslive…/exchange-os |
| troptions-university.com (+ www) | fthedu.unykorn.org |
| troptionstelevisionnetwork.tv (+ www) | troptionslive…/sports |
| hotrcw.com (+ www) | troptionslive…/ |
| troptions.io (+ www) | troptions.unykorn.org/troptions |
| therealestateconnections.com (+ www) | aurora.unykorn.org |
| green-n-go.solar (+ www) | impact.unykorn.org |
