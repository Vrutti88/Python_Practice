# Q34) Write a function to check if a 3-digit number is an Armstrong number (e.g., 153 -> 1^3 + 5^3 + 3^3 = 153).
num = int(input("Enter a 3-digit number: "))
if sum(int(digit)**3 for digit in str(num))==num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
