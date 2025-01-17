# Q106) Write a script that takes command-line arguments and prints them.
import sys
print("Command-line arguments:", sys.argv)
print("Arguments without the script name:")
for arg in sys.argv[1:]:
    print(arg)
