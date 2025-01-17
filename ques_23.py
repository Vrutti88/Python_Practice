# Q23) Write a program to reverse the digits of a given integer (e.g., 123 -> 321).
num=int(input("Enter a number: "))
rev=0
while (num!=0):
    rem=num%10
    num=num//10
    rev=rev*10+rem
print(f"Number after reversing is: {rev}")
