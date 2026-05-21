#!/bin/bash
set -e

echo "🚀 T-LEV-8 Automated Deployment Script"
echo "========================================="

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

REPO_URL="${1:-https://github.com/FTHTrading/T-Lev-8-.git}"
BRANCH="${2:-main}"

# Check dependencies
check_dep() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${RED}❌ $1 not found. Install it first.${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ $1 detected${NC}"
}

check_dep git
check_dep curl

# Get repo name
REPO_NAME=$(basename "$REPO_URL" .git)

# Clone or pull
if [ -d "$REPO_NAME/.git" ]; then
    echo -e "${YELLOW}📂 Repo exists. Pulling latest...${NC}"
    cd "$REPO_NAME"
    git pull origin "$BRANCH"
else
    echo -e "${YELLOW}📥 Cloning repository...${NC}"
    git clone "$REPO_URL"
    cd "$REPO_NAME"
fi

# Verify git repo
if [ ! -d ".git" ]; then
    echo -e "${RED}❌ Not a git repository. Exiting.${NC}"
    exit 1
fi

# Test remote access
echo -e "${CYAN}🔍 Verifying remote access...${NC}"
if ! git ls-remote --heads origin &> /dev/null; then
    echo -e "${YELLOW}⚠️ Cannot access remote. You may need to authenticate.${NC}"
    echo "Options:"
    echo "  1. Use SSH: git@github.com:FTHTrading/T-Lev-8-.git"
    echo "  2. Set up Personal Access Token"
    echo "  3. Use GitHub CLI: gh auth login"
fi

# Stage and commit
echo ""
echo -e "${CYAN}📝 Staging files...${NC}"
git add .

if git diff --cached --quiet; then
    echo -e "${GREEN}✅ No changes to commit. Already up to date.${NC}"
else
    echo -e "${YELLOW}Changes detected:${NC}"
    git status --short
    
    read -p "Enter commit message (or Enter for default): " msg
    COMMIT_MSG="${msg:-feat: T-LEV-8 deployment update}"
    
    git commit -m "$COMMIT_MSG"
    echo -e "${GREEN}✅ Committed: $COMMIT_MSG${NC}"
fi

# Push
echo ""
echo -e "${CYAN}📤 Pushing to origin/$BRANCH...${NC}"
if git push origin "$BRANCH"; then
    echo ""
    echo -e "${GREEN}✅ SUCCESS! Deployment complete.${NC}"
    echo -e "${GREEN}🌐 Site will be live at: https://fthtrading.github.io/T-Lev-8-/${NC}"
    echo -e "${YELLOW}⏰ Wait 2 minutes for GitHub Pages to build.${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Go to: https://github.com/FTHTrading/T-Lev-8-/settings/pages"
    echo "2. Under 'Build and deployment' → Source: select 'GitHub Actions'"
    echo "3. Click Save"
    echo "4. Your site will be live in ~2 minutes"
else
    echo ""
    echo -e "${RED}❌ Push failed.${NC}"
    echo "Common causes:"
    echo "  - Not authenticated with GitHub"
    echo "  - No write access to repo"
    echo "  - Network issue"
fi

echo ""
echo -e "${CYAN}🚀 Done!${NC}"
