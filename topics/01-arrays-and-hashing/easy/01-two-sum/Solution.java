import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Solution {

    // ── Approach 1: Brute Force ───────────────────────────────────────────────
    // Check every pair of elements.
    // Time:  O(n²)
    // Space: O(1)
    public int[] twoSumBrute(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }

    // ── Approach 2: HashMap (Optimal) ─────────────────────────────────────────
    // For each element, check if its complement (target - num) already exists
    // in the map. If yes, we have our pair. If no, store the current element.
    //
    // Key insight: we do not need two passes. A single pass works because
    // we are looking for a pair — if A needs B, then when we process B,
    // A is already in the map.
    //
    // Time:  O(n)   — one pass through the array
    // Space: O(n)   — HashMap stores up to n elements
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>(); // value → index

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }

            seen.put(nums[i], i);
        }

        return new int[]{}; // guaranteed to find a solution per problem constraints
    }

    // ── Driver ────────────────────────────────────────────────────────────────
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(Arrays.toString(sol.twoSum(new int[]{2, 7, 11, 15}, 9)));  // [0, 1]
        System.out.println(Arrays.toString(sol.twoSum(new int[]{3, 2, 4}, 6)));       // [1, 2]
        System.out.println(Arrays.toString(sol.twoSum(new int[]{3, 3}, 6)));          // [0, 1]
    }
}
