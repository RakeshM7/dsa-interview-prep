# Best Time to Buy and Sell Stock — Notes

## Approaches

### Brute Force
Check every pair (i, j) where j > i. Calculate profit = prices[j] - prices[i]. Track the maximum.
- Time: O(n²)
- Space: O(1)
- When to mention: Always mention brute force first in interviews before jumping to the optimal solution.

### Two Pointers (Optimal)
Use two pointers `lp` (left/buy) and `rp` (right/sell) both starting at index 0.
- If `prices[rp] < prices[lp]` → found a cheaper buy day, move `lp` to `rp`
- Otherwise → calculate profit, update `max_profit`
- Advance `rp` each iteration

- Time: O(n) — single pass
- Space: O(1) — no extra data structures

**Why this works:** `lp` always tracks the minimum price seen so far. For every sell candidate `rp`, we compute profit against the best possible buy. If `rp` is cheaper than `lp`, it becomes the new best buy — no point keeping the old one since everything to the left of `rp` is already covered.

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Brute force | O(n²) | O(1) |
| Two Pointers | O(n) | O(1) |

---

## Interview Discussion Points

**Q: Why can't we just find the global min and global max?**
Order matters — you must buy before you sell. The global max might come before the global min.
Example: `[3, 1, 2]` — global min is 1 (index 1), global max is 3 (index 0), but you can't sell before you buy.

**Q: What if prices only decrease?**
`lp` keeps moving right chasing the new minimum, `rp` never finds a profitable sell. `max_profit` stays 0 and we return 0.

**Q: What if all prices are equal?**
Every profit calculation yields 0. We return 0.

**Q: Can we extend this to multiple transactions?**
Yes — that's LeetCode #122. The greedy approach changes: sum up every positive day-over-day difference.

---

## Traps to Avoid

- Do not return a negative profit — the constraint says return 0 if no profit is possible.
- Do not forget to move `lp` to `rp` (not `lp + 1`) when a cheaper price is found.

---

## Related Problems

- Best Time to Buy and Sell Stock II (#122) — multiple transactions allowed
- Best Time to Buy and Sell Stock III (#123) — at most two transactions
- Best Time to Buy and Sell Stock with Cooldown (#309)
