# Q6) Write a Python function that takes a string and returns its length without using the built-in len() function.
n=input("Enter a string: ")
count=0
index=0
while index<len(n):
    count+=1
    index+=1
print(f"The length of the string is: {count}")
