# Q40) Write a program to count how many times a specific character appears in a given string.
string = input("Enter a string: ")
char = input("Enter the character to count: ")
if len(char) != 1:
    print("Please enter a single character.")
else:
    count = 0
    for c in string:
        if c == char:
            count += 1
    print(f"The character {char} appears {count} times.")
