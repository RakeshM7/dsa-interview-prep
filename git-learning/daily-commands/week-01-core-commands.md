# Week 1 — Core Git Commands

Practice these every day. By end of week 1 you should run them without thinking.

---

## Day 1 — Setup and your first commit

```bash
git config --global user.name "Rakesh Manoharan"
git config --global user.email "akashmrakesh@gmail.com"

git init my-project
cd my-project
git status

echo "# My Project" > README.md
git add README.md
git commit -m "docs: add README"
git log --oneline
```

**Learned:** init → status → add → commit → log

---

## Day 2 — Staging area deep dive

```bash
echo "hello" > file1.txt && echo "world" > file2.txt

git add file1.txt       # stage only one file
git status

git add .               # stage everything
git restore --staged file2.txt   # unstage (keeps changes)
git restore file2.txt   # discard changes entirely (irreversible)

git diff                # unstaged changes
git diff --staged       # staged changes (what goes into next commit)
```

**Learned:** The three zones — working directory, staging area, commit history

---

## Day 3 — Branching

```bash
git branch                          # list branches
git switch -c feature/add-login     # create and switch (preferred modern way)
git checkout -b feature/add-login   # older equivalent, still widely used

echo "login" > login.txt
git add login.txt && git commit -m "feat: add login"

git switch main      # switch back — login.txt disappears (it's on the other branch)
git branch           # star marks current branch
```

**Learned:** Branches are isolated. Always work on a branch, never directly on main.

---

## Day 4 — Merging

```bash
git switch main
git merge feature/add-login        # merge feature into main

git log --oneline --graph --all    # see visual branch history

git branch -d feature/add-login   # delete after merging (safe)
git branch -D feature/add-login   # force delete unmerged branch
```

**Merge types:**
- **Fast-forward** — linear, no merge commit, main had no new commits while you worked
- **Three-way merge** — creates a merge commit, both branches had commits

---

## Day 5 — Remote repositories

```bash
git remote add origin https://github.com/YOUR_USERNAME/dsa-interview-prep.git
git remote -v                          # verify

git push -u origin main                # first push, sets upstream
git push                               # subsequent pushes

git fetch origin                       # download changes, do NOT merge
git pull                               # fetch + merge in one step

git push origin feature/add-login     # push a branch to GitHub
git push origin --delete feature/add-login   # delete remote branch
```

---

## Day 6 — Undoing things

```bash
git reset --soft HEAD~1    # undo last commit, keep changes staged
git reset HEAD~1           # undo last commit, unstage changes (keep files)
git reset --hard HEAD~1    # undo last commit, discard changes (DESTRUCTIVE)

git revert HEAD            # create a new commit that reverses the last one (safe for shared branches)

git commit --amend -m "fixed message"    # fix last commit message
git add forgotten.txt && git commit --amend --no-edit  # add forgotten file to last commit
```

**Rule:** Use `revert` on shared branches. Use `reset` only on your own local commits.

---

## Day 7 — Stashing

```bash
git stash                  # save uncommitted work temporarily
git stash list             # see all stashes
git stash pop              # restore latest stash and remove it
git stash apply            # restore latest stash but keep it in list
git stash push -m "half-done two-sum"   # stash with a label
git stash drop stash@{0}  # delete a specific stash
git stash clear            # delete all stashes
```
