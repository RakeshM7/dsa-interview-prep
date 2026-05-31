def print_demo():
    print("1. before yield")
    yield "first"
    print("2. between yields")
    yield "two"
    print("3. after last yield")

gen = print_demo()
for i in range(2):
    print(next(gen))
