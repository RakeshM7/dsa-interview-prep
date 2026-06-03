# Maximum Subarray
# LeetCode #53 | Difficulty: Easy | Topic: Dynamic Programming / Greedy

# Brute Force — O(n²) time, O(1) space
def max_subarray_brute(nums)
end

# Kadane's Algorithm (Optimal) — O(n) time, O(1) space
def max_subarray(nums)
end

# Driver
test_cases = [
  [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
  [[1], 1],
  [[5, 4, -1, 7, 8], 23],
  [[-1, -2, -3, -4], -1],
  [[0, 0, 0], 0],
  [[-2, -1], -1],
  [[1, 2, 3, 4, 5], 15],
  [[3, -1, 2, -1], 4],
]

test_cases.each do |nums, expected|
  result = max_subarray(nums)
  if result == expected
    puts "Passed"
  else
    puts "[Fail] nums=#{nums} -> #{result} (expected #{expected})"
  end
end
