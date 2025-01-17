# Q30) A perfect number is a number that is equal to the sum of its positive divisors (excluding itself). Write a program to check if a number is perfect.
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num // 2 + 1):
    if num % i == 0:  
        sum += i
if sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
