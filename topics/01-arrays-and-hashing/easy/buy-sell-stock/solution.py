"""
Best Time to Buy and Sell Stock
LeetCode #121 | Difficulty: Easy | Topic: Arrays & Hashing / Two Pointers
"""

from typing import List


# ── Approach 1: Brute Force ───────────────────────────────────────────────────
# Time:  O(n²)
# Space: O(1)
def max_profit_brute(prices: List[int]) -> int:
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                current_profit = prices[j] - prices[i]
                if current_profit > max_profit:
                    max_profit = current_profit
    return max_profit


# ── Approach 2: Two Pointers (Optimal) ───────────────────────────────────────
# Time:  O(n)
# Space: O(1)
def max_profit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0
    
    max_profit = 0
    left_ptr, right_ptr = 0, 1
    # while prices[right_ptr] < prices[left_ptr]:
    #     left_ptr +=1
    # right_ptr = left_ptr+1
    while right_ptr < len(prices):
        if prices[right_ptr] - prices[left_ptr] > max_profit:
            max_profit = prices[right_ptr] - prices[left_ptr]
        if prices[right_ptr] <= prices[left_ptr]:
            left_ptr = right_ptr
        right_ptr += 1
    return max_profit
        

        



# ── Driver ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),       # buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),          # strictly decreasing
        ([5, 5, 5, 5], 0),             # all prices equal
        ([1, 2, 3, 4, 5], 4),          # strictly increasing
        ([1], 0),                      # only one day
        ([], 0),                       # no prices
        ([2, 4, 1], 2),                # best sale before final drop
        ([3, 2, 6, 5, 0, 3], 4),       # best profit occurs before later minimum
        ([2, 1, 2, 1, 0, 1, 2], 2),    # repeated valleys and peaks
        ([10, 1, 2, 11], 10),          # maximum profit at the end
        ([6, 1, 3, 2, 4, 7], 6),       # multiple possible profitable windows
        ([0, 0, 5, 0, 10], 10),        # zero price edge case
    ]

    for prices, expected in test_cases:
        result = max_profit(prices)
        if result == expected:
            print("Passed")
        else:
            print(f"[Fail] prices={prices} -> {result} (expected {expected})")

