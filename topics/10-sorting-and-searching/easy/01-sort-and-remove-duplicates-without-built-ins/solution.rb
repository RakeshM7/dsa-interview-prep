def sift_down(arr, heap_size, root)
  loop do
    largest = root
    left = 2 * root + 1
    right = left + 1

    largest = left if left < heap_size && arr[left] > arr[largest]
    largest = right if right < heap_size && arr[right] > arr[largest]
    return if largest == root

    temporary = arr[root]
    arr[root] = arr[largest]
    arr[largest] = temporary
    root = largest
  end
end

def heap_sort(arr)
  root = arr.length / 2 - 1
  while root >= 0
    sift_down(arr, arr.length, root)
    root -= 1
  end

  ending = arr.length - 1
  while ending > 0
    temporary = arr[0]
    arr[0] = arr[ending]
    arr[ending] = temporary
    sift_down(arr, ending, 0)
    ending -= 1
  end
end

def sort_and_remove_duplicates(arr)
  return 0 if arr.empty?

  heap_sort(arr)
  write = 1
  read = 1

  while read < arr.length
    if arr[read] != arr[write - 1]
      arr[write] = arr[read]
      write += 1
    end
    read += 1
  end

  write
end

def distinct_values(arr, count)
  result = []
  index = 0
  while index < count
    result[result.length] = arr[index]
    index += 1
  end
  result
end

tests = [
  [4, 2, 4, 1, 3, 2],
  [5, 5, 5, 5],
  [-1, 3, -1, 2, 3, 0],
  [],
  [7]
]

tests.each do |values|
  count = sort_and_remove_duplicates(values)
  p distinct_values(values, count)
end
