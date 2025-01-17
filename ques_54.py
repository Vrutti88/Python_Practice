# Q54) Write a program to shuffle a list in-place (you can use random.shuffle or implement your own shuffling algorithm).
import random
arr = list(map(int, input("Enter a list of numbers: ").split()))
random.shuffle(arr)
print(arr)
