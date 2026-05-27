# 🚀 T-VEX-8 Deployment Guide

## Prerequisites

- [ ] Git installed (`git --version`)
- [ ] GitHub account with access to `FTHTrading/T-VEX-8-` repo
- [ ] Authentication set up (SSH key or Personal Access Token)

---

## Quick Deploy (Windows)

### Method 1: PowerShell Script (Recommended)

```powershell
# Navigate to the package folder
cd C:\Users\Kevan\Documents\UNYKORN_Ecosystem\T-VEX-8-

# Run the deploy script
.\deploy.ps1
```

### Method 2: Manual Git Commands

```powershell
# Step 1: Navigate to package
cd C:\Users\Kevan\Documents\UNYKORN_Ecosystem\T-VEX-8-

# Step 2: Initialize git (if not already)
git init
git remote add origin https://github.com/FTHTrading/T-VEX-8-.git

# Step 3: Stage all files
git add .

# Step 4: Commit
git commit -m "feat: T-VEX-8 automated launch v1.0"

# Step 5: Push
git push -u origin main
```

---

## Quick Deploy (Mac/Linux)

```bash
# Navigate to the package folder
cd ~/Documents/UNYKORN_Ecosystem/T-VEX-8-

# Make script executable and run
chmod +x deploy.sh
./deploy.sh
```

---

## Enable GitHub Pages (1 minute)

1. Go to: https://github.com/FTHTrading/T-VEX-8-/settings/pages
2. Under **Build and deployment** → **Source**: select **GitHub Actions**
3. Click **Save**
4. Wait 2 minutes for the workflow to run

---

## Verify Deployment

```bash
# Check if site is live
curl -s https://fthtrading.github.io/T-VEX-8-/ | head -20

# Or open in browser
start https://fthtrading.github.io/T-VEX-8-/
```

---

## Troubleshooting

### ❌ "Repository not found"

**Fix:** The repo doesn't exist yet. Create it:
1. Go to https://github.com/new
2. Name: `T-VEX-8-`
3. Owner: `FTHTrading`
4. Click **Create repository**
5. Then retry deploy

### ❌ "Permission denied"

**Fix:** Authenticate with GitHub:
```bash
# Option 1: GitHub CLI
gh auth login

# Option 2: Use token
 git remote set-url origin https://TOKEN@github.com/FTHTrading/T-VEX-8-.git
```

### ❌ "Push rejected"

**Fix:** Pull first, then push:
```bash
git pull origin main --rebase
git push origin main
```

---

## File Structure

```
T-VEX-8-/
├── index.html                          # Liquid glass deal room site
├── README.md                           # Repository documentation
├── deploy.ps1                          # Windows deploy script
├── deploy.sh                           # Linux/Mac deploy script
├── DEPLOY.md                           # This file
├── INTEGRATION.md                      # needai integration guide
├── .github/
│   └── workflows/
│       ├── pages.yml                   # GitHub Pages deployment
│       └── ai-legal-review.yml         # PR review automation
├── LEGAL/
│   ├── MASTER_AGREEMENT.md            # Two-party agreement
│   ├── TOKEN_LISTING_POLICY.md        # Listing requirements
│   └── REGULATORY_KILL_SWITCH.md      # Kill switch protocol
├── AI_SYSTEM/
│   └── LEGAL_ARCHITECT_PROMPT.md      # AI monitoring protocol
├── IPFS/
│   └── EXECUTION_MANIFEST.md          # CID registry
├── COMPLIANCE/                        # (empty, for future)
└── EVIDENCE/                           # (empty, for future)
```

---

## Post-Deployment Checklist

- [ ] Site loads at `https://fthtrading.github.io/T-VEX-8-/`
- [ ] All 8 conditions show "Pending"
- [ ] Progress bar shows 0%
- [ ] Kill switch terminal renders
- [ ] Theme toggle works (dark/light)
- [ ] Mobile responsive (check on phone)
- [ ] Links to needai site work
- [ ] GitHub Actions shows green checkmark

---

## Need Help?

Contact: DONK AI for UNYKORN
Date: 2026-05-20
