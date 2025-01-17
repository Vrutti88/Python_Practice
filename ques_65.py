# Q65) Given two lists, write a program to find the common elements using sets.
set1 = set(map(int, input("Enter elements for set1: ").split()))
set2 = set(map(int, input("Enter elements for set2: ").split()))
common=set1&set2
print(f"Common elements are: {common}")
