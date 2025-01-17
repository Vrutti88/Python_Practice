# Q82) Write a program that finds the longest word in a text file and prints it.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
    words = content.split()
    longest_word = max(words, key=len)
    print(f"The longest word in the file is: {longest_word}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
