# Q16) Write a program to display the multiplication table of a given integer up to 10.
n=int(input("Enter a number: "))
for i in range (1,11):
    prod=n*i
    print(f"{n} * {i} = {prod}")
