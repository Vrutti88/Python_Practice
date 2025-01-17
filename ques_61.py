# Q61) Write a Python program to sort a dictionary by its values in ascending order.
keys = input("Enter the key: ").split()
values = input("Enter the value: ").split()
dict1 = dict(zip(keys, values))
sort=dict(sorted(dict1.items(),key=lambda item:item[1]))
print("Sorted dictionary in ascending order:", sort)
