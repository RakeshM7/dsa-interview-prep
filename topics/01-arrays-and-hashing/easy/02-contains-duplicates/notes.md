# Contains Duplicate — Notes

## Approaches

### Brute Force
Compare every pair (i, j) where j > i. Return `true` on the first equal pair.
- Time: O(n²)
- Space: O(1)
- When to mention: Always mention brute force first in interviews before jumping to the optimal solution.

### Hash Set (Optimal)
Single pass. For each element, check if it is already in the set. If yes, return `true`. If no, add it.
- Time: O(n)
- Space: O(n)

**Key insight:** You only need to know whether a value was seen before — not its index — so a `Set` is enough (unlike Two Sum, which needs `value → index`).

### Sort + Adjacent Compare (Alternative)
Sort the array, then check if any adjacent elements are equal.
- Time: O(n log n)
- Space: O(1) if you can sort in place (or O(n) if sorting copies the array)
- Useful when the interviewer asks for O(1) extra space and in-place mutation is allowed.

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Brute force | O(n²) | O(1) |
| Hash set | O(n) | O(n) |
| Sort + scan | O(n log n) | O(1) in-place |

---

## Interview Discussion Points

**Q: Can you solve it without extra space?**
Yes — sort first and compare neighbors. Trade-off: O(n log n) time and you mutate the input (or need O(n) space for a copy).

**Q: What about an empty array or a single element?**
Both return `false` — no pair exists to duplicate.

**Q: Can you use `len(set(nums)) != len(nums)` in Python?**
Yes — elegant one-liner, but still O(n) time and O(n) space to build the set. Good to mention, but walk through the explicit loop for clarity.

**Q: What if you need the duplicate value or its indices?**
Extend the set approach: store `value → first index`, return as soon as you see a value already in the map.

**Q: How does this relate to Two Sum?**
Same pattern — hash structure for O(1) lookups — but simpler: membership check only, no complement arithmetic.

---

## Traps to Avoid

- Empty array `[]` → `false`, not an error.
- Single element `[5]` → `false`.
- Negative numbers work the same; the set/hash handles them like any integer.
- Do not confuse with **Contains Duplicate II** (duplicate within distance k) or **III** (within sorted window) — those need different techniques.

---

## Related Problems

- Contains Duplicate II — sliding window + hash set (distance ≤ k)
- Contains Duplicate III — sorted set / tree map (value within range t)
- Valid Anagram — same hashing theme, character counts
- Two Sum — hash map with complement lookup
