# Contains Duplicate
# LeetCode #217 | Difficulty: Easy | Topic: Arrays & Hashing

class HashBasics
  def contains_duplicates?(input_array)
    result_hash = Hash.new(0)
    input_array.each do |item|
      if result_hash[item] > 1
        return true
      else
        result_hash[item] += 1
      end
    end
  end
end

dup_processor = HashBasics.new
puts dup_processor.contains_duplicates?([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
puts dup_processor.contains_duplicates?([1, 2, 3, 4, 5, 6, 7, 8, 9, 12])

