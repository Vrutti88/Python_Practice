# Q46) Implement the bubble sort algorithm to sort a list in ascending order.
arr = list(map(int, input("Enter a list of numbers: ").split()))
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted list in ascending order:", arr)
