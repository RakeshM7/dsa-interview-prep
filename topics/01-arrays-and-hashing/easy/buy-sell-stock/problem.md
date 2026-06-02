# Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Topic:** Arrays & Hashing / Two Pointers
**LeetCode:** [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
**Interview Frequency:** Extremely High

---

## Problem Statement

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If no profit is possible, return `0`.

---

## Examples

```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price=1), sell on day 5 (price=6). Profit = 6 - 1 = 5.
```

```
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: Prices only decrease. No transaction gives a profit.
```

```
Input:  prices = [5, 5, 5, 5]
Output: 0
Explanation: All prices equal. No profit possible.
```

---

## Constraints

- `1 <= prices.length <= 100,000`
- `0 <= prices[i] <= 10,000`
- You must buy before you sell — no time travel
- Only one transaction allowed (one buy + one sell)
- If no profit is possible, return `0`

---

## Attempt the problem yourself before opening the solution files.
