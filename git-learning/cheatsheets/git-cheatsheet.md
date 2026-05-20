# Git Cheatsheet — Commands by Task

## Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
git config --global core.editor "code --wait"  # use VS Code as editor
git config --list                               # view all config
```

## Start a repo
```bash
git init                        # new local repo
git clone <url>                 # copy an existing repo
git clone <url> my-folder       # clone into a specific folder
```

## Daily cycle
```bash
git status                      # what changed?
git add <file>                  # stage a file
git add .                       # stage everything
git diff                        # unstaged changes
git diff --staged               # staged changes
git commit -m "message"         # commit
git push                        # send to remote
git pull                        # get latest from remote
```

## Branches
```bash
git branch                      # list local branches
git branch -a                   # list all (including remote)
git switch -c <name>            # create and switch
git switch <name>               # switch to existing
git branch -d <name>            # delete (safe)
git branch -D <name>            # force delete
git push origin <name>          # push branch to remote
git push origin --delete <name> # delete remote branch
```

## Merging and rebasing
```bash
git merge <branch>              # merge branch into current
git merge --abort               # cancel a merge
git rebase <branch>             # rebase current on top of branch
git rebase -i HEAD~3            # interactive rebase, last 3 commits
git rebase --abort              # cancel a rebase
git cherry-pick <hash>          # copy one commit to current branch
```

## Undoing
```bash
git restore <file>              # discard working directory changes
git restore --staged <file>     # unstage
git reset --soft HEAD~1         # undo commit, keep staged
git reset HEAD~1                # undo commit, unstage
git reset --hard HEAD~1         # undo commit, discard changes
git revert <hash>               # reverse a commit (safe for shared branches)
git commit --amend -m "msg"     # fix last commit message
```

## Stashing
```bash
git stash                       # save uncommitted work
git stash list                  # see all stashes
git stash pop                   # restore and remove latest
git stash apply stash@{0}       # restore without removing
git stash drop stash@{0}        # delete a stash
git stash clear                 # delete all stashes
```

## Remote
```bash
git remote -v                   # list remotes
git remote add origin <url>     # add remote
git fetch origin                # download, do not merge
git pull origin main            # download and merge
git push -u origin main         # push and set upstream
git push --force-with-lease     # safe force push
```

## History and inspection
```bash
git log --oneline               # compact history
git log --oneline --graph --all # visual branch tree
git log --author="Name"         # filter by author
git log -- <path>               # history of a file
git show <hash>                 # detail of one commit
git blame <file>                # who wrote each line
git diff main..feature          # compare two branches
git reflog                      # full HEAD movement history (recovery tool)
```

## Tagging
```bash
git tag                         # list tags
git tag -a v1.0.0 -m "Release"  # annotated tag
git push origin --tags          # push all tags
git push origin --delete v1.0.0 # delete remote tag
```

## Useful one-liners
```bash
git log --oneline -10                     # last 10 commits
git diff HEAD~1 HEAD -- solution.py       # what changed in a file last commit
git grep "HashMap" -- "*.java"           # search code in tracked files
git shortlog -s -n                        # commit count by author
git stash show -p stash@{0}              # see contents of a stash
```
