# Q31) Implement the Euclidean algorithm to find the GCD (Greatest Common Divisor) of two numbers using a while loop.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if b > a:
    a, b = b, a
# Euclidean algorithm
while b != 0:
    a, b = b, a % b
print(f"The GCD of the given numbers is: {a}")
