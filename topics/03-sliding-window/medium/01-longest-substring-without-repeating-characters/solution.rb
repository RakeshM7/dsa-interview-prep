# LeetCode #3 | Medium | Sliding Window
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class SlidingWindowProcessor
  def longest_substring_length(input_string)
    result_max_substring = ""
    input_last_position = input_string.length - 1
    for i in 0..input_last_position - 1
      current_hash = Hash.new(0)
      current_max_string = ""
      for j in i..input_last_position
        if current_hash[input_string[j]] > 0
          break
        else
          current_max_string += input_string[j]
          current_hash[input_string[j]] += 1
        end
      end
      if current_max_string.length > result_max_substring.length
        result_max_substring = current_max_string
      end
    end
    print "result_max_substring : #{result_max_substring}"
    return result_max_substring.length
  end
end

processor = SlidingWindowProcessor.new
puts processor.longest_substring_length("abcabcbb") # 3
puts processor.longest_substring_length("bbbbb")    # 1
puts processor.longest_substring_length("pwwkew")   # 3
puts processor.longest_substring_length("")         # 0
puts processor.longest_substring_length("dvdf")     # 3