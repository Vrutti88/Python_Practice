# Q70) Implement binary search recursively to find an element in a sorted list.
def binary(arr, left, right, target):
    if left > right:
        return -1 
    mid = (left + right) 
    if arr[mid] == target:
        return mid  
    elif arr[mid] > target:
        return binary(arr, left, mid - 1, target)
    else:
        return binary(arr, mid + 1, right, target)
arr = list(map(int, input("Enter a sorted list of elements: ").split()))
target = int(input("Enter the element to search for: "))
result = binary(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
