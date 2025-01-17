# Q25) Write a program that checks if a number is a palindrome (e.g., 121 -> palindrome).
num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
