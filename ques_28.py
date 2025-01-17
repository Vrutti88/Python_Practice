# Q28) Write a program that prints numbers from 1 to 10, but skip multiples of 3 using continue, and stop completely if the number is 9 using break.
for i in range(1,11):
    if (i%3==0):
        continue
    if (i==9):
        break
    else:
        print(i)
