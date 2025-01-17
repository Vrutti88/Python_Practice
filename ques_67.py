# Q67) Implement a function fib(n) to return the nth Fibonacci number using recursion.
n=int(input("Enter a number: "))
a,b=0,1
if n==0:
    print(f"fibonacci series of {n} numbers is: 0")
elif n==1:
    print(f"fibonacci series of {n} numbers is: 1")
else:
    print("Fibonacci series:", end=" ")
    while n > 0:
        print(a, end=" ")
        a, b = b, a + b
        n -= 1
