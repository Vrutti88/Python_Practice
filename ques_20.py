# Q20) Write a function that determines whether a number is prime.
n=int(input("Enter a number: "))
for i in range(2,int((n/2)+1)):
    if (n%i==0):
        print(f"{n} is not prime number")
        break
else:
    print(f"{n} is prime number")
