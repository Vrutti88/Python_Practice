# Q78) Write a Python program to copy the contents of one file to another.
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
try:
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"Content from {source_file} has been copied to {destination_file}.")
except FileNotFoundError:
    print(f"Error: The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
