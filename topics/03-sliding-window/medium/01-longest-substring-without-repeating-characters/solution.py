"""
Longest Substring Without Repeating Characters
LeetCode #3 | Difficulty: Medium | Topic: Sliding Window
"""


# Approach: Sliding Window + Hash Map
# Time:  O(n)
# Space: O(min(n, charset_size))
def length_of_longest_substring(s: str) -> int:
    max_substring_len = 0
    left_ptr = 0
    right_ptr = 0
    tracker = {}
    while left_ptr < len(s) and right_ptr < len(s):
        current_char = s[right_ptr]
        if current_char in tracker and tracker[current_char] >= left_ptr:
            left_ptr = tracker[current_char] + 1

        tracker[current_char] = right_ptr
        ss_len = right_ptr - left_ptr + 1
        right_ptr += 1
        if ss_len > max_substring_len:
            max_substring_len = ss_len
    return max_substring_len


# Driver
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),       # "abc"
        ("bbbbb", 1),          # all repeated chars
        ("pwwkew", 3),         # "wke", not "pwke"
        ("", 0),               # empty string
        ("dvdf", 3),           # duplicate before current best window
        ("a", 1),              # single character
        ("au", 2),             # two unique characters
        ("aa", 1),             # two same characters
        ("abba", 2),           # left pointer should not move backward
        ("tmmzuxt", 5),        # "mzuxt"
        ("abcdef", 6),         # all unique
        ("abcadefg", 7),       # "bcadefg"
        ("a b c a", 3),        # spaces count as repeated characters
        ("!@#$!@#", 4),        # symbols
        ("AaBbCcAa", 6),       # case-sensitive chars
        ("123451234", 5),      # digits
        ("abc def!gh", 10),    # letters, space, and symbol
        ("anviaj", 5),         # "nviaj"
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        if result == expected:
            print("Passed")
        else:
            print(f"[Fail] s={s!r} -> {result} (expected {expected})")
