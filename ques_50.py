# Q50) Write a function to find the second-largest element in a list.
arr = list(map(int, input("Enter a list of numbers: ").split()))
largest = second = float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(f"The second-largest element is: {second}")
