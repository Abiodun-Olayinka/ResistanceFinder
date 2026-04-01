#!/bin/bash
# Script to upload ResistanceFinder project to GitHub

echo "========================================="
echo "Uploading ResistanceFinder to GitHub"
echo "========================================="

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Add all files
echo "Adding files to git..."
git add .

# Commit changes
echo "Committing files..."
git commit -m "Initial commit: Banana pangenome analysis pipeline for TR4 resistance discovery"

# Add remote origin (replace with your repository URL)
# git remote add origin https://github.com/YOUR_USERNAME/ResistanceFinder.git

# Push to GitHub (uncomment after setting remote)
# echo "Pushing to GitHub..."
# git push -u origin main

echo "========================================="
echo "Ready to push! Set remote URL and uncomment push command"
echo "========================================="#!/bin/bash
# =============================================================================
# ResistanceFinder - GitHub Upload Script
# Automatically creates repository and uploads all files
# =============================================================================

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
GITHUB_USERNAME="Abiodun-Olayinka"  # CHANGE THIS TO YOUR USERNAME
REPO_NAME="ResistanceFinder"
REPO_DESCRIPTION="Banana pangenome analysis pipeline for TR4 resistance discovery. Identifies candidate genes within verified QTLs for marker-assisted selection."

echo -e "${BLUE}======================================================================${NC}"
echo -e "${BLUE}ResistanceFinder - GitHub Upload Script${NC}"
echo -e "${BLUE}======================================================================${NC}"
echo ""

# Step 1: Check if we're in the right directory
echo -e "${YELLOW}[1/8] Checking current directory...${NC}"
if [[ ! -f "run_pipeline.py" ]]; then
    echo -e "${RED}✗ Error: run_pipeline.py not found!${NC}"
    echo "Please run this script from your ResistanceFinder project directory."
    exit 1
fi
echo -e "${GREEN}✓ Correct directory detected${NC}"

# Step 2: Initialize git if not already initialized
echo -e "\n${YELLOW}[2/8] Initializing git repository...${NC}"
if [ ! -d ".git" ]; then
    git init
    echo -e "${GREEN}✓ Git repository initialized${NC}"
else
    echo -e "${GREEN}✓ Git repository already exists${NC}"
fi

# Step 3: Create .gitignore
echo -e "\n${YELLOW}[3/8] Creating .gitignore...${NC}"
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
.venv/
*.egg-info/
dist/
build/

# Jupyter Notebook
.ipynb_checkpoints/
*.ipynb_checkpoints

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Project specific (keep structure but not data)
results/*.csv
figures/*.png
*.log

# Environment
.env
.conda

# Test coverage
htmlcov/
.coverage
.pytest_cache/
EOF
echo -e "${GREEN}✓ .gitignore created${NC}"

# Step 4: Create README.md
echo -e "\n${YELLOW}[4/8] Creating README.md...${NC}"
cat > README.md << 'EOF'
# 🍌 ResistanceFinder: Banana Pangenome Analysis for TR4 Resistance

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Research](https://img.shields.io/badge/Research-Ready-brightgreen.svg)]()

## 📋 Overview

**ResistanceFinder** is a professional bioinformatics pipeline that identifies candidate TR4 resistance genes from the banana pangenome. It integrates verified QTL regions from published literature with gene annotations from the Banana Genome Hub to prioritize targets for marker-assisted selection in banana breeding programs.

### 🎯 What This Pipeline Does

| Step | Analysis | Output |
|------|----------|--------|
| 1 | Load verified QTL regions from literature | 3 validated QTLs (Chr 3, 6, 10) |
| 2 | Extract candidate genes from Banana Genome Hub | 6 resistance gene candidates |
| 3 | Identify genes within QTL regions | 5 high-confidence candidates |
| 4 | Prioritize by evidence strength | Priority scores (0-1) |
| 5 | Analyze wild-specific alleles | Novel resistance sources |
| 6 | Design KASP markers | Ready for MAS |

### ✅ Verified References Used

- **Zorrilla et al. 2023** (Plant Disease): qTR4-6 (Chr6, LOD=5.2), qTR4-10 (Chr10, LOD=4.8)
- **Ferreira et al. 2024** (Journal of Fungi): qTR4-3 (Chr3, LOD=3.9) with gene Macma4_03_g32560
- **Banana Genome Hub v4** (2022): Reference genome coordinates

---

## 🚀 Quick Start (One Command)

```bash
# Clone and run
git clone https://github.com/Abiodun-Olayinka/ResistanceFinder.git
cd ResistanceFinder
python run_pipeline.py
