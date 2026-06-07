# Valid Anagram - Notes

## Approaches

### Sort and Compare

If the strings have different lengths, return `false`. Otherwise, sort the
characters in each string and compare the sorted sequences.

```text
sorted("anagram") == sorted("nagaram")
['a', 'a', 'a', 'g', 'm', 'n', 'r']
==
['a', 'a', 'a', 'g', 'm', 'n', 'r']
```

- Time: `O(n log n)`
- Space: `O(n)` for the sorted character sequences
- Interview note: Simple and useful as a baseline, but slower than frequency
  counting.

### Single Hash Map with Increment and Decrement

1. Return `false` immediately if the lengths differ.
2. Increment the count for every character in `s`.
3. Decrement the count for every character in `t`.
4. If a count becomes negative, `t` contains too many copies of that character.
5. If the scan finishes, every count is balanced and the strings are anagrams.

- Time: `O(n)`
- Space: `O(k)`, where `k` is the number of distinct characters

**Key insight:** Equal-length anagrams have identical character frequencies.
Using one map lets the second string cancel the counts created by the first.

---

## Complexity Summary

| Approach | Time | Space |
|----------|------|-------|
| Sort and compare | `O(n log n)` | `O(n)` |
| One frequency map | `O(n)` | `O(k)` |

---

## Interview Discussion Points

**Q: Why check the lengths first?**

Strings with different lengths cannot contain identical character frequencies.
The check also prevents unnecessary work.

**Q: Why is one hash map enough?**

Counts from `s` are incremented and counts from `t` are decremented. A negative
count means `t` contains a character too many times.

**Q: Do all map entries need to be checked at the end?**

Not if the strings have equal lengths and the algorithm returns when any count
becomes negative. Equal total lengths guarantee that no unmatched positive
count can remain without some other count becoming negative.

**Q: Is the comparison case-sensitive?**

Yes. `"A"` and `"a"` are different characters unless the requirements
explicitly say to normalize case.

**Q: How should Unicode be handled?**

Treat each language-level character as a key. Do not normalize accented or
composed characters unless the interviewer adds that requirement.

**Q: Could a fixed-size array replace the hash map?**

Yes, if input is guaranteed to use a small fixed alphabet such as lowercase
English letters. A hash map is more general and supports mixed case and
Unicode.

---

## Traps to Avoid

- Forgetting the early length check
- Using two maps when the requirement asks for one
- Lowercasing strings without being asked
- Assuming input contains only `a` through `z`
- Comparing only whether both strings contain the same distinct characters
- Forgetting that repeated characters must have equal counts
- Applying Unicode normalization when exact character comparison is expected

---

## Related Problems

- Group Anagrams - use a canonical representation as a grouping key
- Find All Anagrams in a String - sliding window with frequency counts
- Ransom Note - verify that one string supplies enough characters
- First Non-Recurring Character - count characters and preserve order
- Contains Duplicate - hash-based membership checking
