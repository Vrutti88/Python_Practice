# Q24) Write a simple “guess the number” game. The program randomly generates a number between 1 and 10, and the user has to guess it.
import random
print("Welcome to 'Guess the Number'!")
print("I have selected a number between 1 and 10. Try to guess it.")
number_to_guess = random.randint(1, 10)
while True:
    user_guess = int(input("Enter your guess: "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
        break
