# Q81) Modify the file-reading program to handle exceptions (e.g., file not found) gracefully.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
    line_count = len(lines)
    print(f"The number of lines in '{file_name}' is: {line_count}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
