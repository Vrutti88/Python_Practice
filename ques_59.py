# Q59) Write a program to check if a given key exists in a dictionary.
keys = input("Enter the key: ").split()
values = input("Enter the value: ").split()
dict = dict(zip(keys, values))
check = input("Enter the key to check: ")
if check in keys:
    print(f"The key {check} exists in the dictionary.")
else:
    print(f"The key {check} do not exists in the dictionary.")
