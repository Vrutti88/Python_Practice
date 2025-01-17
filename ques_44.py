# Q44) Write a Python function that removes duplicate elements from a list and returns the new list.
n=input("Enter a list: ").split()
n=[int(i) for i in n]
result=list(set(n))
print(f"List after removing the duplicate elements: {result}")
