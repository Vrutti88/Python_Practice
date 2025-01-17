# Q101) Write a script that uses the math module to compute the square root, floor, and ceiling of a user-input number.
import math
number = float(input("Enter a number: "))
sq = math.sqrt(number)
flr = math.floor(number)
cei = math.ceil(number)
print(f"The square root of {number} is: {sq}")
print(f"The floor value of {number} is: {flr}")
print(f"The ceiling value of {number} is: {cei}")
