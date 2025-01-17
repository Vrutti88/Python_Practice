# Q102) Write a function that randomly selects an element from a given list using the random module.
import random
lst = list(map(int, input("Enter a list: ").split()))
result=random.choice(lst)
print(f"Randomly selected element: {result}")
