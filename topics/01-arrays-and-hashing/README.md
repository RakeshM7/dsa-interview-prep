# Arrays & Hashing

## Core Pattern

Use a **HashMap** (or HashSet) to trade space for time. Instead of a nested loop checking all pairs (O(n²)), store elements you have already seen and look up the complement in O(1).

**When to reach for this pattern:**
- "Find two elements that satisfy a condition" → HashMap of seen values
- "Check for duplicates / uniqueness" → HashSet
- "Group elements by a key" → HashMap<Key, List>
- "Count frequencies" → HashMap<Value, Count>

---

## Key Concepts

| Concept | Time | Space |
|---------|------|-------|
| HashMap get / put | O(1) avg | O(n) |
| HashSet contains / add | O(1) avg | O(n) |
| Sorting the array first | O(n log n) | O(1) |
| Nested loop brute force | O(n²) | O(1) |

---

## Problems

### Easy
| # | Problem | Key Insight |
|---|---------|-------------|
| 01 | [Two Sum](easy/01-two-sum/problem.md) | Store complement in HashMap |
| 02 | Contains Duplicate | HashSet membership check |
| 03 | Valid Anagram | Frequency count comparison |

### Medium
| # | Problem | Key Insight |
|---|---------|-------------|
| 01 | Group Anagrams | Sorted string as HashMap key |
| 02 | Top K Frequent Elements | HashMap + bucket sort / heap |
| 03 | Product of Array Except Self | Prefix and suffix products |

### Hard
| # | Problem | Key Insight |
|---|---------|-------------|
| 01 | Longest Consecutive Sequence | HashSet + expand only from sequence start |

---

## Common Interview Follow-ups

- What if the array is sorted? Does that change your approach?
- What if there are multiple valid answers?
- Can you do it without extra space?
- How does this behave with hash collisions?
