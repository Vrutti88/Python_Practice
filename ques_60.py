# Q60) Write a function to merge two dictionaries. If a key appears in both, add their values.
keys1 = input("Enter the key: ").split()
values1 = input("Enter the value: ").split()
dict1 = dict(zip(keys1, values1))
keys2 = input("Enter the key: ").split()
values2 = input("Enter the value: ").split()
dict2 = dict(zip(keys2, values2))
add=dict1.copy()
for key, value in dict2.items():
    if key in add:
        add[key]+=value
    else:
        add[key]=value
print("Merged Dictionary:", add)
