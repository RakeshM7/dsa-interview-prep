# LeetCode #20 | Easy | Stacks & Queues
# https://leetcode.com/problems/valid-parentheses/

class StackProcessor
  def validate_parantheses(input_string)
    return true if input_string.empty?
    return false if input_string.nil? || input_string.length == 0 || input_string.length%2 != 0
    storage_stack = []
    possible_combinations = {
      '{' => '}',
      '(' => ')',
      '[' => ']'
    }
    input_string.each_char do |current_char|
      # puts "possible_combinations[current_char] : #{possible_combinations[current_char]}"
      # puts "storage_stack.last : #{storage_stack.last}"
      top_element = storage_stack.last
      expected_closing_bracket = possible_combinations[top_element]
      if !storage_stack.empty? && expected_closing_bracket == current_char
        storage_stack.pop()
      elsif possible_combinations.key?(current_char)
        storage_stack.push(current_char)
      else
        return false
      end
    end
    # puts "Stack content: #{storage_stack}"
    return storage_stack.empty?
  end
end

processor_1 = StackProcessor.new
puts processor_1.validate_parantheses("()") # true
puts processor_1.validate_parantheses("{[]}") # true
puts processor_1.validate_parantheses("") # true
puts processor_1.validate_parantheses("([)]") # false
puts processor_1.validate_parantheses("(]") # false
puts processor_1.validate_parantheses("()[]{}") # true

