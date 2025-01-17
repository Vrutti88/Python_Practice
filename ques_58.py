# Q58) Write a function that inverts a dictionary (keys become values, values become keys).
keys = input("Enter the first list: ").split()
values = input("Enter the second list: ").split()
if len(keys) != len(values):
    print("Error: Both lists must have the same length.")
else:
    result_dict = dict(zip(keys, values))
    inverted_dict = {value: key for key, value in result_dict.items()}
    print("Resulting dictionary:", inverted_dict)
