# Q63) Write a Python program to perform union, intersection, and difference operations on two sets.
set1 = set(map(int, input("Enter elements for set1: ").split()))
set2 = set(map(int, input("Enter elements for set2: ").split()))
union = set1 | set2 
intersection = set1 & set2  
difference1 = set1 - set2 
difference2 = set2 - set1 
print(f"Union of set1 and set2: {union}")
print(f"Intersection of set1 and set2: {intersection}")
print(f"Difference of set1 and set2: {difference1}")
print(f"Difference of set2 and set1: {difference2}")
