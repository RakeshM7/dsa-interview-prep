# TODO: Implement solution
input_array = ['2', '5', '1', '3', '0', 'a', 'b', 'c']

def is_digit(value)
    return value.match?(/^\d+$/)
end


input_array.each_with_index do |element, index|
    puts "Currently processing: #{element}"
    if is_digit(element)
        puts "Element #{element} at #{index} is a digit"
    else
        puts "Element #{element} at #{index} is a character"
    end
end