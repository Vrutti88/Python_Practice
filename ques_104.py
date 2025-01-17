# Q104) Write a program that lists all files and directories in the current directory using os.listdir().
import os
current_directory = os.getcwd()
files_and_dirs = os.listdir(current_directory)
print("Files and directories in the current directory:")
for item in files_and_dirs:
    print(item)
