def check_if_array_is_sorted(input_arr):
    last_pos = len(input_arr) - 1
    flag = 0
    for i in range(0,last_pos):
        if input_arr[i] > input_arr[i+1]:
            return False
        # print("value of i is :", i)
        i += 1
    return True

if __name__ == "__main__":
    print(check_if_array_is_sorted([1,2,3,4,5,0]))