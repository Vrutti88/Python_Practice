# Q66) Implement a function factorial(n) that calculates n! using recursion.
n=int(input("Enter a number: "))
fact=1
if n==0 or n==1:
    print("The factorial is: 1")
else:
    for i in range(1, n + 1):
        fact *= i
print("The fatorial is: ",fact)
