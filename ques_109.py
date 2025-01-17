# Q109) Write a script that extracts all email addresses from a given string using the re module.
import re
text = "Please contact us at support@example.com or sales@mycompany.org for more info."
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_addresses = re.findall(email_pattern, text)
print("Extracted email addresses:", email_addresses)
