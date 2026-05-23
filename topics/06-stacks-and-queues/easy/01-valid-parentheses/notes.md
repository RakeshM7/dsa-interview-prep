# Valid Parentheses — Notes

## Approaches

### Brute Force (Repeated Replacement)
Repeatedly remove valid adjacent pairs `"()"`, `"[]"`, `"{}"` from the string until no more can be removed. If the string becomes empty, it was valid.
- Time: O(n²) — each pass scans the string; up to n/2 passes
- Space: O(n) — string copies or a mutable buffer
- When to mention: Shows you understand the pairing idea, but the stack approach is cleaner

### Stack (Optimal)
Single left-to-right scan:
- **Opening bracket** → push onto stack
- **Closing bracket** → stack must be non-empty and top must be the matching opener; pop if match, else return `false`
- After the scan → return `true` only if stack is empty

- Time: O(n)
- Space: O(n) — stack holds up to n/2 openers in the worst case

**Key insight:** The most recently opened bracket must close first — last-in, first-out → stack.

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Repeated replacement | O(n²) | O(n) |
| Stack | O(n) | O(n) |

---

## Interview Discussion Points

**Q: Why a stack and not a queue?**
Closing brackets match the **most recent** unmatched opener (LIFO). A queue (FIFO) would match the oldest opener, which is wrong for nested brackets.

**Q: Can you use O(1) space?**
Only if you can assume a **single bracket type** (e.g. only `(` and `)`). Then a counter works. With three types, you need to remember which openers are pending and in what order — that requires O(n) space in the worst case.

**Q: What if the string has other characters (letters, digits)?**
Ignore non-bracket characters and run the same logic on brackets only, or treat unknown characters as invalid — clarify with the interviewer.

**Q: What about `"((("` or `")))"`?**
`"((("` → stack not empty at end → `false`. `")))"` → closing bracket with empty stack → `false` immediately.

**Q: How is this related to other stack problems?**
Same LIFO matching idea appears in: Min Stack, Evaluate Reverse Polish Notation, Decode String, and HTML/tag validation.

---

## Traps to Avoid

- Forgetting to check **stack empty** before pop on a closing bracket — `")"` alone should return `false`.
- Forgetting to check **stack empty at the end** — `"("` alone should return `false`.
- Mismatching pairs — `"(]"` must return `false` even though both sides are brackets.
- Wrong order — `"([)]"` fails because `[` must close before `(` can close with `)`.
- Empty string `""` → `true`, not `false`.

---

## Related Problems

- Minimum Add to Make Parentheses Valid — count unmatched
- Longest Valid Parentheses — dynamic programming / stack
- Remove Invalid Parentheses — backtracking
- Decode String — stack of strings / counts
- Implement Stack using Queues — data structure design
