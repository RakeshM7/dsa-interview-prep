# Baseball Game — Notes

## Problem Summary
You are given a list of operations representing scores in a baseball game.

Each operation can be:
- Integer → add a new score
- `"+"` → add a score equal to the sum of the previous two scores
- `"D"` → add a score equal to double the previous score
- `"C"` → invalidate and remove the previous score

Return the total sum of all valid scores.

---

## Approaches

### Brute Force
Maintain an array of scores and recompute totals whenever needed.

- `C` → remove last score
- `D` → append double of last score
- `+` → append sum of last two scores
- Number → append directly

At the end, iterate again to calculate total score.

- Time: O(n)
- Space: O(n)

Even though this works fine, interviewers usually expect the stack interpretation because operations always affect the most recent scores.

### Stack (Optimal)
Use a stack to track valid scores.

For each operation:
- Integer → push onto stack
- `"C"` → pop last score
- `"D"` → push `stack[-1] * 2`
- `"+"` → push `stack[-1] + stack[-2]`

Finally, return the sum of the stack.

- Time: O(n)
- Space: O(n)

**Key insight:** Every operation depends on the most recent valid scores → LIFO behavior → stack.

---

## Example Walkthrough

Input:

```text
ops = ["5", "2", "C", "D", "+"]
```

Step-by-step:

| Operation | Stack | Explanation |
|----------|-------|-------------|
| `5` | `[5]` | Add 5 |
| `2` | `[5, 2]` | Add 2 |
| `C` | `[5]` | Remove previous score |
| `D` | `[5, 10]` | Double previous score |
| `+` | `[5, 10, 15]` | Sum of last two scores |

Final answer:

```text
5 + 10 + 15 = 30
```

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Array / brute force tracking | O(n) | O(n) |
| Stack | O(n) | O(n) |

---

## Interview Discussion Points

**Q: Why is a stack the right data structure?**
Every operation affects the most recent valid score(s).
- `C` removes the latest score
- `D` uses the latest score
- `+` uses the latest two scores

That is classic LIFO behavior.

**Q: Why not use a queue?**
A queue removes the oldest element first (FIFO), but this problem always works with the latest scores.

**Q: Can we solve this in O(1) space?**
Not really.
You must remember previous valid scores because future operations depend on them.

**Q: What happens if operations are invalid?**
The problem guarantees all operations are valid.
For example:
- `D` will always have at least one previous score
- `+` will always have at least two previous scores
- `C` will always have a score to remove

**Q: What real concept does this simulate?**
Undo/history systems.
`C` behaves like undoing the latest operation.

---

## Traps to Avoid

- Forgetting that `+` uses the last TWO valid scores
- Modifying the stack incorrectly before computing `+`
- Treating numbers as strings instead of integers
- Forgetting to remove invalidated scores on `C`
- Returning stack length instead of stack sum

---

## Related Problems

- Valid Parentheses — stack matching
- Min Stack — stack with additional state
- Evaluate Reverse Polish Notation — stack-based evaluation
- Daily Temperatures — monotonic stack
- Backspace String Compare — undo-style stack operations