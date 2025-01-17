# Q4) Write a Python program that swaps the values of two variables without using a temporary variable.
n1=int(input("Enter first integer: "))
n2=int(input("Enter second integer: "))
print("Before swapping:-")
print(f"{n1} {n2}")
n1,n2=n2,n1
print("After swapping:-")
print(f"{n1} {n2}")
