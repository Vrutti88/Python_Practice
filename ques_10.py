# Q10) Write a Python program that calculates simple interest. Prompt for principal, rate, and time, then compute the interest.
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter the time period: "))
SI=(p*r*t)/100
print(f"The Simple Interest is: {SI}")
