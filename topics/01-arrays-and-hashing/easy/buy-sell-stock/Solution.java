public class Solution {

    // ── Approach 1: Brute Force ───────────────────────────────────────────────
    // Time:  O(n²)
    // Space: O(1)
    public int maxProfitBrute(int[] prices) {
        return 0;
    }

    // ── Approach 2: Two Pointers (Optimal) ────────────────────────────────────
    // Time:  O(n)
    // Space: O(1)
    public int maxProfit(int[] prices) {
        return 0;
    }

    // ── Driver ────────────────────────────────────────────────────────────────
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.maxProfit(new int[]{7, 1, 5, 3, 6, 4})); // 5
        System.out.println(sol.maxProfit(new int[]{7, 6, 4, 3, 1}));    // 0
        System.out.println(sol.maxProfit(new int[]{5, 5, 5, 5}));       // 0
    }
}
