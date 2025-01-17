# Q62) Generate a dictionary that contains numbers (1 to n) as keys and their squares as values.
n=int(input("Enter a number: "))
sq={i:i**2 for i in range(1,n+1)}
print("The numbers and their squares are:")
print(sq)
