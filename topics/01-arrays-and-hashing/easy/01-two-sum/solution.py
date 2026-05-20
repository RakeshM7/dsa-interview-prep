"""
Two Sum
LeetCode #1 | Difficulty: Easy | Topic: Arrays & Hashing
"""

from typing import List


# ── Approach 1: Brute Force ───────────────────────────────────────────────────
# Time:  O(n²)
# Space: O(1)
def two_sum_brute(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ── Approach 2: HashMap (Optimal) ─────────────────────────────────────────────
# For each element, calculate its complement (target - num).
# If the complement is already in the dict, we have our answer.
# Otherwise, store the current value and its index.
#
# Time:  O(n)   — single pass
# Space: O(n)   — dict stores up to n elements
def two_sum(nums: List[int], target: int) -> List[int]:
    seen: dict[int, int] = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []  # guaranteed to find a solution


# ── Driver ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))       # [1, 2]
    print(two_sum([3, 3], 6))          # [0, 1]
