# this is additional content addded via the cat commane
character_variable = 'a'

print("This variable", character_variable, "is of type", type(character_variable))

integer_variable = 1
print("This variable", integer_variable,  "is of type", type(integer_variable))

float_variable = 1.1
print("This variable", float_variable, "is of type", type(float_variable))

list_variable = ["SDET", "QA", "Automation"]
print("This variable", list_variable, "is of type", type(list_variable))

dict_variable = {
    "key1": "value1",
    "key2": 1,
    2: "value3"
}
print("This variable", dict_variable, "is of type", type(dict_variable))
print("Reading from the dictionary")
print("the key is ", dict_variable["key1"])
print("the key is ", dict_variable["key2"])
print("the key is ", dict_variable[2])

# Assign multiple variables at once
character_variable, integer_variable, float_variable, list_variable, dict_variable = 'a', 1, 1.1, ["SDET", "QA", "Automation"], {
    "key1": "value1",
    "key2": 1,
    2: "value3"
}

print("Character variable", character_variable)
print("Integer variable", integer_variable)
print("Float variable", float_variable)
print("list variable", list_variable)
print("Dict variable", dict_variable)


x,y,z = list_variable
print("X:", x, "Y:", y, "Z:", z)

print("------------------------------------------------------")
