# Valid Anagram

**Difficulty:** Easy
**Topic:** Hashes + Strings
**Language:** Ruby
**LeetCode:** [#242](https://leetcode.com/problems/valid-anagram/)
**Interview Frequency:** Very High

---

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An anagram is a word formed by **rearranging the letters** of another word, using all original letters **exactly once**.

---

## Examples

```
Input:  s = "anagram", t = "nagaram"
Output: true

Input:  s = "rat", t = "car"
Output: false

Input:  s = "listen", t = "silent"
Output: true

Input:  s = "hello", t = "world"
Output: false
```

---

## Constraints

- Both strings contain only lowercase English letters
- Strings can be empty — two empty strings are anagrams of each other
- If lengths differ → immediately `false`

---

## Hint

An anagram means both strings have exactly the same character frequencies.
Build a frequency hash for each string and compare them.

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```
topics/01-arrays-and-hashing/easy/03-valid-anagram/
  problem.md        ← you are here
  solution.rb       ← brute force + optimal
  notes.md          ← complexity, interview Qs, traps
```
