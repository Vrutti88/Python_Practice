# Q57) Write a program that counts the frequency of each element in a list using a dictionary.
arr = input("Enter the elements of the list: ").split()
frequency = {}
for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("Frequency of each element:", frequency)
