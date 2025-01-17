# Q37) Write a program that displays the Collatz sequence for any positive integer given by the user.
Input: Get a positive integer from the user
n = int(input("Enter a positive integer: "))
while n != 1:
    print(n, end=" -> ") 
    if n % 2 == 0: 
        n //= 2
    else: 
        n = 3 * n + 1
print(1) 
