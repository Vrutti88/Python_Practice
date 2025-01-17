# Q38) Print a diamond-shaped pattern of stars with a width given by the user (e.g., for 5).
Input: Get the width of the diamond (must be odd)
n = int(input("Enter an odd number for the diamond's width: "))
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)
for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)
