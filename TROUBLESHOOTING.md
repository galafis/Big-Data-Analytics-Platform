# Troubleshooting Guide

## Common Issues and Solutions

### Git Error: "fatal: ambiguous argument 'refs/heads/master': unknown revision or path not in the working tree"

**Problem:** You may encounter this error when running certain Git commands or automated workflows that reference the `master` branch, but this repository uses `main` as the default branch.

**Root Cause:** Modern GitHub repositories use `main` as the default branch name instead of the legacy `master` branch name. Any scripts, workflows, or tools that hardcode references to `master` will fail.

**Solutions:**

#### Option 1: Use Dynamic Branch Detection

Instead of hardcoding branch names, use Git commands to detect the default branch:

```bash
# Get the default branch name dynamically
DEFAULT_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')

# Use it in commands
git diff origin/$DEFAULT_BRANCH HEAD
```

#### Option 2: Update Hardcoded References

If you have control over the workflow or script, update all occurrences:

**Before:**
```yaml
- name: Compare with default branch
  run: git diff refs/heads/master HEAD
```

**After:**
```yaml
- name: Compare with default branch
  run: git diff refs/heads/main HEAD
```

#### Option 3: Set Up Remote HEAD Reference

Ensure your local repository knows about the correct default branch:

```bash
# Update remote HEAD reference
git remote set-head origin -a

# Verify it's set correctly
git symbolic-ref refs/remotes/origin/HEAD
# Should output: refs/remotes/origin/main
```

### Repository Default Branch Information

- **Default Branch:** `main`
- **Branch Strategy:** All development and releases use the `main` branch
- **Protected Branch:** Yes, `main` is protected and requires pull requests

### Workflow Errors

If you're experiencing GitHub Actions workflow errors related to branch references:

1. Check the workflow file in `.github/workflows/`
2. Ensure all branch references use `main` instead of `master`
3. Verify the trigger conditions:
   ```yaml
   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]
   ```

### Testing After Changes

After fixing branch references, always test your changes:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run tests
python3 src/test_data_processor.py

# 3. Run the data processor
python3 src/data_processor.py
```

### Getting Help

If you continue to experience issues:

1. Check the [GitHub Actions logs](https://github.com/galafis/Big-Data-Analytics-Platform/actions) for detailed error messages
2. Review the [CONTRIBUTING.md](CONTRIBUTING.md) guide for development workflow
3. Open an issue on the [repository](https://github.com/galafis/Big-Data-Analytics-Platform/issues) with:
   - Error message
   - Steps to reproduce
   - Your environment details (OS, Python version, etc.)

## Additional Resources

- [GitHub: Renaming the default branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch)
- [Git: Working with branches](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
