# Q5) Write a Python program that asks the user to input a float number, then prints the integer part (truncate), and the fraction part separately.
n1=float(input("Enter a float number: "))
print(f"Integer part is: {int(n1)} and fraction part is: {abs(n1-int(n1))}")
