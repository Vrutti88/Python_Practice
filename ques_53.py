# Q53) Write a program to remove all even numbers from a list of integers.
arr = list(map(int, input("Enter a list of numbers: ").split()))
result=[num for num in arr if num%2!=0]
print(f"List after removing even numbers is: {result}")
