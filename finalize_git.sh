#!/bin/bash
echo "========================================="
echo "Finalizing Git Setup for ResistanceFinder"
echo "========================================="

# Add all files
echo "Adding files..."
git add .

# Commit
echo "Committing..."
git commit -m "Initial commit: Banana pangenome analysis for TR4 resistance"

# Show commit
echo "Commit created:"
git log --oneline

# Add remote (if not already added)
if ! git remote | grep -q origin; then
    echo "Adding remote origin..."
    git remote add origin https://github.com/Abiodun-Olayinka/ResistanceFinder.git
fi

# Rename branch to main
echo "Renaming branch to main..."
git branch -M main

# Push
echo "Pushing to GitHub..."
git push -u origin main

echo "========================================="
echo "Done! Check your GitHub repository"
echo "========================================="
