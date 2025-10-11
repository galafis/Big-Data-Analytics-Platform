#!/bin/bash

# Branch Helper Script
# This script provides utilities for working with Git branches in this repository

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to get the default branch
get_default_branch() {
    # Try to get from remote HEAD
    default_branch=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@')
    
    # If not set, try to detect from remote
    if [ -z "$default_branch" ]; then
        echo -e "${YELLOW}Remote HEAD not set. Detecting default branch...${NC}" >&2
        git remote set-head origin -a >/dev/null 2>&1
        default_branch=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@')
    fi
    
    # Fallback to 'main' if still not found
    if [ -z "$default_branch" ]; then
        default_branch="main"
        echo -e "${YELLOW}Could not detect default branch. Using 'main' as fallback.${NC}" >&2
    fi
    
    echo "$default_branch"
}

# Function to check if a branch exists
branch_exists() {
    branch=$1
    git rev-parse --verify --quiet "refs/heads/$branch" >/dev/null 2>&1
    return $?
}

# Function to compare current branch with default
compare_with_default() {
    default_branch=$(get_default_branch)
    current_branch=$(git branch --show-current)
    
    echo -e "${GREEN}Comparing $current_branch with $default_branch...${NC}"
    
    if [ "$current_branch" = "$default_branch" ]; then
        echo -e "${YELLOW}You are on the default branch. Showing recent changes:${NC}"
        git --no-pager log --oneline -10
    else
        echo -e "Changes in $current_branch not in $default_branch:"
        git --no-pager log --oneline "origin/$default_branch..$current_branch"
        echo ""
        echo -e "Diff with $default_branch:"
        git --no-pager diff "origin/$default_branch...HEAD" --stat
    fi
}

# Main command handling
case "${1:-help}" in
    get-default)
        get_default_branch
        ;;
    
    exists)
        if [ -z "$2" ]; then
            echo -e "${RED}Error: Please provide a branch name${NC}"
            exit 1
        fi
        if branch_exists "$2"; then
            echo -e "${GREEN}Branch '$2' exists${NC}"
            exit 0
        else
            echo -e "${RED}Branch '$2' does not exist${NC}"
            exit 1
        fi
        ;;
    
    compare)
        compare_with_default
        ;;
    
    info)
        default_branch=$(get_default_branch)
        current_branch=$(git branch --show-current)
        echo -e "${GREEN}Repository Branch Information:${NC}"
        echo -e "  Default branch: ${YELLOW}$default_branch${NC}"
        echo -e "  Current branch: ${YELLOW}$current_branch${NC}"
        echo -e "  Remote: ${YELLOW}$(git remote get-url origin)${NC}"
        ;;
    
    help|*)
        echo "Branch Helper Script"
        echo ""
        echo "Usage: $0 [command]"
        echo ""
        echo "Commands:"
        echo "  get-default    - Print the default branch name"
        echo "  exists <name>  - Check if a branch exists"
        echo "  compare        - Compare current branch with default branch"
        echo "  info           - Show branch information"
        echo "  help           - Show this help message"
        echo ""
        echo "Examples:"
        echo "  $0 get-default"
        echo "  $0 exists feature/new-feature"
        echo "  $0 compare"
        echo "  $0 info"
        ;;
esac
