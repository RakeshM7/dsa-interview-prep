# Interview Tips

## The 5-Step Framework for Every Problem

1. **Clarify** — Ask about constraints, edge cases, and expected output before writing code.
2. **Brute force** — State the naive solution and its complexity out loud. Never jump straight to optimal.
3. **Optimize** — Identify the bottleneck (usually the nested loop) and ask what data structure eliminates it.
4. **Code** — Write clean, readable code. Name variables well. Do not compress logic.
5. **Verify** — Walk through examples manually. Test edge cases: empty array, single element, duplicates, negatives.

---

## What Interviewers Actually Evaluate

- **Problem decomposition:** Can you break the problem down before writing?
- **Communication:** Are you thinking out loud?
- **Edge case awareness:** Do you ask about them, or do they have to prompt you?
- **Code clarity:** Would a teammate understand your code?
- **Debugging:** Can you trace through your own code and find bugs?

---

## Common Edge Cases to Always Check

- Empty array or null input
- Single-element array
- All elements the same
- Negative numbers
- Integer overflow (especially in Java — use long when summing large numbers)
- Target is 0
- Array is already sorted (does your solution handle this correctly?)

---

## How to Explain Complexity

Always explain both time and space. Use this structure:

> "The brute force is O(n²) time and O(1) space because we check every pair. The optimal solution uses a HashMap, which gives us O(n) time and O(n) space because we trade memory for a single-pass lookup."

---

## Phrases That Signal Strong Engineering Thinking

- "Before I code, let me clarify the constraints..."
- "The brute force would be... but the bottleneck is the nested loop..."
- "I can trade O(n) space for O(n) time by using a HashMap..."
- "Edge cases I want to handle are..."
- "Let me trace through this example to verify..."
