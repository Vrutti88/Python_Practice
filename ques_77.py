# Q77) Write a program that prompts the user for a line of text and writes that line to a file.
text = input("Enter a line of text: ")
file_name = input("Enter the filename to save the text: ")
try:
    with open(file_name, 'w') as file:
        file.write(text)
    print(f"Text has been written to {file_name}")
except Exception as e:
    print(f"An error occurred: {e}")
