# Sort and Remove Duplicates Without Built-ins - Notes

## Approaches

### Brute Force: Selection Sort and Compaction

Use selection sort to order the array without a built-in sorting function.
Then scan the sorted array and copy each new value to the next write position.

- Time: `O(n²)`
- Extra space: `O(1)`
- When to mention: It is simple to implement, but it does not scale to the
  maximum input size.

### Optimal: Heap Sort and Two-Pointer Compaction

1. Rearrange the array into a max heap.
2. Repeatedly move the largest value to the end and restore the heap.
3. Scan the sorted array with a read pointer and a write pointer.
4. Write a value only when it differs from the last distinct value.

- Time: `O(n log n)` for heap sort plus `O(n)` for compaction
- Extra space: `O(1)`

**Key insight:** Sorting makes all equal values adjacent, allowing duplicates
to be removed with one linear pass and no lookup collection.

---

## Complexity Summary

| Approach | Time | Extra Space |
|----------|------|-------------|
| Selection sort + compaction | O(n²) | O(1) |
| Heap sort + compaction | O(n log n) | O(1) |

---

## Why Heap Sort?

- It has a guaranteed `O(n log n)` runtime.
- It sorts in place.
- It does not require a temporary merge array.
- An iterative `heapify` avoids recursion stack space.

Quicksort is often fast in practice, but a poor pivot strategy can degrade to
`O(n²)`. Merge sort guarantees `O(n log n)` time but normally needs `O(n)`
extra space for arrays.

---

## Interview Discussion Points

**Q: Why not remove duplicates before sorting?**  
Without a set or map, determining whether every value has appeared before can
require scanning the earlier portion of the array, leading to `O(n²)` time.

**Q: What does the returned value represent?**  
The returned value `k` is the number of distinct elements. The valid answer is
stored in indices `0` through `k - 1`.

**Q: What if the input is already sorted?**  
The compaction phase alone would take `O(n)`. If sorted input were guaranteed,
the heap sort phase could be skipped.

**Q: Is heap sort stable?**  
No. Stability does not affect this problem because duplicate integers are
indistinguishable and only one copy is retained.

**Q: Can the physical length of every input array be reduced in place?**  
Not in languages such as Java, where arrays have fixed length. Returning `k`
provides one contract that works consistently across languages.

**Q: Are basic array operations considered forbidden collections?**  
The input itself is an array, so indexing and assignment must be allowed. The
restriction targets helper collections and library operations that perform the
sorting or deduplication.

---

## Traps to Avoid

- Calling a built-in sort indirectly
- Using a set, map, dictionary, or frequency table
- Forgetting that the empty array should return `0`
- Starting the write pointer incorrectly and losing the first value
- Comparing against `arr[read - 1]` after overwriting values during compaction
- Implementing recursive heapify while claiming strict `O(1)` extra space

---

## Related Problems

- Remove Duplicates from Sorted Array - same compaction step with sorted input
- Sort an Array - focuses on implementing an efficient comparison sort
- Contains Duplicate - detects duplicates without needing ordered output
- Move Zeroes - another in-place read/write pointer problem
- Kth Largest Element in an Array - can also use heap operations
