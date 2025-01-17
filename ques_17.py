# Q17) Write a program that calculates the factorial of a given positive integer using a for loop.
num =int(input("Enter your number: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(f"Factorial is: {factorial}")
