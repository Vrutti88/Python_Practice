# Q79) Write a Python program that reads a file and counts the number of words in it.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
    words = content.split()
    word_count = len(words)
    print(f"The number of words in '{file_name}' is: {word_count}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
