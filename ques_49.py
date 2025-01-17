# Q49) Write a function to rotate a list by k positions to the right. For instance, [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3].
arr = list(map(int, input("Enter a list of numbers: ").split()))
k = int(input("Enter the positions to rotate: "))
k = k % len(arr)
rotated_arr = arr[-k:] + arr[:-k]
print("Rotated list:", rotated_arr)
