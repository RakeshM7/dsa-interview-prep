def sort_and_remove_dup(input_array: list) -> list:
    result = []
    
    for i in range(0, len(input_array)):
        i_min_element = float('inf')
        for j in range(0, len(input_array)):
            if result and input_array[j] <= result[-1]:
                continue
            if input_array[j] < i_min_element:
                i_min_element = input_array[j]
        if i_min_element == float('inf'):
            break
        result.append(i_min_element)
    return result

def run_test(input_array: list, expected_output: list) -> None:
    actual_output = sort_and_remove_dup(input_array)
    if actual_output == expected_output:
        print(f"[PASSED]")
    else:
        print(f"[FAILED] Expected: {expected_output} / Actual: {actual_output}")

if __name__ == "__main__":
    run_test([4, 2, 4, 1, 3, 2], [1, 2, 3, 4])
    run_test([5, 5, 5, 5], [5])
    run_test([-1, 3, -1, 2, 3, 0], [-1, 0, 2, 3])
    run_test([], [])
    run_test([7], [7])