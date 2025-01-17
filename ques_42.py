# Q42) Write a program that calculates the sum of all elements in a list.
n=input("Enter a list: ").split()
n=[int(i) for i in n]
result=sum(n)
print(f"Sum if the elements is: {result}")
