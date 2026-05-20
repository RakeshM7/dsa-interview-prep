# Git Learning

A structured, day-by-day Git learning path from absolute beginner to interview-ready.

---

## Learning Path

| Week | Focus | Folder |
|------|-------|--------|
| Week 1 | Core daily commands | [daily-commands/](daily-commands/) |
| Week 2 | Branching and merging workflows | [workflows/](workflows/) |
| Week 3 | Collaboration and conflict resolution | [workflows/](workflows/) |
| Week 4 | Interview preparation | [interview-prep/](interview-prep/) |

---

## Quick Reference

- [Cheatsheets](cheatsheets/) — commands grouped by task
- [Interview Prep](interview-prep/) — common Git interview questions with answers

---

## How to Practice Git Using This Repo

Every time you add a new DSA problem:

```bash
git checkout -b add/two-sum           # create a branch
# ... add your files ...
git add topics/01-arrays-and-hashing/easy/01-two-sum/
git commit -m "feat: add Two Sum solution (Java, Python, JS, TS, Ruby)"
git push origin add/two-sum
# then open a Pull Request on GitHub
```

This gives you real, daily Git practice inside a project you actually care about.
