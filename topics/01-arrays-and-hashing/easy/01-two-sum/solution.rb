#REF: https://www.youtube.com/watch?v=KLlXCFG5TnA

class ArrayBasics
  def two_sum_brute(input_array, target_sum)
    array_last_index = input_array.length-1
    for i in 0...array_last_index do
      for j in i+1..array_last_index do
        if (input_array[i] + input_array[j]) ==  target_sum
          return [i,j]
        end
      end
    end
  end

  def two_sum_optimised(input_array, target_sum)
    array_map = {}
    array_last_index = input_array.length - 1
    for i in 0..array_last_index do
      # print "Array map : #{array_map}\n"
      difference = target_sum - input_array[i]
      if array_map[difference]
        return [array_map[difference], i]
      else
        array_map[input_array[i]] = i
      end
    end
  end
end


array_obj = ArrayBasics.new

print array_obj.two_sum_optimised([2, 7, 11, 15], 9) # [0, 1]
print array_obj.two_sum_optimised([3, 2, 4], 6) # [1, 2]
print array_obj.two_sum_optimised([3, 3], 6) # [0, 1]