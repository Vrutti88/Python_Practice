# Q47) Write a program to reverse a list in-place (without using reversed() or slicing).
arr = list(map(int, input("Enter a list of numbers: ").split()))
n = len(arr)
left=0
right=len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print("Reversed list:", arr)
