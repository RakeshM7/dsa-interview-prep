# Valid Anagram
# LeetCode #242 | Difficulty: Easy | Topic: Arrays & Hashing

class StringBasics

	# Brute force
	def valid_anagram?(string_1, string_2)
		return false if (string_1.length != string_2.length)
		hash_1 = construct_hash_map(string_1)
		hash_2 = construct_hash_map(string_2)
		return hash_1 == hash_2
	end

	private
	def construct_hash_map_complex(input_string)
		result_hash = Hash.new(0)
		for i in 0..input_string.length
			result_hash[input_string[i]] += 1
		end
		return result_hash
	end

	def construct_hash_map(input_string)
		result_hash = Hash.new(0)
		input_string.each_char {|k| result_hash[k] += 1}
		result_hash
	end
end

anagram_validator = StringBasics.new
puts anagram_validator.valid_anagram?("anagram", "nagaram")
puts anagram_validator.valid_anagram?("rat", "car")
puts anagram_validator.valid_anagram?("listen", "silent")
puts anagram_validator.valid_anagram?("hello","world")
puts anagram_validator.valid_anagram?("","")