# Git Interview Questions — With Answers

These are the actual questions asked in SDET and SWE interviews. Study both the answer AND the explanation.

---

## Fundamentals

**Q1. What is the difference between `git fetch` and `git pull`?**

`git fetch` downloads changes from the remote but does NOT modify your working directory or current branch. It updates your remote-tracking branches (e.g. `origin/main`).

`git pull` is `git fetch` followed by `git merge`. It downloads changes and immediately merges them into your current branch.

**When to use fetch:** When you want to inspect what changed remotely before integrating it.
**When to use pull:** When you trust the changes and want to update immediately.

---

**Q2. What is the difference between `git merge` and `git rebase`?**

Both integrate changes from one branch into another, but they do it differently.

`git merge` creates a new merge commit that joins the two branch histories. The original commits are preserved as-is. Good for shared branches because it does not rewrite history.

`git rebase` moves your commits to the tip of another branch by replaying them one by one. Creates a linear history with no merge commits. Good for cleaning up feature branches before a PR.

**Key rule:** Never rebase a branch that other people are working on. It rewrites commit hashes and causes chaos.

---

**Q3. What is the difference between `git reset` and `git revert`?**

`git reset` moves the HEAD pointer backwards, effectively removing commits from history. It can modify the staging area and working directory depending on the flag (soft / mixed / hard).

`git revert` creates a new commit that is the inverse of the target commit. The original commit stays in history.

**Use `reset`** for local commits that have not been shared.
**Use `revert`** for commits on shared branches. It is safe because it does not rewrite history.

---

**Q4. What does `git stash` do?**

It temporarily saves your uncommitted changes (both staged and unstaged) and reverts your working directory to the last commit. This lets you switch branches without committing unfinished work.

`git stash pop` restores the changes and removes the stash entry.
`git stash apply` restores but keeps the stash entry (useful if you want to apply the same changes on multiple branches).

---

**Q5. What is a detached HEAD state?**

Normally, HEAD points to a branch, which points to a commit. In detached HEAD state, HEAD points directly to a commit instead of a branch.

This happens when you run `git checkout <commit-hash>` or `git checkout <tag>`.

In this state, any commits you make are not attached to any branch and can be lost when you switch branches. To preserve work done in detached HEAD state:
```bash
git switch -c new-branch-name
```

---

**Q6. What is the difference between `--soft`, `--mixed`, and `--hard` in `git reset`?**

All three move HEAD to the specified commit. The difference is what happens to your changes:

| Flag | Staging area | Working directory |
|------|-------------|-------------------|
| `--soft` | Keeps staged changes | Unchanged |
| `--mixed` (default) | Unstages changes | Unchanged |
| `--hard` | Clears staging area | Discards all changes |

**Remember:** `--hard` is the only one that can cause you to lose work permanently.

---

**Q7. What is `git cherry-pick`?**

It applies a specific commit from one branch to your current branch. Useful when you want one specific fix from a branch without merging the entire branch.

```bash
git cherry-pick a3b4c5d
```

The resulting commit has a new hash but the same changes as the original.

---

**Q8. What is `git bisect`?**

A tool for finding which commit introduced a bug using binary search. You mark a known good commit and a known bad commit, and Git automatically checks out commits in the middle for you to test.

```bash
git bisect start
git bisect bad HEAD           # current commit is bad
git bisect good v2.0          # v2.0 was good
# Git checks out the midpoint — test it
git bisect good               # or: git bisect bad
# Git narrows down — repeat until the culprit commit is found
git bisect reset              # return to original HEAD
```

---

**Q9. How would you undo a commit that has already been pushed to a shared branch?**

Use `git revert`, not `git reset`. Revert creates a new commit that undoes the changes, preserving the original commit in history. This is safe for shared branches.

```bash
git revert a3b4c5d
git push
```

Never use `git reset` to undo pushed commits on shared branches — it rewrites history and forces collaborators to re-sync.

---

**Q10. What is `git reflog` and when is it useful?**

`git reflog` records every movement of HEAD, even resets and deleted branches. It is Git's safety net.

If you accidentally ran `git reset --hard` and lost commits, `git reflog` shows those lost commit hashes and you can recover them:

```bash
git reflog                    # find the commit hash before the reset
git reset --hard a3b4c5d      # go back to it
```

---

**Q11. What is the difference between a fast-forward merge and a three-way merge?**

**Fast-forward:** The target branch (main) has not moved since the feature branch was created. Git simply moves the main pointer forward to the feature branch tip. No merge commit is created. Results in linear history.

**Three-way merge:** Both branches have new commits. Git finds the common ancestor commit, then combines changes from both branches into a new merge commit.

---

**Q12. What is `git rebase -i` used for?**

Interactive rebase. It lets you rewrite your local commit history before pushing or opening a PR. Common uses:

- **squash** — combine multiple small commits into one meaningful commit
- **reword** — fix a commit message
- **drop** — delete a commit entirely
- **reorder** — change the order of commits

```bash
git rebase -i HEAD~4    # interactively edit the last 4 commits
```

---

## Scenario Questions

**Q: You committed sensitive data (a password) to a public repo. What do you do?**

1. Immediately invalidate the credential at the source (rotate the API key, change the password)
2. Remove the file from history: `git filter-branch` or `git filter-repo`
3. Force push: `git push --force`
4. Notify your team

Note: Rotating the credential is step 1 because the secret is already exposed. Removing it from Git history is step 2 but does not undo the exposure.

---

**Q: Your feature branch is 20 commits behind main. How do you sync it?**

```bash
git switch feature/my-branch
git rebase main
# resolve any conflicts, then:
git push --force-with-lease origin feature/my-branch
```

`--force-with-lease` is safer than `--force` — it only force-pushes if no one else has pushed to the remote branch since your last fetch.

---

**Q: You need to work on an urgent hotfix but your feature branch is half done. What do you do?**

```bash
git stash push -m "half-done feature work"
git switch main && git pull
git switch -c hotfix/login-crash
# ... fix the bug ...
git commit -m "fix: prevent crash on empty login"
git push origin hotfix/login-crash
# open PR, get merged

git switch feature/my-branch
git stash pop
```
