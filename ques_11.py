# Q11) Write a Python program to calculate compound interest given principal, rate, and time in years.
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter the time period: "))
CI=(p*(1+r/100)**t)-p
print(f"The Compound Interest is: {CI}")
