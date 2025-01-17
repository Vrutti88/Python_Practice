# Q84) Write a program that appends a user-input line to an existing file without overwriting it.
file_name = input("Enter the file name: ")
line_to_append = input("Enter the line you want to append: ")
try:
    with open(file_name, 'a') as file:
        file.write(line_to_append + "\n")
    print(f"The line has been appended to {file_name}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
