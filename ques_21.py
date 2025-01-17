# Q21) Write a program that counts the number of vowels in a string.
n=input("Enter a string: ")
vowel="a,e,i,o,u,A,E,I,O,U"
count=0
for i in n:
    if i in vowel:
        count+=1
print("Total vowels = ",count)
