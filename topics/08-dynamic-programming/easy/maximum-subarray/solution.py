"""
Maximum Subarray
LeetCode #53 | Difficulty: Easy | Topic: Dynamic Programming / Greedy
"""

from typing import List


# ── Approach 1: Brute Force ───────────────────────────────────────────────────
# Time:  O(n²)
# Space: O(1)
def max_subarray_brute(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    max_sum = float('-inf')
    for i in range(0, len(nums)):
        i_sum = 0
        for j in range(i, len(nums)):
            i_sum += nums[j]
            if i_sum > max_sum:
                max_sum = i_sum
            # print(f"Current i_sum : {i_sum}")
    return max_sum



        



# ── Approach 2: Kadane's Algorithm (Optimal) ─────────────────────────────────
# At each position, decide: extend the current subarray or start fresh.
# current_sum = max(nums[i], current_sum + nums[i])
#
# Time:  O(n)   — single pass
# Space: O(1)   — two variables
def max_subarray_kadanes(nums: List[int]) -> int:
    max_sum = float('-inf')
    if len(nums) == 1:
        return nums[0]
    current_sum = 0
    for i in range(0, len(nums)):
        current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

        


# ── Driver ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),   # [4, -1, 2, 1]
        ([1], 1),                                  # single element
        ([5, 4, -1, 7, 8], 23),                   # entire array
        ([-1, -2, -3, -4], -1),                   # all negative
        ([0, 0, 0], 0),                            # all zeros
        ([-2, -1], -1),                            # two negatives, return least
        ([1, 2, 3, 4, 5], 15),                    # strictly increasing
        ([3, -1, 2, -1], 4),                      # [3, -1, 2]
    ]

    for nums, expected in test_cases:
        result = max_subarray_kadanes(nums)
        if result == expected:
            print("Passed")
        else:
            print(f"[Fail] nums={nums} -> {result} (expected {expected})")
