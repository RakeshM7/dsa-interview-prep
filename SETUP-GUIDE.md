# Complete Setup Guide — DSA Interview Prep Project

A step-by-step guide to creating and maintaining this project yourself.
Covers folder structure, README writing, language choice, and daily Git practice.

---

## Part 1 — Create the Project on Your Machine

### Step 1: Install the prerequisites

**Git**
```bash
# macOS
brew install git

# Ubuntu / WSL
sudo apt update && sudo apt install git

# Verify
git --version
```

**Java (JDK 17)**
- Download from: https://adoptium.net/
- Or: `brew install openjdk@17`
- Verify: `java --version && javac --version`

**Python 3**
- Download from: https://www.python.org/downloads/
- Or: `brew install python3`
- Verify: `python3 --version`

**Node.js (for JS and TS)**
- Download from: https://nodejs.org/ (LTS version)
- Verify: `node --version && npm --version`

**TypeScript**
```bash
npm install -g typescript
tsc --version
```

**Ruby**
- macOS: pre-installed or `brew install ruby`
- Ubuntu: `sudo apt install ruby`
- Verify: `ruby --version`

---

### Step 2: Create the folder structure manually

```bash
mkdir dsa-interview-prep
cd dsa-interview-prep
git init

mkdir -p topics/{01-arrays-and-hashing,02-two-pointers,03-sliding-window,\
04-binary-search,05-linked-lists,06-stacks-and-queues,\
07-trees-and-graphs,08-dynamic-programming,\
09-recursion-and-backtracking,10-sorting-and-searching}/{easy,medium,hard}

mkdir -p git-learning/{daily-commands,workflows,interview-prep,cheatsheets}
mkdir -p docs
mkdir -p shared/{java,python,javascript,ruby}
```

---

### Step 3: Create your first problem folder

```bash
mkdir -p topics/01-arrays-and-hashing/easy/01-two-sum
cd topics/01-arrays-and-hashing/easy/01-two-sum
touch problem.md Solution.java solution.py solution.js solution.ts solution.rb notes.md
```

---

## Part 2 — Folder Structure Best Practices

### The Pattern (copy this for every problem)

```
topics/
  01-arrays-and-hashing/
    README.md              ← Pattern explanation + problem list for this topic
    easy/
      01-two-sum/
        problem.md         ← Problem statement, constraints, examples
        Solution.java      ← Java: brute force + optimal, with main()
        solution.py        ← Python: brute force + optimal, with if __name__
        solution.js        ← JavaScript: brute force + optimal, with console.log
        solution.ts        ← TypeScript: same as JS with types
        solution.rb        ← Ruby: brute force + optimal, with p statements
        notes.md           ← Complexity, interview Qs, traps, related problems
```

### Naming conventions

| Item | Convention | Example |
|------|-----------|---------|
| Topic folders | number + kebab-case | `01-arrays-and-hashing` |
| Problem folders | number + kebab-case | `01-two-sum` |
| Java file | PascalCase | `Solution.java` |
| Python file | snake_case | `solution.py` |
| JavaScript file | snake_case | `solution.js` |
| TypeScript file | snake_case | `solution.ts` |
| Ruby file | snake_case | `solution.rb` |
| Markdown files | UPPER or kebab | `README.md`, `notes.md` |

### Why number the folders?

Numbered folders (`01-`, `02-`) sort correctly in every file browser and terminal.
Without numbers, `arrays-and-hashing` would appear before `binary-search` alphabetically — fine.
But `trees-and-graphs` would appear after `two-pointers` which breaks the learning progression.
Numbers make the intended order explicit.

---

## Part 3 — How to Write README Files

### Rule 1: Every README answers one question

| Level | README answers |
|-------|---------------|
| Root `README.md` | What is this repo and how do I navigate it? |
| Topic `README.md` | What is this pattern, when do I use it, what problems are here? |
| Problem `notes.md` | How does this solution work and what will the interviewer ask? |

### Rule 2: README structure for the root

```markdown
# Project Name

One sentence describing what this repo is.

## Topics table with links and status
## How to run solutions
## How to contribute
## Progress tracker link
```

### Rule 3: README structure for a topic

```markdown
# Topic Name

## Core Pattern — when to use this, key insight

## Key Complexity Table

## Problems — linked list with key insight per problem
  ### Easy
  ### Medium
  ### Hard

## Common Interview Follow-ups
```

### Rule 4: notes.md structure for a problem

```markdown
# Problem Name — Notes

## Approaches — brute force first, then optimal
## Complexity Summary table
## Interview Discussion Points — Q&A format
## Traps to Avoid
## Related Problems
```

### Rule 5: Commit message format

Follow the Conventional Commits standard. Every team uses a version of this:

```
feat: add Two Sum solution (Java, Python, JS, TS, Ruby)
fix: correct off-by-one in sliding window solution
docs: add notes for Group Anagrams
refactor: simplify Two Sum with early return
chore: update .gitignore for Ruby
```

Format: `type: short description` (no period, lowercase, imperative mood)

Types: `feat` | `fix` | `docs` | `refactor` | `test` | `chore`

---

## Part 4 — Which Language to Use for Which Problems

### The honest answer for a beginner

You do not need to solve everything in all 5 languages from day one.
Pick one primary language per problem and add others when you are comfortable.

### Recommended primary language by role

| If you are targeting... | Primary language to use |
|------------------------|------------------------|
| SDET / QA Automation | Python or JavaScript |
| SWE (general) | Java or Python |
| Frontend SWE | JavaScript or TypeScript |
| Full-stack SWE | Python or TypeScript |

### Language strengths for DSA

**Python** — best for beginners and interviews
- Shortest code, most readable
- Built-in `collections.defaultdict`, `Counter`, `heapq`, `deque`
- Use when: you want to think about the algorithm, not the syntax
- Watch out for: no static types (can cause confusion in complex problems)

**Java** — best for SDET and enterprise roles
- Verbose but explicit (good for learning what you are actually doing)
- `HashMap`, `HashSet`, `ArrayDeque`, `PriorityQueue` are your main tools
- Use when: the job description mentions Java, or you need strict type safety
- Watch out for: boilerplate, checked exceptions, `Integer` vs `int`

**JavaScript** — best for full-stack and frontend roles
- `Map` and `Set` are first-class
- Short, flexible syntax
- Use when: targeting frontend or full-stack roles, or you already know JS
- Watch out for: `===` vs `==`, loose typing causing silent bugs

**TypeScript** — Java-like safety with JS flexibility
- Best when you already know JavaScript
- Adds type annotations which catch bugs early
- Use when: targeting modern frontend/backend roles that list TypeScript in the JD
- Watch out for: need to compile (`tsc`) before running

**Ruby** — only relevant if targeting Selenium + Ruby SDET roles
- Extremely readable, great for RSpec-style test logic
- Limited DSA interview usage except in Ruby-focused SDET roles
- Use when: practising for Freshworks-style SDET interviews or Ruby codebases

### Practical plan for this repo

```
Start:     Solve every problem in Python (fastest to learn, most readable)
Month 2:   Add Java solutions (important for SDET interview rounds)
Month 3:   Add JavaScript solutions (useful for full-stack roles)
Month 4+:  Add TypeScript and Ruby (completes the portfolio)
```

---

## Part 5 — Daily Workflow

### The routine (15–30 minutes per day)

```bash
# Morning — before you start
git switch main && git pull         # get latest

# Create a branch for today's problem
git switch -c feat/two-sum-python

# Write your solution, run it, verify output
python3 solution.py

# Commit your work
git add topics/01-arrays-and-hashing/easy/01-two-sum/solution.py
git commit -m "feat: add Two Sum Python solution"

# Push and open a PR (even if it's just your own repo — practice the workflow)
git push origin feat/two-sum-python
```

### When you add a new problem

```bash
# 1. Read the problem statement
# 2. Try brute force first without looking at the solution
# 3. Code it, verify it works
# 4. Think: what is the bottleneck? Can I eliminate a loop?
# 5. Code the optimal solution
# 6. Write notes.md with complexity and interview Qs
# 7. Add to PROGRESS.md
# 8. Commit and push
```

### Update PROGRESS.md after every problem

```markdown
| 001 | Two Sum | Arrays & Hashing | Easy | ✅ Done | 2025-06-01 | HashMap O(n) |
| 002 | Contains Duplicate | Arrays & Hashing | Easy | ✅ Done | 2025-06-02 | HashSet |
```

---

## Part 6 — Push to GitHub

### Step 1: Create a repo on GitHub
- Go to github.com → New repository
- Name: `dsa-interview-prep`
- Public (so others can reference it)
- Do NOT initialise with README (you already have one)

### Step 2: Connect and push
```bash
cd dsa-interview-prep
git remote add origin https://github.com/YOUR_USERNAME/dsa-interview-prep.git
git push -u origin main
```

### Step 3: Enable GitHub Actions
The `.github/workflows/ci.yml` file is already in this repo.
Every push will automatically run your Python and Java solutions and show a green check or red cross.

---

## Part 7 — Keeping the Repo Clean

### Branch naming convention
```
feat/two-sum-python
feat/contains-duplicate-java
fix/sliding-window-off-by-one
docs/update-arrays-readme
```

### Commit message convention
```
feat: add Two Sum (Python)
feat: add Two Sum optimal solution (Java, hashmap approach)
docs: add complexity notes for Two Sum
fix: correct index return in Two Sum brute force
```

### Never commit these
```
*.class       # Java compiled files
__pycache__/  # Python cache
node_modules/ # Node dependencies
.DS_Store     # macOS metadata
.idea/        # IDE config
```
