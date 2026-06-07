# Contains Duplicate

**Difficulty:** Easy

**Topic:** Arrays and Hashing

**LeetCode:** [#217](https://leetcode.com/problems/contains-duplicate/)

**Interview Frequency:** Very High

**Study Plan:** DSA - Day 4

---

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least
twice in the array.

Return `false` if every value in the array is unique.

Your solution must run in `O(n)` time.

---

## Examples

```text
Input:  nums = [1, 2, 3, 1]
Output: true
Explanation: The value 1 appears twice.
```

```text
Input:  nums = [1, 2, 3, 4]
Output: false
Explanation: Every value is unique.
```

```text
Input:  nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
Output: true
Explanation: Multiple values appear more than once.
```

---

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- The array may contain negative values
- An empty array or an array with one element returns `false`

---

## Expected Complexity

- Time: `O(n)`
- Space: `O(n)`

---

## Hint

As you traverse the array, keep track of values you have already encountered.
If the current value has been seen before, you can return immediately.

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```
topics/01-arrays-and-hashing/easy/02-contains-duplicates/
  problem.md        <- you are here
  notes.md          <- approaches, complexity, and interview notes
  testcases.md      <- test inputs and expected outputs
  solution.rb
  solution.py
  solution.js
  solution.ts
  Solution.java
```
