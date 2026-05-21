# T-LEV-8 Auto-Deploy Script for Windows
# Run this in PowerShell as Administrator (optional but recommended)

param(
    [string]$RepoUrl = "https://github.com/FTHTrading/T-Lev-8-.git",
    [string]$Branch = "main"
)

Write-Host @"
🚀 T-LEV-8 Automated Deployment Script
=========================================
"@ -ForegroundColor Cyan

# Check if git is installed
$gitVersion = git --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Git not found. Install from https://git-scm.com/download/win" -ForegroundColor Red
    exit 1
}
Write-Host "✅ Git detected: $gitVersion" -ForegroundColor Green

# Check if repo exists locally
$repoName = ($RepoUrl -split '/')[-1] -replace '\.git$',''
if (Test-Path "$repoName\.git") {
    Write-Host "📂 Repo exists locally. Pulling latest..." -ForegroundColor Yellow
    Set-Location $repoName
    git pull origin $Branch
} else {
    Write-Host "📥 Cloning repository..." -ForegroundColor Yellow
    git clone $RepoUrl
    Set-Location $repoName
}

# Verify we're in the repo
if (-not (Test-Path ".git")) {
    Write-Host "❌ Not a git repository. Exiting." -ForegroundColor Red
    exit 1
}

# Check remote access
Write-Host "🔍 Verifying remote access..." -ForegroundColor Cyan
$remoteTest = git ls-remote --heads origin 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️ Cannot access remote. You may need to authenticate." -ForegroundColor Yellow
    Write-Host "   Options:"
    Write-Host "   1. Use GitHub Desktop (recommended)"
    Write-Host "   2. Set up SSH key: https://docs.github.com/en/authentication/connecting-to-github-with-ssh"
    Write-Host "   3. Use Personal Access Token"
}

# Stage and commit
Write-Host "`n📝 Staging files..." -ForegroundColor Cyan
git add .

# Check for changes
$status = git status --short
if ([string]::IsNullOrWhiteSpace($status)) {
    Write-Host "✅ No changes to commit. Already up to date." -ForegroundColor Green
} else {
    Write-Host "Changes detected:`n$status" -ForegroundColor Yellow
    
    $commitMsg = Read-Host "Enter commit message (or press Enter for default)"
    if ([string]::IsNullOrWhiteSpace($commitMsg)) {
        $commitMsg = "feat: T-LEV-8 deployment update"
    }
    
    git commit -m "$commitMsg"
    Write-Host "✅ Committed: $commitMsg" -ForegroundColor Green
}

# Push
Write-Host "`n📤 Pushing to origin/$Branch..." -ForegroundColor Cyan
git push origin $Branch

if ($LASTEXITCODE -eq 0) {
    Write-Host @"
`n✅ SUCCESS! Deployment complete.
🌐 Site will be live at: https://fthtrading.github.io/T-Lev-8-/
⏰ Wait 2 minutes for GitHub Pages to build.

📥 Next steps:
1. Go to: https://github.com/FTHTrading/T-Lev-8-/settings/pages
2. Under "Build and deployment" → Source: select "GitHub Actions"
3. Click Save
4. Your site will be live in ~2 minutes
"@ -ForegroundColor Green
} else {
    Write-Host @"
`n❌ Push failed. Common causes:
- Not authenticated with GitHub
- No write access to repo
- Network issue

🔧 Fix: Run 'gh auth login' or use GitHub Desktop
"@ -ForegroundColor Red
}

Write-Host "`n🚀 Done!" -ForegroundColor Cyan
