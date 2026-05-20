# Longest Substring Without Repeating Characters — Notes

## Approaches

### Brute Force
For each starting index `i`, extend `j` from `i` while characters in `s[i..j]` are unique (use a set to check). Track the maximum length.
- Time: O(n²) — O(n) starts × O(n) extend per start
- Space: O(min(n, charset)) — set in the inner loop
- When to mention: Always mention brute force first in interviews before jumping to the optimal solution.

### Sliding Window + Hash Set
Two pointers `left` and `right`. Expand `right` and add `s[right]` to a set. If duplicate, shrink from `left` (remove `s[left]` from set, increment `left`) until unique again. Track max window size.
- Time: O(n) — each character added and removed at most once
- Space: O(min(n, charset))

**Key insight:** `right` only moves forward; `left` catches up when the window is invalid — no need to restart from every `i`.

### Sliding Window + Hash Map (Optimal)
Store `char → last index seen`. When `s[right]` was seen at index `last` and `last >= left`, jump `left` to `last + 1` (use `left = [left, last + 1].max` so `left` never moves backward). Update max length as `right - left + 1` each step.
- Time: O(n)
- Space: O(min(n, charset))

**Why `max(left, last + 1)`:** A character may appear in the map from *outside* the current window (e.g. `"abba"` when `left` is past the first `'a'`). Only shrink when the duplicate is inside `[left, right]`.

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Brute force | O(n²) | O(min(n, charset)) |
| Window + set | O(n) | O(min(n, charset)) |
| Window + hash map | O(n) | O(min(n, charset)) |

---

## Interview Discussion Points

**Q: Substring vs subsequence?**
This problem requires **contiguous** characters. Subsequence problems (e.g. longest increasing subsequence) use DP, not sliding window.

**Q: Return length vs return the actual substring?**
Same window logic; also track `start_index` and `max_len`, then return `s[start_index, start_index + max_len]`.

**Q: What about `"dvdf"`?**
Naive “jump `left` to last_index + 1`” without `max(left, …)` can move `left` backward. Always clamp: `left = max(left, last_index[char] + 1)`.

**Q: Can you do it with a fixed-size window?**
No — window size varies. Fixed windows apply to problems like “max sum of subarray of size k.”

**Q: How does this extend to at most K distinct characters?**
Same two pointers, but shrink when distinct count > K (frequency map + count of distinct keys).

**Q: How does this relate to Contains Duplicate II?**
Both use a window + hash structure; Duplicate II caps window *length* (index distance), this problem caps *uniqueness*.

---

## Traps to Avoid

- Using `left = last_index + 1` without `max(left, …)` — breaks on `"abba"`, `"dvdf"`.
- Confusing substring with subsequence — `"pwwkew"` answer is `3` (`"wke"`), not `4`.
- Forgetting empty string → `0`.
- Not updating the answer **after** adjusting `left` — window `[left, right]` must be valid when you record length.
- Off-by-one on length: inclusive window size is `right - left + 1`.

---

## Related Problems

- Longest Substring with At Most K Distinct Characters — same window, different constraint
- Minimum Window Substring — variable window, shrink until valid
- Contains Duplicate II — window of indices distance ≤ k
- First Non-Recurring Character — hashing + order
- Valid Parentheses — different stack pattern, often taught before sliding window
