# Q75) Write a recursive function to compute the Greatest Common Divisor (GCD) of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = gcd(a, b)
print(f"The GCD of {a} and {b} is: {result}")
