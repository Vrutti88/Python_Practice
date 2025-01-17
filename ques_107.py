# Q107) Write a script that reads a JSON file, modifies a value, and writes the updated data back to the file.
import json
filename = "data.json" 
try:
    with open(filename, 'r') as file:
        data = json.load(file)
    if "key_name" in data:
        data["key_name"] = "new_value" 
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("JSON file updated successfully!")
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from the file {filename}.")
