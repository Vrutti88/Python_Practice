# Q83) Write a program to search for a specific substring in a file and print the lines where it appears.
file_name = input("Enter the file name: ")
substring = input("Enter the substring to search for: ")
try:
    with open(file_name, 'r') as file:
        found = False
        for line_number, line in enumerate(file, start=1):
            if substring in line:
                found = True
                print(f"Line {line_number}: {line.strip()}")
        if not found:
            print(f"The substring '{substring}' was not found in any line of the file.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
