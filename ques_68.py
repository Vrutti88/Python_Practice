# Q68) Write a recursive function power(base, exp) that computes base^exp.
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = 1
while exp > 0:
    result *= base
    exp -= 1
print(f"The result of {base}^exp is: {result}")
