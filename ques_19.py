# Q19)Write a Python program to find the sum of all natural numbers up to a given number n.
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
