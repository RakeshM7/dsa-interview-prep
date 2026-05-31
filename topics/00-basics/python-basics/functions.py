def greet(name: str, greeting: str="hello") -> str:
    return f"{greeting}, {name}" 
    # the 'f' before the quotes is to instruct python to embed the variable values into the string that is being printed

print(greet("rakesh"))