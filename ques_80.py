# Q80) Write a program that counts how many lines are in a file.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
    line_count = len(lines)
    print(f"The number of lines in '{file_name}' is: {line_count}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
