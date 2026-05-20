# Week 2 — Branching Workflows and Rebasing

---

## Day 8 — Rebase

```bash
# You are on feature/add-login. Main has moved ahead while you worked.
# Instead of a merge commit, you want a clean linear history.

git switch feature/add-login
git rebase main

# What rebase does:
# 1. Temporarily removes your commits from the branch
# 2. Moves the branch to the tip of main
# 3. Replays your commits on top one by one

# Interactive rebase — rewrite last 3 commits
git rebase -i HEAD~3
# In the editor:
#   pick   — keep commit as is
#   reword — keep commit but edit its message
#   squash — combine with previous commit
#   drop   — delete the commit entirely
```

**When to use rebase vs merge:**
- `rebase` — for feature branches before opening a PR (clean history)
- `merge` — for pulling main into a long-lived shared branch (preserves context)
- **Never rebase a branch others are working on**

---

## Day 9 — Cherry-pick

```bash
# Copy a specific commit from another branch into your current branch
git log --oneline feature/other-feature   # find the commit hash
git cherry-pick a3b4c5d                   # apply just that commit here

# Cherry-pick without committing (lets you edit first)
git cherry-pick --no-commit a3b4c5d
```

---

## Day 10 — Tags and releases

```bash
git tag                          # list all tags
git tag v1.0.0                   # lightweight tag
git tag -a v1.0.0 -m "Release 1.0"   # annotated tag (preferred)

git push origin v1.0.0           # push a specific tag
git push origin --tags           # push all tags

git tag -d v1.0.0                # delete local tag
git push origin --delete v1.0.0  # delete remote tag
```

---

## Day 11 — Viewing history

```bash
git log --oneline --graph --all     # visual branch tree
git log --author="Rakesh"           # filter by author
git log --since="2 weeks ago"       # filter by date
git log -- topics/01-arrays-and-hashing/   # history for a specific path

git show a3b4c5d                    # full detail of one commit
git show a3b4c5d --stat             # which files changed

git blame solution.py               # who wrote each line and when
git diff main..feature/add-login    # compare two branches
git diff HEAD~2 HEAD solution.py    # compare a file across commits
```

---

## Day 12 — .gitignore

```bash
# Create a .gitignore file in the repo root
cat > .gitignore << EOF
# Java
*.class
target/

# Python
__pycache__/
*.pyc

# Node
node_modules/

# IDE
.idea/
.vscode/

# OS
.DS_Store
Thumbs.db
EOF

# Check if a file is ignored
git check-ignore -v node_modules/

# Add an already-tracked file to .gitignore
git rm --cached some-file.txt    # stop tracking
echo "some-file.txt" >> .gitignore
git commit -m "chore: stop tracking some-file"
```

---

## Day 13 — Pull requests workflow

```bash
# Standard PR workflow
git switch main && git pull                     # get latest main
git switch -c feat/two-sum-solution             # create feature branch
# ... write your code ...
git add . && git commit -m "feat: add Two Sum (Java, Python)"
git push origin feat/two-sum-solution           # push to GitHub
# → Open a Pull Request on GitHub
# → Get review → merge → delete branch

# After PR is merged, clean up locally
git switch main && git pull
git branch -d feat/two-sum-solution
```

---

## Day 14 — Resolving merge conflicts

```bash
# A conflict happens when two branches changed the same line
git merge feature/other-branch
# CONFLICT (content): Merge conflict in solution.py

# Open the file. You will see:
# <<<<<<< HEAD
# your version
# =======
# their version
# >>>>>>> feature/other-branch

# Edit the file to keep the correct version, remove all markers
# Then:
git add solution.py
git commit -m "merge: resolve conflict in solution.py"

# Abort a merge if you are unsure
git merge --abort
```
