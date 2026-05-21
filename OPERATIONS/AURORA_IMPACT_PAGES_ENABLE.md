# Enable GitHub Pages — aurora-site & impact-site

**Repos:**  
- https://github.com/FTHTrading/aurora-site  
- https://github.com/FTHTrading/impact-site  

Workflow file already in each repo: `.github/workflows/pages.yml`  
`CNAME` files: `aurora.unykorn.org` / `impact.unykorn.org`

---

## Steps (each repo, ~2 minutes)

1. Open **Settings** → **Pages**  
   - aurora: https://github.com/FTHTrading/aurora-site/settings/pages  
   - impact: https://github.com/FTHTrading/impact-site/settings/pages  

2. **Build and deployment** → Source: **GitHub Actions**

3. **Actions** tab → open latest **Deploy to GitHub Pages** workflow  
   - If failed: re-run after Pages enabled  
   - If green: proceed to DNS verify  

4. DNS (`unykorn.org` zone):

| Host | Type | Value |
|------|------|--------|
| `aurora` | CNAME | `fthtrading.github.io` |
| `impact` | CNAME | `fthtrading.github.io` |

5. Verify (wait 5–30 min after DNS):

```powershell
curl.exe -sI https://aurora.unykorn.org/
curl.exe -sI https://impact.unykorn.org/
```

Expect **HTTP 200**.

6. Only then: activate worker redirects for `therealestateconnections.com` → aurora, `green-n-go.solar` → impact.

---

## Default URLs (before custom domain)

- https://fthtrading.github.io/aurora-site/  
- https://fthtrading.github.io/impact-site/

---

## If workflow fails

Error: *"repository has Pages enabled and configured to build using GitHub Actions"*  
→ You skipped step 2. Enable Pages source = GitHub Actions, then re-run workflow.
