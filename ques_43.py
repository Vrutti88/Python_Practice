# Q43) Write a function that returns the largest and the smallest elements in a given list.
n=input("Enter a list: ").split()
n=[int(i) for i in n]
print(f"The largest elemennt is: {max(n)}")
print(f"The smallest elemennt is: {min(n)}")
