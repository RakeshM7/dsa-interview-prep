user_input = [2, 5, 1, 3, 0, 700]

def get_max_element(input_array)
    max_element = input_array.first
    for i in 0..(input_array.length - 1) do 
        if input_array[i] >= max_element
            max_element = input_array[i]
        end
    end

    return max_element
end

print get_max_element(user_input)
