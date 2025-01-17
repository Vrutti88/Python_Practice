# Q36) Write a program that generates all prime numbers in a given range [start, end].
start= int(input("Enter the first number: "))
end= int(input("Enter the end number: "))
for i in range(start, end + 1):
    for j in range(2, int((i / 2) + 1)):
        if i%j == 0:
            break
    else:
        print(i)
