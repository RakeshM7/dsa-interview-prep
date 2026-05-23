# DSA Problem Folder — Templates

## problem.md

```markdown
# {Display Title}

**Difficulty:** {Easy|Medium|Hard}
**Topic:** {Short topic label, e.g. Stacks, Sliding Window}
**Language:** Ruby
**LeetCode:** [#{N}](https://leetcode.com/problems/{slug}/)
**Interview Frequency:** {Very High | High | Medium}

---

## Problem Statement

{Official-style statement}

---

## Examples

```
Input:  ...
Output: ...
```

(Add 3–5 examples; include edge cases: empty input, single element, tricky case.)

---

## Constraints

- {bullet list}

---

## Hint

{One paragraph — optimal pattern nudge, no full solution}

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```
topics/{topic-slug}/{difficulty}/{folder-name}/
  problem.md        ← you are here
  solution.rb       ← {brief approach label}
  solution.py
  solution.js
  solution.ts
  Solution.java
  notes.md          ← complexity, interview Qs, traps
```
```

If not a LeetCode problem, omit the **LeetCode** line and use **Interview Frequency** only.

---

## notes.md

```markdown
# {Display Title} — Notes

## Approaches

### Brute Force
{description}
- Time: ...
- Space: ...
- When to mention: Always mention brute force first in interviews before jumping to the optimal solution.

### {Optimal approach name}
{description}
- Time: ...
- Space: ...

**Key insight:** {one sentence}

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Brute force | ... | ... |
| {Optimal} | ... | ... |

---

## Interview Discussion Points

**Q: ...**
{answer}

(4–6 Q&A pairs)

---

## Traps to Avoid

- {bullet list}

---

## Related Problems

- {Problem Name} — {why related}
(4–6 items)
```

---

## solution.rb

```ruby
# LeetCode #{N} | {Difficulty} | {Topic Label}
# https://leetcode.com/problems/{slug}/

class {ClassName}
  def {method_name}({args})
    # TODO: implement
  end
end

processor = {ClassName}.new
puts processor.{method_name}({example_input}) # {expected}
# one puts per example from problem.md
```

Omit LeetCode URL line if not on LeetCode. Use `return` values that match example outputs.

---

## Empty language files

Create `solution.py`, `solution.js`, `solution.ts`, `Solution.java` as **zero-byte or single blank line** only.

---

## Topic README.md (create if missing)

```markdown
# {Topic Display Name}

## Core Pattern

{2–4 sentences + bullet list of when to use}

---

## Key Concepts

| Concept | Time | Space |
|---------|------|-------|
| ... | ... | ... |

---

## Problems

### Easy
| # | Problem | Key Insight |
|---|---------|-------------|
| 01 | [{Title}](easy/01-{slug}/problem.md) | {insight} |

### Medium
| # | Problem | Key Insight |
|---|---------|-------------|
| — | *Coming soon* | |

### Hard
| # | Problem | Key Insight |
|---|---------|-------------|
| — | *Coming soon* | |

---

## Common Interview Follow-ups

- {question}
```

When adding a problem to an existing README, insert the row in numeric order under the correct difficulty section; remove `*Coming soon*` only for that tier if it was a placeholder and other problems exist.
