# Two Sum — Ruby
# LeetCode #1 | Easy | Arrays & Hashing

# Brute Force — O(n²) time, O(1) space
def two_sum_brute(nums, target)
  nums.each_with_index do |a, i|
    nums.each_with_index do |b, j|
      next if i == j
      return [i, j] if a + b == target
    end
  end
  []
end

# Optimal — O(n) time, O(n) space
def two_sum(nums, target)
  seen = {} # value -> index

  nums.each_with_index do |num, i|
    complement = target - num
    return [seen[complement], i] if seen.key?(complement)
    seen[num] = i
  end

  []
end

# Driver
p two_sum([2, 7, 11, 15], 9)  # [0, 1]
p two_sum([3, 2, 4], 6)       # [1, 2]
p two_sum([3, 3], 6)          # [0, 1]
