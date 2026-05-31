# using map method 
multiples_of_two = [x * 2 for x in [1,2,3,4]]
print(f"Multiples of 2 is {multiples_of_two}")

input_variable = [1,3,5,4,23,634,4523,12,1242,23455,2345,1212,4356,23,123412,6234]
print([x for x in input_variable if x > 10])


str_list = ["Rakesh", "Manoharan", "SDET", "QA", "Automation", "SSN", "Freshworks"]

lengths = {word: len(word) for word in str_list}

print(lengths)