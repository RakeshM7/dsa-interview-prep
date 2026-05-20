/**
 * Contains Duplicate — JavaScript
 * LeetCode #217 | Easy | Arrays & Hashing
 */

// Brute Force — O(n²) time, O(1) space
function containsDuplicateBrute(nums) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] === nums[j]) return true;
    }
  }
  return false;
}

// Optimal — O(n) time, O(n) space
function containsDuplicate(nums) {
  const seen = new Set();

  for (const num of nums) {
    if (seen.has(num)) return true;
    seen.add(num);
  }

  return false;
}

// Driver
console.log(containsDuplicate([1, 2, 3, 1]));                          // true
console.log(containsDuplicate([1, 2, 3, 4]));                          // false
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));     // true
