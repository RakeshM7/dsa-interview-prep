# Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Topic:** Sliding Window
**Language:** Ruby
**LeetCode:** [#3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
**Interview Frequency:** Extremely High

---

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

A **substring** is a contiguous sequence of characters within the string (not a subsequence).

---

## Examples

```
Input:  s = "abcabcbb"
Output: 3
Reason: The longest substring without repeating characters is "abc", length 3
```

```
Input:  s = "bbbbb"
Output: 1
Reason: The longest substring is "b", length 1
```

```
Input:  s = "pwwkew"
Output: 3
Reason: The longest substring is "wke", length 3 (not "pwke" — "pwke" is not contiguous)
```

```
Input:  s = ""
Output: 0
```

```
Input:  s = "dvdf"
Output: 3
Reason: "vdf" — the window skips the duplicate 'v' correctly when shrinking from the left
```

---

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces
- Empty string → return `0`

---

## Hint

Use two pointers (`left`, `right`) and a hash map storing each character’s **most recent index**. When you see a duplicate inside the current window, move `left` to `max(left, last_index[char] + 1)`. Track the maximum window size as you expand `right`.

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```
topics/03-sliding-window/medium/01-longest-substring-without-repeating-characters/
  problem.md        ← you are here
  solution.rb       ← sliding window + hash map
  solution.py
  solution.js
  solution.ts
  Solution.java
  notes.md          ← complexity, interview Qs, traps
```
