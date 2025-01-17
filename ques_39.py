# Q39) Print the numbers from 1 to n. For multiples of 3, print “Fizz” instead of the number; for multiples of 5, print “Buzz”; for multiples of both 3 and 5, print “FizzBuzz”.
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if (i%3==0 and i%5==0):
        print("FizzBuzz")
    elif (i%3==0):
        print("Fizz")
    elif (i%5==0):
        print("Buzz")
    else:
        print(i)
