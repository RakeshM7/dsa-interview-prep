"""
Contains Duplicate
LeetCode #217 | Difficulty: Easy | Topic: Arrays & Hashing
"""

from typing import List


# ── Approach 1: Brute Force ───────────────────────────────────────────────────
# Compare every pair of indices.
# Time:  O(n²)
# Space: O(1)
def contains_duplicate_brute(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


# ── Approach 2: Hash Set (Optimal) ────────────────────────────────────────────
# Single pass. If we've seen the value before, we have a duplicate.
# Otherwise, add it to the set.
#
# Time:  O(n)   — single pass
# Space: O(n)   — set stores up to n elements
def contains_duplicate(nums: List[int]) -> bool:
    seen: set[int] = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# ── Driver ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))                          # True
    print(contains_duplicate([1, 2, 3, 4]))                          # False
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))     # True
