# Maximum Subarray — Notes

## Approaches

### Brute Force
Check every possible subarray (i, j). Sum each one and track the maximum.
- Time: O(n²) — two nested loops
- Space: O(1)
- When to mention: Always mention brute force first in interviews before jumping to the optimal.

### Kadane's Algorithm (Optimal)
Single pass. At each position, decide:
- **Extend** the current subarray: `current_sum + nums[i]`
- **Start fresh** from here: `nums[i]`

Take whichever is larger. This is the key insight — if the running sum has gone negative, it only drags down whatever comes next. Restart from the current element.

Update `max_sum` after each decision.

- Time: O(n) — single pass
- Space: O(1) — only two variables

**The DP perspective:** `dp[i]` = max subarray sum ending at index `i`.
Recurrence: `dp[i] = max(nums[i], dp[i-1] + nums[i])`
We don't need the full `dp` array — only the previous value, so it reduces to O(1) space.

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Brute force | O(n²) | O(1) |
| Kadane's Algorithm | O(n) | O(1) |

---

## Walkthrough — `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| i | nums[i] | current_sum | max_sum |
|---|---------|-------------|---------|
| 0 | -2      | -2          | -2      |
| 1 | 1       | 1           | 1       |
| 2 | -3      | -2          | 1       |
| 3 | 4       | 4           | 4       |
| 4 | -1      | 3           | 4       |
| 5 | 2       | 5           | 5       |
| 6 | 1       | 6           | **6**   |
| 7 | -5      | 1           | 6       |
| 8 | 4       | 5           | 6       |

Result: **6** → subarray `[4, -1, 2, 1]`

---

## Interview Discussion Points

**Q: What if all numbers are negative?**
Kadane's handles it correctly — `max_sum` is initialized to `nums[0]` (not 0), so the least-negative element is returned. Be careful not to initialize `max_sum = 0` or you'll wrongly return 0 for all-negative arrays.

**Q: What if we need to return the actual subarray, not just the sum?**
Track `start`, `end`, and `temp_start` indices. When you restart (`nums[i] > current_sum + nums[i]`), update `temp_start = i`. When you update `max_sum`, set `start = temp_start`, `end = i`.

**Q: Is this greedy or DP?**
Both — it can be framed either way. DP: `dp[i] = max(nums[i], dp[i-1] + nums[i])`. Greedy: at each step, greedily drop the prefix if it's negative. Either explanation is valid in an interview.

**Q: Can this be solved with divide and conquer?**
Yes — O(n log n). Split the array in half; the answer is either in the left half, right half, or crosses the midpoint. Less efficient than Kadane's but good to know.

---

## Traps to Avoid

- Do not initialize `max_sum = 0` — this breaks all-negative input.
- Do not confuse "maximum subarray sum" with "maximum subarray product" (a different problem).

---

## Related Problems

- Maximum Product Subarray (#152) — same pattern but multiplication changes things
- Maximum Sum Circular Subarray (#918) — Kadane's on a circular array
- Longest Turbulent Subarray (#978)
