# Q76) Write a Python script that reads a text file and prints its contents.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
