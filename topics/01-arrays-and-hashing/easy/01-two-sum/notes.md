# Two Sum — Notes

## Approaches

### Brute Force
Iterate every pair (i, j) where j > i. Check if they sum to target.
- Time: O(n²)
- Space: O(1)
- When to mention: Always mention brute force first in interviews before jumping to the optimal solution.

### HashMap (Optimal)
Single pass. For each element, compute `complement = target - nums[i]`.
Check if complement is already in the map. If yes, return indices. If no, store current element.

- Time: O(n)
- Space: O(n)

**Why one pass works:** You do not need to pre-populate the map. If pair (A, B) satisfies A + B = target, then when you process B, A is guaranteed to already be in the map.

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Brute force | O(n²) | O(1) |
| HashMap | O(n) | O(n) |

---

## Interview Discussion Points

**Q: Can you solve it without extra space?**
Yes, but only if the array is sorted first — then you can use two pointers (O(n log n) time, O(1) space). The original problem does not guarantee a sorted array, so HashMap is the general optimal solution.

**Q: What if there are multiple valid pairs?**
The current implementation returns the first found pair. If all pairs are needed, collect results into a list instead of returning on first match.

**Q: What if no valid pair exists?**
The problem guarantees exactly one solution. In production code, you would return `null` or throw an exception.

**Q: How does this behave with hash collisions?**
Java's HashMap and Python's dict use separate chaining / open addressing with load factor management. In practice, average-case O(1) is reliable. Worst-case is O(n) per lookup if all keys hash to the same bucket, but this is extremely rare with standard implementations.

**Q: What if the same number appears twice (e.g., [3, 3], target = 6)?**
This works correctly. When we process the second 3, the first 3 is already in the map with index 0. We return [0, 1].

---

## Traps to Avoid

- Do not add the current element to the map *before* checking for the complement. Otherwise `[3, 3], target = 6` would incorrectly return `[0, 0]` using the same element twice.
- Always store `value → index`, not `index → value`. You look up by value.

---

## Related Problems

- Two Sum II (sorted array) — two pointers
- Three Sum — sort + two pointers
- Four Sum — sort + nested two pointers
