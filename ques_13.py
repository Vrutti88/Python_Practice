# Q13) Write a Python program to convert a temperature from Celsius to Fahrenheit and vice versa.
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is equal to {fahrenheit}F.")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}F is equal to {celsius}C.")
else:
    print("Invalid choice! Please enter 1 or 2.")
