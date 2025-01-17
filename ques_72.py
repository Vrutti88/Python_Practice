# Q72) Write a recursive function that returns the number of vowels in a string.
def vowel(s):
    if not s:
        return 0
    vowels = "aeiouAEIOU"
    if s[0] in vowels:
        return 1 + vowel(s[1:])
    else:
        return vowel(s[1:]) 
n = input("Enter a string: ")
result = vowel(n)
print(f"The number of vowels in the string is: {result}")
