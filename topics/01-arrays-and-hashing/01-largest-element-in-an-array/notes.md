# Largest Element in an Array — Notes

## Problem Summary

Find the maximum element present in the array.

The problem looks simple, but it introduces an extremely important interview concept:

> Traversing the array once while maintaining state.

This is the foundation for many array problems.

---

## Brute Force Approach

### Sorting

Sort the array and return the last element.

### Example

```text
arr = [2,5,1,3,0]

After sorting:
[0,1,2,3,5]
```

Largest element = `5`

---

## Algorithm

1. Sort the array
2. Return the last element

---

## Complexity

| Metric | Complexity |
|---|---|
| Time | O(n log n) |
| Space | Depends on sorting algorithm |

---

## Drawback

Sorting rearranges the entire array even though we only need one value.

That extra work is unnecessary.

---

## Optimal Approach

### Linear Scan

Traverse the array once while tracking the maximum element seen so far.

---

## Core Idea

At every index:

```text
max_element = max(max_element, current_element)
```

---

## Algorithm

1. Initialize:

```text
max_element = arr[0]
```

2. Traverse the array
3. If current element > max_element
   - update max_element
4. Return max_element

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Sorting | O(n log n) | O(1) / O(n) |
| Linear Scan | O(n) | O(1) |

---

## Why O(n) is Optimal

You must inspect every element at least once.

Therefore:

```text
Lower bound = O(n)
```

No algorithm can do better than linear time for this problem.

---

## Example Walkthrough

```text
arr = [2,5,1,3,0]
```

| Index | Element | Current Maximum |
|---|---|---|
| 0 | 2 | 2 |
| 1 | 5 | 5 |
| 2 | 1 | 5 |
| 3 | 3 | 5 |
| 4 | 0 | 5 |

Answer = `5`

---

## Key Insight

You only need:

- current element
- current maximum

No extra data structure is required.

---

## Interview Discussion Points

### Q: Why is sorting not optimal?

Because sorting performs unnecessary operations.

We only need one value:
- not the entire sorted order

---

### Q: Why initialize with arr[0]?

Because:
- arrays may contain negative numbers

Incorrect:

```text
max = 0
```

This fails for:

```text
[-5, -2, -10]
```

Correct:

```text
max = arr[0]
```

---

### Q: Can this be solved recursively?

Yes.

But iterative traversal is:
- simpler
- more memory efficient
- preferred in interviews

---

## Common Mistakes

### 1. Initializing max incorrectly

Wrong:

```text
max = 0
```

Correct:

```text
max = arr[0]
```

---

### 2. Sorting unnecessarily

Sorting increases time complexity.

---

### 3. Ignoring negative values

Always consider:
- all-negative arrays
- single-element arrays

---

## Edge Cases

### Single Element

```text
[7]
```

Answer = `7`

---

### All Negative Numbers

```text
[-10, -3, -50]
```

Answer = `-3`

---

### Already Sorted

```text
[1,2,3,4]
```

Answer = `4`

---

## Related Problems

- Second Largest Element in an Array
- Minimum Element in an Array
- Kth Largest Element
- Maximum Subarray Sum
- Check if Array is Sorted

---

## Pattern Recognition

This problem teaches:

- Array traversal
- Maintaining running state
- Observation-based optimization
- Replacing unnecessary sorting with linear scans

This pattern appears repeatedly in:
- sliding window
- greedy algorithms
- Kadane’s Algorithm
- prefix-based problems