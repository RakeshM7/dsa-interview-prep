import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {

    // ── Approach 1: Brute Force ───────────────────────────────────────────────
    // Compare every pair of elements.
    // Time:  O(n²)
    // Space: O(1)
    public boolean containsDuplicateBrute(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }

    // ── Approach 2: HashSet (Optimal) ───────────────────────────────────────────
    // Single pass. If the value is already in the set, we found a duplicate.
    // Otherwise, add it and continue.
    //
    // Time:  O(n)   — one pass through the array
    // Space: O(n)   — HashSet stores up to n elements
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }

        return false;
    }

    // ── Driver ────────────────────────────────────────────────────────────────
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.containsDuplicate(new int[]{1, 2, 3, 1}));                          // true
        System.out.println(sol.containsDuplicate(new int[]{1, 2, 3, 4}));                          // false
        System.out.println(sol.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}));     // true
    }
}
