# Vaidate parantheses problem

# Given: s = "()"
# Return: true

# Given: s = "()[]{}"
# Return: true

# Given: s = "(]"
# Return: false

# Given: s = "([)]"
# Return: false

tests = [
    {"s": "", "expected": True},              # empty string

    {"s": "()", "expected": True},            # single valid pair

    {"s": "()[]{}", "expected": True},        # multiple valid pairs

    {"s": "({[]})", "expected": True},        # nested valid pairs

    {"s": "(]", "expected": False},           # wrong closing bracket

    {"s": "([)]", "expected": False},         # incorrect nesting order

    {"s": "(", "expected": False},            # unclosed opening bracket

    {"s": "]", "expected": False},            # closing bracket without opening

    {"s": "((()))", "expected": True},        # deeply nested same bracket type

    {"s": "({[)]}", "expected": False},       # mixed brackets with bad nesting
]

def validate_paranteses(input_array: list[int]):
    stack_store = []
    parantheses_mapping = {
        "}": "{",
        ')': "(",
        "]": "["
    }

    if len(input_array) == 0:
        return True

    for bracket in input_array:
        if bracket in parantheses_mapping.keys():
            if len(stack_store) == 0:
                return False # if stack is empty and it is a closing bracket, then return false straightaway
            elif stack_store[-1] == parantheses_mapping[bracket]:
                stack_store.pop()
        else:
            stack_store.append(bracket)
    
    return len(stack_store)==0
            

for current_test in tests:
    result = validate_paranteses(current_test["s"])
    if result == current_test["expected"]:
        print("Testcase passed")
    else:
        print("Testcase failed for input: ", current_test["s"], "expected output: ", current_test["expected"], "actual output: ", result)    

        