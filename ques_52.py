# Q52) Given a list, write a Python function to find all duplicate elements.
arr = list(map(int, input("Enter a list of numbers: ").split()))
element_count = {}
duplicates = []
for elem in arr:
    if elem in element_count:
        element_count[elem] += 1
    else:
        element_count[elem] = 1
for elem, count in element_count.items():
    if count > 1:
        duplicates.append(elem)
print("Duplicate elements are:", duplicates)
