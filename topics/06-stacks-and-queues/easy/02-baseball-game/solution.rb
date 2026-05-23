# @param {String[]} operations
# @return {Integer}
def cal_points(operations)
  last_position = operations.length - 1
  output_array = []
  for i in 0..last_position
      current_character = operations[i]
      if current_character == 'C'
          unless output_array.empty?
              output_array.pop()
          end
      elsif current_character == 'D'
          unless output_array.empty?
              output_array << output_array[-1] * 2
          end
      elsif current_character == '+'
          unless output_array.length < 2
              output_array << output_array[-1] + output_array[-2]
          end
      else
          output_array << current_character.to_i
      end
  end
  return output_array.sum
end

def is_digit(character)
  return Integer(character, exception: false)
end