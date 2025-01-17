# Q32) Write a Python function to compute the LCM (Least Common Multiple) of two numbers, leveraging the GCD.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
