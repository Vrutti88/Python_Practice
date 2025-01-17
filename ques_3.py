# Q3) Write a Python program that prompts the user for two numbers and prints their sum, difference, product, and quotient.
num1=float(input("Enter a first number: "))
num2=float(input("Enter a second number: "))
print(f"Sum of {num1} and {num2} is: {num1+num2}")
print(f"Difference of {num1} and {num2} is: {num1-num2}")
print(f"Product of {num1} and {num2} is: {num1*num2}")
if (num2!=0):
    print(f"Quotient of {num1} and {num2} is: {num1/num2}")
else:
    print("Error!! Cannot divide by zero")
