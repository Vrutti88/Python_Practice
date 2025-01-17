# Q29) Write a Python script to print the multiplication table for numbers 1 through 5 (using nested loops).
for i in range(1,6):
    print(f"Multiplication table of {i}:-")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
