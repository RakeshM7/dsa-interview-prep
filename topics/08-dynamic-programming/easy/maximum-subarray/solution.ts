/**
 * Maximum Subarray — TypeScript
 * LeetCode #53 | Easy | Dynamic Programming / Greedy
 */

// Brute Force — O(n²) time, O(1) space
function maxSubarrayBrute(nums: number[]): number {
  return 0;
}

// Kadane's Algorithm (Optimal) — O(n) time, O(1) space
function maxSubarray(nums: number[]): number {
  return 0;
}

// Driver
const testCases: [number[], number][] = [
  [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
  [[1], 1],
  [[5, 4, -1, 7, 8], 23],
  [[-1, -2, -3, -4], -1],
  [[0, 0, 0], 0],
  [[-2, -1], -1],
  [[1, 2, 3, 4, 5], 15],
  [[3, -1, 2, -1], 4],
];

testCases.forEach(([nums, expected]) => {
  const result = maxSubarray(nums);
  if (result === expected) {
    console.log("Passed");
  } else {
    console.log(`[Fail] nums=${JSON.stringify(nums)} -> ${result} (expected ${expected})`);
  }
});
