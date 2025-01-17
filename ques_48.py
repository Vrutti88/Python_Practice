# Q48) Write a Python program that counts the number of times a given element appears in a list.
arr = list(map(int, input("Enter a list of numbers: ").split()))
element = int(input("Enter the element to be counted: "))
count = arr.count(element)
print(f"The element {element} appears {count} time3 in the list.")
