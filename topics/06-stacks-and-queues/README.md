# Stacks & Queues

## Core Pattern

Use a **stack** (LIFO) or **queue** (FIFO) when order of processing matters — especially for matching pairs, nested structures, or level-by-level traversal.

**When to reach for this pattern:**
- "Validate or match opening/closing pairs" → Stack
- "Process in reverse order / undo operations" → Stack
- "First-in-first-out scheduling" → Queue
- "Level-order traversal" → Queue (BFS)

---

## Key Concepts

| Concept | Time | Space |
|---------|------|-------|
| Stack push / pop | O(1) | O(n) |
| Queue enqueue / dequeue | O(1) | O(n) |
| Single-pass scan with stack | O(n) | O(n) |

---

## Problems

### Easy
| # | Problem | Key Insight |
|---|---------|-------------|
| 01 | [Valid Parentheses](easy/01-valid-parentheses/problem.md) | Stack matches each closing bracket to the most recent opener |

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

- What if the string contains characters other than brackets?
- Can you solve it without a stack?
- How would you extend this to HTML/XML tag validation?
- Stack vs queue — when do you pick each?
