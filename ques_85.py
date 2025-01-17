# Q85) Write a Python script to read a CSV file and print each row.
import csv
file_name = input("Enter the CSV file name: ")
try:
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
