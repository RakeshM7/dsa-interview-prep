# Largest Element in an Array

**Difficulty:** Easy  
**Topic:** Arrays  
**Interview Frequency:** Very Common  
**Source:** Striver A2Z DSA Sheet

---

## Problem Statement

Given an array of integers, find the largest element present in the array.

Return the maximum value.

---

## Examples

```text
Input: arr = [2, 5, 1, 3, 0]
Output: 5
```

Explanation:

The largest element in the array is `5`.

---

```text
Input: arr = [8, 10, 5, 7, 9]
Output: 10
```

Explanation:

The largest element in the array is `10`.

---

## Constraints

- `1 <= n <= 10^5`
- `-10^9 <= arr[i] <= 10^9`

---

## Hint

You do not need sorting to find the largest element.

Think about:
- keeping track of the maximum value seen so far
- updating it while traversing the array

---

## Expected Complexity

- Time Complexity: `O(n)`
- Space Complexity: `O(1)`

---

## Folder Structure

```text
01-largest-element-in-an-array/
  problem.md
  notes.md
  solution.rb
  solution.py
  solution.js
  solution.ts
  Solution.java
```

---

## Follow-up

Can you solve this problem:
- without sorting the array?
- in a single traversal?