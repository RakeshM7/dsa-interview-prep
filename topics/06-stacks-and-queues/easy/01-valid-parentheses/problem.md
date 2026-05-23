# Valid Parentheses

**Difficulty:** Easy
**Topic:** Stacks
**Language:** Ruby
**LeetCode:** [#20](https://leetcode.com/problems/valid-parentheses/)
**Interview Frequency:** Extremely High

---

## Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is **valid**.

A string is valid if:

1. Every opening bracket has a corresponding closing bracket of the **same type**.
2. Opening brackets are closed in the **correct order**.
3. Every closing bracket has a corresponding **earlier** opening bracket.

Return `true` if valid, otherwise `false`.

---

## Examples

```
Input:  s = "()"
Output: true
```

```
Input:  s = "()[]{}"
Output: true
```

```
Input:  s = "(]"
Output: false
Reason: '(' is closed by ']' — wrong type
```

```
Input:  s = "([)]"
Output: false
Reason: brackets are not closed in the correct order
```

```
Input:  s = "{[]}"
Output: true
```

```
Input:  s = ""
Output: true
Reason: empty string has no unmatched brackets
```

---

## Constraints

- `0 <= s.length <= 10^4`
- `s` consists of parentheses only: `'()[]{}'`
- Empty string → return `true`

---

## Hint

Use a stack. Push each opening bracket. When you see a closing bracket, the top of the stack must be its matching opener — pop and continue. If the stack is empty at the end, the string is valid.

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```
topics/06-stacks-and-queues/easy/01-valid-parentheses/
  problem.md        ← you are here
  solution.rb       ← stack matching
  solution.py
  solution.js
  solution.ts
  Solution.java
  notes.md          ← complexity, interview Qs, traps
```
