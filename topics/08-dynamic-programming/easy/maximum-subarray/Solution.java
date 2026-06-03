public class Solution {

    // ── Approach 1: Brute Force ───────────────────────────────────────────────
    // Time:  O(n²)
    // Space: O(1)
    public int maxSubarrayBrute(int[] nums) {
        return 0;
    }

    // ── Approach 2: Kadane's Algorithm (Optimal) ─────────────────────────────
    // At each position: extend current subarray or start fresh.
    // current_sum = Math.max(nums[i], current_sum + nums[i])
    //
    // Time:  O(n)
    // Space: O(1)
    public int maxSubarray(int[] nums) {
        return 0;
    }

    // ── Driver ────────────────────────────────────────────────────────────────
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] inputs = {
            {-2, 1, -3, 4, -1, 2, 1, -5, 4},
            {1},
            {5, 4, -1, 7, 8},
            {-1, -2, -3, -4},
            {0, 0, 0},
            {-2, -1},
            {1, 2, 3, 4, 5},
            {3, -1, 2, -1},
        };
        int[] expected = {6, 1, 23, -1, 0, -1, 15, 4};

        for (int i = 0; i < inputs.length; i++) {
            int result = sol.maxSubarray(inputs[i]);
            if (result == expected[i]) {
                System.out.println("Passed");
            } else {
                System.out.printf("[Fail] -> %d (expected %d)%n", result, expected[i]);
            }
        }
    }
}
