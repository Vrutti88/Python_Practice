# Q22) Print the first n numbers of the Fibonacci sequence using a for loop.
n=int(input("Enter a number: "))
a,b=0,1
for i in range (n):
    print(a,end=" ")
    a,b=b,a+b
