# Q103) Write a script that gets the current date and time and formats it as YYYY-MM-DD HH:MM:SS.
import time
current = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", current)
print("Current Date and Time:", formatted)
