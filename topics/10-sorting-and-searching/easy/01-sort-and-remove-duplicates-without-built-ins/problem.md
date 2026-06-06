# Sort and Remove Duplicates Without Built-ins

**Difficulty:** Easy  
**Topic:** Sorting, Arrays, Two Pointers  
**Interview Frequency:** Common

---

## Problem Statement

Given an array of integers, sort the array in ascending order and remove all
duplicate values.

You must not use:

- A built-in sorting function such as `sort()` or `sorted()`
- Sets, hash maps, dictionaries, or similar collection types for deduplication

Modify the input array in place and return the number of distinct values, `k`.
After the function returns, the first `k` positions of the array must contain
the sorted distinct values. Values after index `k - 1` do not matter.

Basic array indexing, assignment, length access, loops, and local variables are
allowed.

---

## Examples

```text
Input:  arr = [4, 2, 4, 1, 3, 2]
Output: k = 4, arr[0...k] = [1, 2, 3, 4]
```

```text
Input:  arr = [5, 5, 5, 5]
Output: k = 1, arr[0...k] = [5]
```

```text
Input:  arr = [-1, 3, -1, 2, 3, 0]
Output: k = 4, arr[0...k] = [-1, 0, 2, 3]
```

```text
Input:  arr = []
Output: k = 0, arr[0...k] = []
```

```text
Input:  arr = [7]
Output: k = 1, arr[0...k] = [7]
```

---

## Constraints

- `0 <= arr.length <= 10^5`
- `-10^9 <= arr[i] <= 10^9`
- The input array may be empty
- The input array may already be sorted
- The input array may contain only duplicate values

---

## Expected Complexity

- Time: `O(n log n)`
- Extra space: `O(1)`

---

## Hint

First implement an in-place comparison sort with guaranteed `O(n log n)` time.
Once the array is sorted, equal values are adjacent, so a write pointer can
compact the distinct values into the front of the same array.

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```text
topics/10-sorting-and-searching/easy/01-sort-and-remove-duplicates-without-built-ins/
  problem.md        <- you are here
  notes.md          <- approaches, complexity, interview discussion
  solution.rb
  solution.py
  solution.js
  solution.ts
  Solution.java
```
