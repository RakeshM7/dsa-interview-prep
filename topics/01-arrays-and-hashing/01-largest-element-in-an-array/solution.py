def largest_element_sort(input_arr):
    input_arr.sort()

    return input_arr[-1]

def largest_element_traverse(input_arr):
    max_element = input_arr[0]
    for i in range(0, len(input_arr)-1):
        if input_arr[i] > max_element:
            max_element = input_arr[i]
        else:
            max_element = max_element
                
    return max_element

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]

    print("Largest element in the given array :", largest_element_traverse(arr1))
    print("Largest element in the given array :", largest_element_traverse(arr2))