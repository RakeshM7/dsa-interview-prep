# First Non-Recurring Character

**Difficulty:** Easy
**Topic:** Hashes + Strings
**Language:** Ruby
**LeetCode:** [#387](https://leetcode.com/problems/first-unique-character-in-a-string/)
**Interview Frequency:** Very High

---

## Problem Statement

Given a string `s`, find the **first non-repeating character** in it and return its index.
If there is no such character, return `-1`.

A non-repeating character appears in the string **exactly once**.

---

## Examples

```
Input:  s = "leetcode"
Output: 0
Reason: 'l' is the first character that appears only once (at index 0)
```

```
Input:  s = "loveleetcode"
Output: 2
Reason: 'v' is the first unique character (at index 2)
```

```
Input:  s = "aabb"
Output: -1
Reason: Every character repeats — no unique character exists
```

```
Input:  s = "z"
Output: 0
```

---

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters
- Empty string → return `-1` (or handle as an edge case before processing)

---

## Hint

Use two passes: first build a frequency map of every character, then scan the string left to right and return the index of the first character whose count is `1`.

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```
topics/01-arrays-and-hashing/easy/04-first-non-recurrent-character/
  problem.md        ← you are here
  solution.rb       ← frequency hash + second pass
  solution.py
  solution.js
  solution.ts
  Solution.java
  notes.md          ← complexity, interview Qs, traps
```
