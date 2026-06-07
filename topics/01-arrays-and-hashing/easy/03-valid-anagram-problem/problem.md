# Valid Anagram

**Difficulty:** Easy

**Topic:** Arrays, Hashing, and Strings

**LeetCode:** [#242](https://leetcode.com/problems/valid-anagram/)

**Interview Frequency:** Very High

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`.
Otherwise, return `false`.

An anagram is formed by rearranging all the characters of another string. Every
character must appear the same number of times in both strings.

Character comparison is case-sensitive. Unicode characters should be handled
as ordinary characters without case conversion or Unicode normalization.

---

## Examples

```text
Input:  s = "anagram", t = "nagaram"
Output: true
Explanation: Both strings contain the same characters with equal frequencies.
```

```text
Input:  s = "rat", t = "car"
Output: false
Explanation: The character frequencies are different.
```

```text
Input:  s = "Listen", t = "Silent"
Output: false
Explanation: Uppercase "L" and uppercase "S" are different characters.
```

```text
Input:  s = "déjà", t = "jàdé"
Output: true
```

---

## Constraints

- `0 <= s.length, t.length <= 10^5`
- The strings may contain letters, digits, symbols, mixed case, or Unicode
- Two empty strings are anagrams
- Strings of different lengths cannot be anagrams

---

## Required Functions

### `is_anagram_brute(s, t)`

- Sort both strings and compare the resulting character sequences
- Time: `O(n log n)`
- Space: `O(n)`

### `is_anagram_optimal(s, t)`

- Use one hash map
- Increment counts while reading `s`
- Decrement counts while reading `t`
- Time: `O(n)`
- Space: `O(k)`, where `k` is the number of distinct characters

---

## Hint

First check whether the string lengths differ. For the optimal solution, update
one frequency map with both strings. If every increment is balanced by a
decrement, the strings are anagrams.

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```
topics/01-arrays-and-hashing/easy/03-valid-anagram-problem/
  problem.md        <- you are here
  notes.md          <- approaches, complexity, and interview notes
  solution.rb
  solution.py
  solution.js
  solution.ts
  Solution.java
```
