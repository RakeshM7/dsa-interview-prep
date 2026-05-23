# Baseball Game

**Difficulty:** Easy  
**Topic:** Stacks  
**Language:** Ruby  
**LeetCode:** [#682](https://leetcode.com/problems/baseball-game/)  
**Interview Frequency:** Medium

---

## Problem Statement

You are keeping score for a baseball game with strange rules.

You are given a list of strings `ops`, where each string represents an operation.

The operations are:

- Integer `x`
  - Record a new score of `x`

- `"+"`
  - Record a new score that is the sum of the previous two scores

- `"D"`
  - Record a new score that is double the previous score

- `"C"`
  - Invalidate and remove the previous score

Return the sum of all valid scores after performing all operations.

---

## Examples

```text
Input: ops = ["5","2","C","D","+"]
Output: 30
```

Explanation:

- Add 5 → [5]
- Add 2 → [5,2]
- Remove previous score → [5]
- Double previous score → [5,10]
- Add sum of previous two → [5,10,15]

Total = 5 + 10 + 15 = 30

---

```text
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
```

---

```text
Input: ops = ["1"]
Output: 1
```

---

## Constraints

- `1 <= ops.length <= 1000`
- `ops[i]` is either:
  - an integer in the range `[-3 * 10^4, 3 * 10^4]`
  - `"+"`
  - `"D"`
  - `"C"`
- The input is guaranteed to be valid.

---

## Hint

This is a classic stack problem.

- Scores are added and removed from the most recent entries.
- `C` removes the latest score.
- `D` depends on the latest score.
- `+` depends on the latest two scores.

Think about which data structure naturally supports operations on the most recent elements.

---

## Attempt the problem yourself before opening the solution file.

Where this file lives in the repo:

```text
topics/06-stacks-and-queues/easy/02-baseball-game/
  problem.md        ← you are here
  solution.rb       ← stack simulation
  solution.py
  solution.js
  solution.ts
  Solution.java
  notes.md          ← complexity, interview Qs, traps
```