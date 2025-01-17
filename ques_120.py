# Q120) Write a script that repeatedly asks the user for a number, catches ValueError if the input is invalid, and stops when a valid number is entered.
while True:
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)
        print(f"You entered the number: {number}")
        break  
    except ValueError:
        print("That's not a valid number. Please try again.")
