# First Non-Recurring Character — Notes

## Approaches

### Brute Force
For each character at index `i`, scan the rest of the string (or the whole string) to count how many times it appears. Return `i` on the first character with count `1`.
- Time: O(n²)
- Space: O(1) — only counters, no hash map
- When to mention: Always mention brute force first in interviews before jumping to the optimal solution.

### Frequency Hash + Second Pass (Optimal)
**Pass 1:** Walk the string once and build a map of `character → count`.
**Pass 2:** Walk the string again left to right. Return the index of the first character whose count is `1`.
- Time: O(n)
- Space: O(1) — at most 26 lowercase letters, so the map size is bounded by the alphabet (often written as O(k) where k = 26)

**Why two passes:** Counting alone does not tell you which unique character appeared *first* — you need the original left-to-right order from a second scan (or an ordered structure that preserves it).

### Frequency Hash + Single Pass on Keys (Ruby-specific nuance)
In Ruby 1.9+, hashes preserve insertion order. If you iterate the hash after counting, the first key with count `1` is the first unique character in string order — because keys were inserted in order of first appearance.
- Same O(n) time and O(1) space bounds
- Prefer the explicit two-pass scan in interviews; it is clearer and works in every language

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Brute force | O(n²) | O(1) |
| Two-pass hash | O(n) | O(1) — fixed alphabet |
| Hash key iteration (Ruby) | O(n) | O(1) |

---

## Interview Discussion Points

**Q: Return the index vs return the character?**
LeetCode 387 asks for the **index** (`-1` if none). Some variants ask for the **character** itself (`nil` / `null` if none). Clarify with the interviewer which output is expected; the same two-pass logic applies — only the return value changes.

**Q: Can you do it in one pass?**
Not with a simple frequency map alone — you must see the full string before you know which characters repeat. One-pass solutions use extra structure (e.g. a linked list of unique candidates, or a queue) and are overkill for this problem at Easy level.

**Q: What about uppercase letters or Unicode?**
Expand the map key space (52 letters, or a full character set). Space is still O(k) where k is the size of the character set, not O(n).

**Q: What if the string is empty?**
Return `-1` (or `nil` for a character-return variant) immediately — no character can be unique.

**Q: How does this relate to Valid Anagram and Contains Duplicate?**
Same hashing theme: character (or element) frequencies. Here you combine counting with **ordering** — the first in string order among those with count `1`.

---

## Traps to Avoid

- Returning on the first character you see with count `1` during the **counting** pass — you have not finished counting yet, so repeats later in the string can invalidate that choice.
- Iterating the hash in languages where key order is **not** guaranteed (pre–Ruby 1.9, some older hash maps) — you may return the wrong character.
- Off-by-one on index vs character — `"leetcode"` → index `0`, character `'l'`.
- Forgetting the all-repeating case (`"aabb"`) — must return `-1` / `nil`, not the first character in the string.

---

## Related Problems

- Valid Anagram — compare two frequency maps
- Contains Duplicate — membership / count > 1, no ordering
- First Unique Character in String (LeetCode 387) — this problem
- Longest Substring Without Repeating Characters — sliding window + frequency
