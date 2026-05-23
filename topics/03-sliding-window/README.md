# Sliding Window

## Core Pattern

Maintain a **window** `[left, right]` over an array or string. Expand `right` to grow the window, then shrink `left` when a constraint is violated. Track the best answer as the window moves.

**When to reach for this pattern:**
- "Longest/shortest substring satisfying a condition" → variable-size window
- "Maximum sum of subarray of size k" → fixed-size window
- "At most K distinct characters / elements" → window + frequency map

---

## Key Concepts

| Concept | Time | Space |
|---------|------|-------|
| Fixed window of size k | O(n) | O(1) or O(k) |
| Variable window (expand/shrink) | O(n) | O(k) — charset or distinct count |
| HashMap for last-seen index | O(n) | O(min(n, charset)) |

---

## Problems

### Medium
| # | Problem | Key Insight |
|---|---------|-------------|
| 01 | [Longest Substring Without Repeating Characters](medium/01-longest-substring-without-repeating-characters/problem.md) | Shrink left when a duplicate appears in the window |

### Easy
| # | Problem | Key Insight |
|---|---------|-------------|
| — | *Coming soon* | |

### Hard
| # | Problem | Key Insight |
|---|---------|-------------|
| — | *Coming soon* | |

---

## Common Interview Follow-ups

- What if you need the substring itself, not just the length?
- How does this change for **at most K** distinct characters?
- Can you solve it with a Set instead of a HashMap?
- Fixed window vs variable window — when do you use each?
