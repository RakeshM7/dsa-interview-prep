---
name: dsa-problem-folder
description: >-
  Scaffolds a new DSA problem folder under topics/ in dsa-interview-prep from a
  problem title (e.g. "Valid Parentheses", "Longest Substring Without Repeating
  Characters"). Creates problem.md, notes.md, solution.rb stub, and empty
  solution.py/js/ts/Solution.java. Use when the user asks to add a new problem,
  create a problem folder, or gives only a LeetCode-style problem name.
---

# DSA Problem Folder

Create a new problem directory in `dsa-interview-prep` matching `topics/01-arrays-and-hashing/easy/02-contains-duplicates/`.

## Input (required)

**Problem statement title** — exact or informal name, e.g.:

- `Valid Parentheses`
- `Longest Substring Without Repeating Characters`
- `two sum` (normalize to title case in files)

Do not start until you have this title. If the user only says "create a problem folder", ask for the title.

## Repo layout

```
topics/{NN-topic-slug}/{difficulty}/{NN-problem-slug}/
  problem.md
  notes.md
  solution.rb       # header + TODO + driver tests (no full solution unless asked)
  solution.py       # empty
  solution.js       # empty
  solution.ts       # empty
  Solution.java     # empty
```

Topic roots (from repo `README.md`):

| NN | Slug |
|----|------|
| 01 | `01-arrays-and-hashing` |
| 02 | `02-two-pointers` |
| 03 | `03-sliding-window` |
| 04 | `04-binary-search` |
| 05 | `05-linked-lists` |
| 06 | `06-stacks-and-queues` |
| 07 | `07-trees-and-graphs` |
| 08 | `08-dynamic-programming` |
| 09 | `09-recursion-and-backtracking` |
| 10 | `10-sorting-and-searching` |

Difficulty: `easy` | `medium` | `hard` (use LeetCode difficulty when known).

## Workflow

Copy and track:

```
- [ ] 1. Resolve metadata from title
- [ ] 2. Pick topic + difficulty + next folder number
- [ ] 3. Create topic README if missing
- [ ] 4. Write all 8 files under problem folder
- [ ] 5. Update topic README problem table
- [ ] 6. Report path to user
```

### Step 1 — Resolve metadata

From the title, determine:

- **Display title** — title case for `#` headings
- **LeetCode #** and **URL slug** — if recognized (e.g. Valid Parentheses → #20, `valid-parentheses`)
- **Difficulty** — Easy / Medium / Hard
- **Topic folder** — pattern that best fits (stack → 06, sliding window → 03, hash/array → 01, etc.)
- **Problem statement, examples, constraints, hint** — accurate LeetCode-style content in `problem.md`
- **Notes content** — brute force + optimal, complexity table, interview Qs, traps, related problems (see [templates.md](templates.md))

If topic or difficulty is ambiguous, pick the best fit and state your choice in the final message.

### Step 2 — Folder name and path

**Problem slug:** lowercase, hyphens, no filler words unless needed for clarity.

- `Longest Substring Without Repeating Characters` → `longest-substring-without-repeating-characters`

**Number prefix:** scan existing folders under `topics/{topic}/{difficulty}/`:

```bash
ls topics/03-sliding-window/medium/
# → 01-longest-substring-...  → next is 02
```

Folder name: `{NN}-{problem-slug}` (e.g. `02-minimum-window-substring`).

Full path example:

`topics/03-sliding-window/medium/02-minimum-window-substring/`

### Step 3 — Topic README

If `topics/{NN-topic-slug}/README.md` is missing, create it using the topic README pattern in [templates.md](templates.md) (core pattern, key concepts table, empty Easy/Medium/Hard tables).

### Step 4 — Files

Use templates in [templates.md](templates.md). Rules:

- **problem.md** — same sections as `02-contains-duplicates/problem.md`; footer `Where this file lives` lists all 7 files
- **notes.md** — substantive interview prep (not placeholder bullets)
- **solution.rb** — LeetCode header comment, one class, one `TODO` method, driver `puts` from **Examples** in problem.md
- **solution.py / .js / .ts / Solution.java** — completely empty (no code, no comments)

Ruby class naming: `{Topic}Processor` or `{Problem}Processor` (e.g. `StackProcessor`, `SlidingWindowProcessor`).

### Step 5 — Update topic README

Add a row under the correct difficulty table:

```markdown
| NN | [Display Title]({difficulty}/{NN-problem-slug}/problem.md) | One-line key insight |
```

Use the same `NN` as the folder prefix. Do not duplicate an existing problem link.

### Step 6 — Report

Tell the user:

- Full folder path
- Topic, difficulty, LeetCode link (if any)
- Files created
- Reminder to implement `solution.rb` and fill other languages later

## Do not

- Add `README.md` inside the problem folder (use `problem.md` only)
- Put implementation code in `.py` / `.js` / `.ts` / `.java` unless the user explicitly asks
- Commit unless the user asks
- Reuse another problem’s `problem.md` text for a different title

## Examples

**Input:** `Valid Parentheses`

**Output path:** `topics/06-stacks-and-queues/easy/02-valid-parentheses/` (if `01-valid-parentheses` already exists)

**Input:** `Longest Substring Without Repeating Characters`

**Output path:** `topics/03-sliding-window/medium/01-longest-substring-without-repeating-characters/`

## Templates

File bodies and topic README skeleton: [templates.md](templates.md)
