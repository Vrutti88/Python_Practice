# Q26) Write a program that calculates the sum of digits of a given integer.
num = int(input("Enter a number: "))
sum=0
while(num!=0):
    rem=num%10
    num=num//10
    sum+=rem
print(sum)
