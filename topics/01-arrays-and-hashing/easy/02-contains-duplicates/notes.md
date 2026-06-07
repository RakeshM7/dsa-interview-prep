# Contains Duplicate - Notes

## Approaches

### Brute Force

Compare every pair of elements. Return `true` when two equal values are found.

- Time: `O(n²)`
- Space: `O(1)`
- Interview note: This is easy to explain, but it does not satisfy the required
  `O(n)` runtime.

### Hash Set (Optimal)

Traverse the array once. For each value:

1. Check whether it has already been seen.
2. Return `true` immediately if it has.
3. Otherwise, record it and continue.

If the traversal finishes, return `false`.

- Time: `O(n)` average
- Space: `O(n)`

**Key insight:** The problem only asks whether a value has appeared before, so
a membership lookup is sufficient. You do not need to store indices or counts.

### Sort and Compare Adjacent Values

Sort the array and compare each value with the value before it.

- Time: `O(n log n)`
- Space: Depends on the sorting algorithm
- Interview note: This does not satisfy the requested `O(n)` time constraint.

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Brute force | `O(n²)` | `O(1)` |
| Hash set | `O(n)` average | `O(n)` |
| Sort and scan | `O(n log n)` | Depends on sort |

---

## Interview Discussion Points

**Q: Why is the hash-set approach O(n)?**

Each element is visited once, and set membership and insertion are `O(1)` on
average.

**Q: Can the algorithm return early?**

Yes. As soon as a previously seen value is encountered, the answer is known.

**Q: What should happen for an empty array or one element?**

Return `false` because at least two occurrences are needed.

**Q: Can this be solved with O(1) extra space?**

Sorting in place and comparing adjacent values may use `O(1)` extra space, but
the runtime becomes `O(n log n)`, which violates this problem's `O(n)`
requirement.

**Q: What if the interviewer asks for the duplicate value or its indices?**

Return the repeated value when it is encountered, or use a map from value to
its first index.

---

## Traps to Avoid

- Returning `true` only when a value appears more than twice
- Forgetting that `[0, 0]` contains a duplicate
- Treating negative values differently from positive values
- Scanning the entire array after a duplicate has already been found
- Using nested loops despite the `O(n)` requirement
- Confusing this problem with Contains Duplicate II, which adds a distance limit

---

## Related Problems

- Contains Duplicate II - duplicate values within distance `k`
- Contains Duplicate III - index and value-distance restrictions
- Two Sum - hash map lookup with complements
- Valid Anagram - frequency counting with hashing
- First Non-Repeating Character - frequency-based uniqueness
