# Q45) Implement a linear search to find a given element in a list. Return the index if found, or -1 otherwise.
n=input("Enter a list: ").split()
search=int(input("Enter the element to be searched: "))
n=[int(i) for i in n]
for index in range(len(n)):
    if (search==n[index]):
        print(f"Element is found at index: {index}")
        break
else:
    print("Element is found at index: -1")
