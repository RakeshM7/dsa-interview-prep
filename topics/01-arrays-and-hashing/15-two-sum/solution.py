# two sum

# Given: nums = [2, 7, 11, 15], target = 9
# Return: [0, 1]  ← indices of the two numbers that add up to 9


tests = [
    # basic case
    {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},

    # pair at the end
    {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},

    # duplicate values
    {"nums": [3, 3], "target": 6, "expected": [0, 1]},

    # includes zero
    {"nums": [0, 4, 3, 0], "target": 0, "expected": [0, 3]},

    # includes negatives
    {"nums": [-1, -2, -3, -4, -5], "target": -8, "expected": [2, 4]},

    # positive + negative
    {"nums": [-3, 4, 3, 90], "target": 0, "expected": [0, 2]},

    # larger numbers
    {"nums": [1000000, 2500000, 3000000, 7500000], "target": 4000000, "expected": [0, 2]},

    # repeated numbers but only one valid pair
    {"nums": [1, 5, 1, 5], "target": 10, "expected": [1, 3]},

    # pair not adjacent
    {"nums": [8, 1, 6, 2, 9], "target": 10, "expected": [0, 3]},

    # target from two middle elements
    {"nums": [10, 20, 30, 40, 50], "target": 70, "expected": [2, 3]},
]



# nums = input("Enter the numbers: ")
# target = input("Enter the target: ")
def two_sum(nums, target):
    tracker = {}
    for index,value in enumerate(nums):
        if (target - value) in tracker.keys():
            return [tracker[target-value], index]
        else:
            tracker[value] = index

for current_test_case in tests:
    two_sum_result = two_sum(current_test_case["nums"], current_test_case["target"])
    print(f"Test case {current_test_case['nums']} and target: {current_test_case['target']} result: {two_sum_result}")
    if two_sum_result == current_test_case["expected"]:
        print("Test case passed")
    else:
        print(f"Test case failed for input: {current_test_case['nums']} and target: {current_test_case['target']}")
        print(f"Expected: {current_test_case['expected']}")
        print(f"Actual: {two_sum_result}")

