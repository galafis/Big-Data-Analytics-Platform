# Quick Reference: Git Branch Fix

## 🔧 The Problem
When running repository audits or certain workflows, you may see:
```
fatal: ambiguous argument 'refs/heads/master': unknown revision or path not in the working tree
```

## ✅ The Solution

### This repository uses `main` as the default branch, NOT `master`

### Quick Fixes

#### Option 1: Use the Helper Script (Recommended)
```bash
# Get default branch name
./scripts/branch-helper.sh get-default

# Show repository info
./scripts/branch-helper.sh info

# Check if a branch exists
./scripts/branch-helper.sh exists main
```

#### Option 2: Dynamic Branch Detection
```bash
# Detect default branch dynamically
DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')

# Use in commands
git diff origin/$DEFAULT_BRANCH HEAD
```

#### Option 3: Update Hardcoded References
Replace all `refs/heads/master` with `refs/heads/main` in your scripts/workflows

## 📚 Full Documentation
- **Complete Guide:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Contributing Guide:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Main Documentation:** [README.md](README.md)

## 🛠️ Helper Script Commands

```bash
./scripts/branch-helper.sh get-default    # Print default branch
./scripts/branch-helper.sh exists <name>  # Check if branch exists
./scripts/branch-helper.sh compare        # Compare with default branch
./scripts/branch-helper.sh info           # Show branch information
./scripts/branch-helper.sh help           # Show help message
```

## 🎯 Branch Structure

- **Default Branch:** `main`
- **Feature Branches:** `feature/your-feature-name`
- **Bugfix Branches:** `bugfix/your-bug-description`
- **Protected:** Yes, `main` requires pull requests

## 📝 For Contributors

When creating a new branch:
```bash
# Always start from main
git checkout main
git pull origin main

# Create your feature branch
git checkout -b feature/your-feature-name

# When ready, open PR to main (NOT master)
```

## 🔗 Useful Links

- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Complete troubleshooting guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [GitHub: Renaming branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch)
