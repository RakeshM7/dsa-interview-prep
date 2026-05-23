
class StringProcessor
	def self.return_nr_character(input_string)
		return nil if input_string.nil? || input_string.empty?
	
		result_hash = Hash.new(0)
		input_string.each_char do |char|
			result_hash[char] += 1
		end

		input_string.each_char {|current_char| return current_char if result_hash[current_char] == 1}
		return nil
	end
end

print StringProcessor.return_nr_character("aabbccdxeff")