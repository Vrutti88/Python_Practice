# Q56) Given two lists of the same length, create a dictionary mapping elements of one list to the corresponding elements of the other.
keys = input("Enter the first list: ").split()
values = input("Enter the second list: ").split()
if len(keys) != len(values):
    print("Error: Both lists must have the same length.")
else:
    result_dict = dict(zip(keys, values))
    print("Resulting dictionary:", result_dict)
