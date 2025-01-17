# Q51) Write a function that merges two sorted lists into one sorted list.
l1 = list(map(int, input("Enter the first sorted list: ").split()))
l2 = list(map(int, input("Enter the second sorted list: ").split()))
merged = []
i = j = 0
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        merged.append(l1[i])
        i += 1
    else:
        merged.append(l2[j])
        j += 1
while i < len(l1):
    merged.append(l1[i])
    i += 1
while j < len(l2):
    merged.append(l2[j])
    j += 1
print("Merged sorted list:", merged)
