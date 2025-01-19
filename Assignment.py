# Q1) Write a Python program to print “Hello, World!”.
print("Hello, World!")


# Q2) Write a Python program that takes a user’s name and prints a greeting with that name in uppercase and lowercase.
name=input("Enter you name: ")
print(f"Hello, {name.upper()}!")
print(f"Hello, {name.lower()}!")



# Q3) Write a Python program that prompts the user for two numbers and prints their sum, difference, product, and quotient.
num1=float(input("Enter a first number: "))
num2=float(input("Enter a second number: "))
print(f"Sum of {num1} and {num2} is: {num1+num2}")
print(f"Difference of {num1} and {num2} is: {num1-num2}")
print(f"Product of {num1} and {num2} is: {num1*num2}")
if (num2!=0):
    print(f"Quotient of {num1} and {num2} is: {num1/num2}")
else:
    print("Error!! Cannot divide by zero")


# Q4) Write a Python program that swaps the values of two variables without using a temporary variable.
n1=int(input("Enter first integer: "))
n2=int(input("Enter second integer: "))
print("Before swapping:-")
print(f"{n1} {n2}")
n1,n2=n2,n1
print("After swapping:-")
print(f"{n1} {n2}")


# Q5) Write a Python program that asks the user to input a float number, then prints the integer part (truncate), and the fraction part separately.
n1=float(input("Enter a float number: "))
print(f"Integer part is: {int(n1)} and fraction part is: {n1-int(n1)}")


# Q6) Write a Python function that takes a string and returns its length without using the built-in len() function.
n=input("Enter a string: ")
count=0
index=0
while index<len(n):
    count+=1
    index+=1
print(f"The length of the string is: {count}")


# Q7) Write a Python program that determines if a given number is even or odd.
num =int(input("Enter your number: "))
if (num%2==0):
    print("The number is even!")
else:
    print("The number is odd!")


# Q8) Write a Python program that takes three numbers and prints the largest and the smallest numbers 
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
print(f"The largest number is: {max(n1,n2,n3)}")
print(f"The smallest number is: {min(n1,n2,n3)}")


# Q9) Write a Python program that converts miles to kilometers. Take miles as user input.
miles=float(input("Enter a number: "))
km=miles*1.6
print(f"{miles} miles = {km} kilometers")


# Q10) Write a Python program that calculates simple interest. Prompt for principal, rate, and time, then compute the interest.
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter the time period: "))
SI=(p*r*t)/100
print(f"The Simple Interest is: {SI}")


# Q11) Write a Python program to calculate compound interest given principal, rate, and time in years.
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter the time period: "))
CI=(p*(1+r/100)**t)-p
print(f"The Compound Interest is: {CI}")


# Q12)Write a program that checks if a given year is a leap year.
year = int(input("Enter a year: "))
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Q13) Write a Python program to convert a temperature from Celsius to Fahrenheit and vice versa.
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is equal to {fahrenheit}F.")
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}F is equal to {celsius}C.")
else:
    print("Invalid choice! Please enter 1 or 2.")


# Q14) Write a function that takes a string s and an integer n, and returns the string repeated n times.
s=input("Enter a string: ")
n=int(input("Enter a number: "))
print(f"After repetition:{s * n}")


# Q15) Write a Python program to round a float to 2 decimal places without using the built-in round() function.
n=float(input("Enter a float number: "))
print(f"The number upto 2 decimal places is: {n:.2f}")


# Q16) Write a program to display the multiplication table of a given integer up to 10.
n=int(input("Enter a number: "))
for i in range (1,11):
    prod=n*i
    print(f"{n} * {i} = {prod}")


# Q17) Write a program that calculates the factorial of a given positive integer using a for loop.
num =int(input("Enter your number: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(f"Factorial is: {factorial}")


# Q18) Write a program using a while loop that prints numbers from 1 to 10.
num=0
while(num<11):
    num+=1
    print(num)


# Q19)Write a Python program to find the sum of all natural numbers up to a given number n.
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)


# Q20) Write a function that determines whether a number is prime.
n=int(input("Enter a number: "))
for i in range(2,int((n/2)+1)):
    if (n%i==0):
        print(f"{n} is not prime number")
        break
else:
    print(f"{n} is prime number")


# Q21) Write a program that counts the number of vowels in a string.
n=input("Enter a string: ")
vowel="a,e,i,o,u,A,E,I,O,U"
count=0
for i in n:
    if i in vowel:
        count+=1
print("Total vowels = ",count)


# Q22) Print the first n numbers of the Fibonacci sequence using a for loop.
n=int(input("Enter a number: "))
a,b=0,1
for i in range (n):
    print(a,end=" ")
    a,b=b,a+b


# Q23) Write a program to reverse the digits of a given integer (e.g., 123 -> 321).
num=int(input("Enter a number: "))
rev=0
while (num!=0):
    rem=num%10
    num=num//10
    rev=rev*10+rem
print(f"Number after reversing is: {rev}")


# Q24) Write a simple “guess the number” game. The program randomly generates a number between 1 and 10, and the user has to guess it.
import random
number_to_guess = random.randint(1, 10)
user_guess = None

print("Welcome to 'Guess the Number'!")
print("I have selected a number between 1 and 10. Try to guess it.")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))

    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly.")


# Q25) Write a program that checks if a number is a palindrome (e.g., 121 -> palindrome).
num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


# Q26) Write a program that calculates the sum of digits of a given integer.
num = int(input("Enter a number: "))
sum=0
while(num!=0):
    rem=num%10
    num=num//10
    sum+=rem
print(sum)


# Q27) Write a program to print a left-aligned triangle of stars of height n.
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("* "*i)


# Q28) Write a program that prints numbers from 1 to 10, but skip multiples of 3 using continue, and stop completely if the number is 9 using break.
for i in range(1,11):
    if (i%3==0):
        continue
    if (i==9):
        break
    else:
        print(i)


# Q29) Write a Python script to print the multiplication table for numbers 1 through 5 (using nested loops).
for i in range(1,6):
    print(f"Multiplication table of {i}:-")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")


# Q30) A perfect number is a number that is equal to the sum of its positive divisors (excluding itself). Write a program to check if a number is perfect.
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num // 2 + 1):
    if num % i == 0:  
        sum += i
if sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")


# Q31) Implement the Euclidean algorithm to find the GCD (Greatest Common Divisor) of two numbers using a while loop.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if b > a:
    a, b = b, a
while b != 0:
    a, b = b, a % b
print(f"The GCD of the given numbers is: {a}")


# Q32) Write a Python function to compute the LCM (Least Common Multiple) of two numbers, leveraging the GCD.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")


# Q33) Write a program to count the number of words in a user-input string (words are separated by spaces).
n=input("Enter a string with spaces: ")
print(f"Total number of words is = {len(n.split())}")


# Q34) Write a function to check if a 3-digit number is an Armstrong number (e.g., 153 -> 1^3 + 5^3 + 3^3 = 153).
num = int(input("Enter a 3-digit number: "))
if sum(int(digit)**3 for digit in str(num))==num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


# Q35) Write a Python program to calculate the sum of the series 1 + 1/2 + 1/3 + … + 1/n using a for loop.
n = int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=1/i
print(sum)


# Q36) Write a program that generates all prime numbers in a given range [start, end].
start= int(input("Enter the first number: "))
end= int(input("Enter the end number: "))
for i in range(start, end + 1):
    for j in range(2, int((i / 2) + 1)):
        if i%j == 0:
            break
    else:
        print(i)


# Q37) Write a program that displays the Collatz sequence for any positive integer given by the user.
n = int(input("Enter a positive integer: "))
while n != 1:
    print(n, end=" -> ") 
    if n % 2 == 0: 
        n //= 2
    else: 
        n = 3 * n + 1
print(1) 


# Q38) Print a diamond-shaped pattern of stars with a width given by the user (e.g., for 5).
n = int(input("Enter an odd number for the diamond's width: "))
for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)
for i in range(n - 2, 0, -2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)


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


# Q40) Write a program to count how many times a specific character appears in a given string.
string = input("Enter a string: ")
char = input("Enter the character to count: ")
if len(char) != 1:
    print("Please enter a single character.")
else:
    count = 0
    for c in string:
        if c == char:
            count += 1
    print(f"The character {char} appears {count} times.")


# Q41) Write a list comprehension that generates a list of squares of numbers from 1 to 10.
sq=[i**2 for i in range(1,11)]
print(sq)


# Q42) Write a program that calculates the sum of all elements in a list.
n=input("Enter a list: ").split()
n=[int(i) for i in n]
result=sum(n)
print(f"Sum if the elements is: {result}")


# Q43) Write a function that returns the largest and the smallest elements in a given list.
n=input("Enter a list: ").split()
n=[int(i) for i in n]
print(f"The largest elemennt is: {max(n)}")
print(f"The smallest elemennt is: {min(n)}")


# Q44) Write a Python function that removes duplicate elements from a list and returns the new list.
n=input("Enter a list: ").split()
n=[int(i) for i in n]
result=list(set(n))
print(f"List after removing the duplicate elements: {result}")


# Q45) Implement a linear search to find a given element in a list. Return the index if found, or -1 otherwise.
n=input("Enter a list: ").split()
search=int(input("Enter the element to be searched: "))
n=[int(i) for i in n]
for index in range(len(n)):
    if (search==n[index]):
        print(f"Element is found at index: {index}")
        break
else:
    print("Element is found at index: -1")


# Q46) Implement the bubble sort algorithm to sort a list in ascending order.
arr = list(map(int, input("Enter a list of numbers: ").split()))
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted list in ascending order:", arr)


# Q47) Write a program to reverse a list in-place (without using reversed() or slicing).
arr = list(map(int, input("Enter a list of numbers: ").split()))
n = len(arr)
left=0
right=len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print("Reversed list:", arr)


# Q48) Write a Python program that counts the number of times a given element appears in a list.
arr = list(map(int, input("Enter a list of numbers: ").split()))
element = int(input("Enter the element to be counted: "))
count = arr.count(element)
print(f"The element {element} appears {count} time3 in the list.")


# Q49) Write a function to rotate a list by k positions to the right. For instance, [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3].
arr = list(map(int, input("Enter a list of numbers: ").split()))
k = int(input("Enter the positions to rotate: "))
k = k % len(arr)
rotated_arr = arr[-k:] + arr[:-k]
print("Rotated list:", rotated_arr)


# Q50) Write a function to find the second-largest element in a list.
arr = list(map(int, input("Enter a list of numbers: ").split()))
largest = second = float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print(f"The second-largest element is: {second}")


# Q51) Write a function that merges two sorted lists into one sorted list.
l1 = list(map(int, input("Enter the first sorted list: ").split()))
l2 = list(map(int, input("Enter the second sorted list: ").split()))
merged = []
i = j = 0
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        merged.append(l1[i])
        i += 1
    else:
        merged.append(l2[j])
        j += 1
while i < len(l1):
    merged.append(l1[i])
    i += 1
while j < len(l2):
    merged.append(l2[j])
    j += 1
print("Merged sorted list:", merged)


# Q52) Given a list, write a Python function to find all duplicate elements.
arr = list(map(int, input("Enter a list of numbers: ").split()))
element_count = {}
duplicates = []
for elem in arr:
    if elem in element_count:
        element_count[elem] += 1
    else:
        element_count[elem] = 1
for elem, count in element_count.items():
    if count > 1:
        duplicates.append(elem)
print("Duplicate elements are:", duplicates)


# Q53) Write a program to remove all even numbers from a list of integers.
arr = list(map(int, input("Enter a list of numbers: ").split()))
result=[num for num in arr if num%2!=0]
print(f"List after removing even numbers is: {result}")


# Q54) Write a program to shuffle a list in-place (you can use random.shuffle or implement your own shuffling algorithm).
import random
arr = list(map(int, input("Enter a list of numbers: ").split()))
random.shuffle(arr)
print(arr)

# Q55) Write a Python function to check if a given list is sorted in ascending order.
arr = list(map(int, input("Enter a list of numbers: ").split()))
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted list in ascending order:", arr)


# Q56) Given two lists of the same length, create a dictionary mapping elements of one list to the corresponding elements of the other.
keys = input("Enter the first list: ").split()
values = input("Enter the second list: ").split()
if len(keys) != len(values):
    print("Error: Both lists must have the same length.")
else:
    result_dict = dict(zip(keys, values))
    print("Resulting dictionary:", result_dict)


# Q57) Write a program that counts the frequency of each element in a list using a dictionary.
arr = input("Enter the elements of the list: ").split()
frequency = {}
for i in arr:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("Frequency of each element:", frequency)


# Q58) Write a function that inverts a dictionary (keys become values, values become keys).
keys = input("Enter the first list: ").split()
values = input("Enter the second list: ").split()
if len(keys) != len(values):
    print("Error: Both lists must have the same length.")
else:
    result_dict = dict(zip(keys, values))
    inverted_dict = {value: key for key, value in result_dict.items()}
    print("Resulting dictionary:", inverted_dict)


# Q59) Write a program to check if a given key exists in a dictionary.
keys = input("Enter the key: ").split()
values = input("Enter the value: ").split()
dict = dict(zip(keys, values))
check = input("Enter the key to check: ")
if check in keys:
    print(f"The key {check} exists in the dictionary.")
else:
    print(f"The key {check} do not exists in the dictionary.")


# Q60) Write a function to merge two dictionaries. If a key appears in both, add their values.
keys1 = input("Enter the key: ").split()
values1 = input("Enter the value: ").split()
dict1 = dict(zip(keys1, values1))
keys2 = input("Enter the key: ").split()
values2 = input("Enter the value: ").split()
dict2 = dict(zip(keys2, values2))
add=dict1.copy()
for key, value in dict2.items():
    if key in add:
        add[key]+=value
    else:
        add[key]=value
print("Merged Dictionary:", add)


# Q61) Write a Python program to sort a dictionary by its values in ascending order.
keys = input("Enter the key: ").split()
values = input("Enter the value: ").split()
dict1 = dict(zip(keys, values))
sort=dict(sorted(dict1.items(),key=lambda item:item[1]))
print("Sorted dictionary in ascending order:", sort)


# Q62) Generate a dictionary that contains numbers (1 to n) as keys and their squares as values.
n=int(input("Enter a number: "))
sq={i:i**2 for i in range(1,n+1)}
print("The numbers and their squares are:")
print(sq)


# Q63) Write a Python program to perform union, intersection, and difference operations on two sets.
set1 = set(map(int, input("Enter elements for set1: ").split()))
set2 = set(map(int, input("Enter elements for set2: ").split()))
union = set1 | set2 
intersection = set1 & set2  
difference1 = set1 - set2 
difference2 = set2 - set1 
print(f"Union of set1 and set2: {union}")
print(f"Intersection of set1 and set2: {intersection}")
print(f"Difference of set1 and set2: {difference1}")
print(f"Difference of set2 and set1: {difference2}")


# Q64) Given a list with duplicates, use a set to create a list of unique elements (in any order).
set1 = set(map(int, input("Enter duplicate elements for set1: ").split()))
print(f"List of unique elements is: {set1}")


# Q65) Given two lists, write a program to find the common elements using sets.
set1 = set(map(int, input("Enter elements for set1: ").split()))
set2 = set(map(int, input("Enter elements for set2: ").split()))
common=set1&set2
print(f"Common elements are: {common}")


# Q66) Implement a function factorial(n) that calculates n! using recursion.
n=int(input("Enter a number: "))
fact=1
if n==0 or n==1:
    print("The factorial is: 1")
else:
    for i in range(1, n + 1):
        fact *= i
print("The fatorial is: ",fact)


# Q67) Implement a function fib(n) to return the nth Fibonacci number using recursion.
n=int(input("Enter a number: "))
a,b=0,1
if n==0:
    print(f"fibonacci series of {n} numbers is: 0")
elif n==1:
    print(f"fibonacci series of {n} numbers is: 1")
else:
    print("Fibonacci series:", end=" ")
    while n > 0:
        print(a, end=" ")
        a, b = b, a + b
        n -= 1


# Q68) Write a recursive function power(base, exp) that computes base^exp.
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = 1
while exp > 0:
    result *= base
    exp -= 1
print(f"The result of {base}^exp is: {result}")


# Q69) Write a recursive function that computes the sum of all elements in a list.
def recursive(lst):
    if not lst:
        return 0
    return lst[0] + recursive(lst[1:])
num = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = recursive(num)
print(f"The sum of the elements is: {result}")



# Q70) Implement binary search recursively to find an element in a sorted list.
def binary(arr, left, right, target):
    if left > right:
        return -1 
    mid = (left + right) 
    if arr[mid] == target:
        return mid  
    elif arr[mid] > target:
        return binary(arr, left, mid - 1, target)
    else:
        return binary(arr, mid + 1, right, target)
arr = list(map(int, input("Enter a sorted list of elements: ").split()))
target = int(input("Enter the element to search for: "))
result = binary(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")


# Q71) Write a recursive solution to the Tower of Hanoi puzzle for n disks.Write a recursive solution to the Tower of Hanoi puzzle for n disks.
def tower(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower(n-1, auxiliary, source, destination)
n = int(input("Enter the number of disks: "))
tower(n, 'A', 'B', 'C')


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


# Q73) Write a recursive function that takes a list which may contain nested lists and returns a flat list of all elements.
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
nested_list = [1, [2, 3], [4, [5, 6]], 7]
result = flatten(nested_list)
print("Flattened list:", result)


# Q74) Write a recursive function that checks if a string is a palindrome.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
n = input("Enter a string: ")
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")


# Q75) Write a recursive function to compute the Greatest Common Divisor (GCD) of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = gcd(a, b)
print(f"The GCD of {a} and {b} is: {result}")


# Q76) Write a Python script that reads a text file and prints its contents.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Q77) Write a program that prompts the user for a line of text and writes that line to a file.
text = input("Enter a line of text: ")
file_name = input("Enter the filename to save the text: ")
try:
    with open(file_name, 'w') as file:
        file.write(text)
    print(f"Text has been written to {file_name}")
except Exception as e:
    print(f"An error occurred: {e}")


# Q78) Write a Python program to copy the contents of one file to another.
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
try:
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"Content from {source_file} has been copied to {destination_file}.")
except FileNotFoundError:
    print(f"Error: The file '{source_file}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# Q79) Write a Python program that reads a file and counts the number of words in it.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
    words = content.split()
    word_count = len(words)
    print(f"The number of words in '{file_name}' is: {word_count}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# Q80) Write a program that counts how many lines are in a file.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
    line_count = len(lines)
    print(f"The number of lines in '{file_name}' is: {line_count}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")


# Q81) Modify the file-reading program to handle exceptions (e.g., file not found) gracefully.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
    line_count = len(lines)
    print(f"The number of lines in '{file_name}' is: {line_count}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Q82) Write a program that finds the longest word in a text file and prints it.
file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
    words = content.split()
    longest_word = max(words, key=len)
    print(f"The longest word in the file is: {longest_word}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Q83) Write a program to search for a specific substring in a file and print the lines where it appears.
file_name = input("Enter the file name: ")
substring = input("Enter the substring to search for: ")
try:
    with open(file_name, 'r') as file:
        found = False
        for line_number, line in enumerate(file, start=1):
            if substring in line:
                found = True
                print(f"Line {line_number}: {line.strip()}")
        if not found:
            print(f"The substring '{substring}' was not found in any line of the file.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Q84) Write a program that appends a user-input line to an existing file without overwriting it.
file_name = input("Enter the file name: ")
line_to_append = input("Enter the line you want to append: ")
try:
    with open(file_name, 'a') as file:
        file.write(line_to_append + "\n")
    print(f"The line has been appended to {file_name}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Q85) Write a Python script to read a CSV file and print each row.
import csv
file_name = input("Enter the CSV file name: ")
try:
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found. Please check the file name and try again.")
except IOError:
    print(f"Error: There was an issue accessing the file '{file_name}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Q86) Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
person1 = Person("Vrutti", 20)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")


# Q87) Add a method greet to the Person class that prints "Hello, my name is <name>".
def greet(name):
    return f"Hello, my name is {name}"
p=input("Enter your name: ")
print(greet(p))


# Q88) Define a class Car with a constructor that sets make, model, and year. Create an instance and display its details.
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display(self):
        print(f"Make is: {self.make} \nModel is: {self.model} \nYear is: {self.year}")
c=Car("Toyota","Corolla",2020)
c.display()


# Q89) Modify the Car class to have default values for make and model if not provided.
class Car:
    def __init__(self, make="Unknown", model="Unknown", year=None):
        self.make = make
        self.model = model
        self.year = year
    def display_details(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year if self.year else 'Unknown'}")
car1 = Car(year=2020)
car2 = Car("Toyota", "Corolla", 2020)
car1.display_details()
car2.display_details()


# Q90) Create a base class Animal and a derived class Dog. The Dog class should inherit attributes and methods from Animal.
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def speak(self):
        print(f"{self.name} makes a sound.")
class Dog(Animal):
    def __init__(self, name, breed, species="Dog"):
        super().__init__(name, species)
        self.breed = breed
    def speak(self):
        print(f"{self.name} barks!")
animal = Animal("Some Animal", "Unknown Species")
animal.speak()
dog = Dog("Buddy", "Golden Retriever")
dog.speak()
print(f"{dog.name} is a {dog.breed} and is a {dog.species}.")


# Q91) In the Dog class, override a method speak defined in Animal (e.g., Animal says “Some sound”, but Dog says “Woof!”).
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says Some sound.")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} says Woof!")
animal = Animal("Some Animal")
animal.speak()  
dog = Dog("Buddy", "Golden Retriever")
dog.speak() 


# Q92) Create classes Rectangle and Square. Square should inherit from Rectangle (or implement composition) in a way that automatically sets the length and width to the same value.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def display(self):
        print(f"Rectangle - Length: {self.length}, Width: {self.width}, Area: {self.area()}, Perimeter: {self.perimeter()}")
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def display(self):
        print(f"Square - Side: {self.length}, Area: {self.area()}, Perimeter: {self.perimeter()}")
rectangle = Rectangle(5, 3)
rectangle.display()
square = Square(4)
square.display()


# Q93) Demonstrate encapsulation by creating a class with private attributes and use getter and setter methods to access/modify them.
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age 
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        if new_age > 0:  
            self.__age = new_age
        else:
            print("Age must be positive.")
person = Person("Alice", 25)
print("Name:", person.get_name())
print("Age:", person.get_age())
person.set_name("Bob")
person.set_age(30)
print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())



# Q94) Demonstrate polymorphism by defining a method draw() in multiple classes (Circle, Triangle, etc.) and calling draw() on a list of shapes.
class Shape:
    def draw(self):
        pass 
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")
class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")
class Square(Shape):
    def draw(self):
        print("Drawing a Square")
shapes = [Circle(), Triangle(), Square()]
for shape in shapes:
    shape.draw()


# Q95) Create a class Counter with a class variable count. Implement a @classmethod to increment count and a @staticmethod to display some utility message.
class Counter:
    count = 0  
    @classmethod
    def increment(cls):
        cls.count += 1
        print(f"Count incremented to: {cls.count}")
    @staticmethod
    def display_message():
        print("This is a static method and does not depend on class or instance variables.")
Counter.increment()  
Counter.increment()  
Counter.display_message() 


# Q96) Implement a Python class that overloads the __str__ method to return a string representation of the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
p = Person("Vrutti", 20)
print(p)  


# Q97) Create a class Point that overloads the + operator (using __add__) to add the coordinates of two Point objects.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __str__(self):
        return f"({self.x}, {self.y})"
p1 = Point(2, 3)
p2 = Point(4, 5)
result = p1 + p2  
print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Result of addition: {result}")


# Q98) Use the abc module to define an abstract base class Shape with an abstract method area(). Implement subclasses Circle and Rectangle.
from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Area of Circle is: {circle.area()}")
print(f"Area of Rectangle is: {rectangle.area()}")


# Q99) Create a class that uses the @property decorator to get/set an attribute with some validation logic.
class Temperature:
    def __init__(self, temp_celsius):
        self._temp_celsius = temp_celsius
    @property
    def temp_celsius(self):
        return self._temp_celsius
    @temp_celsius.setter
    def temp_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature can't be below absolute zero (-273.15°C).")
        self._temp_celsius = value
temp = Temperature(25) 
print(f"Temperature in Celsius: {temp.temp_celsius}")
temp.temp_celsius = 30  
print(f"Updated Temperature in Celsius: {temp.temp_celsius}")
try:
    temp.temp_celsius = -300  
except ValueError as e:
    print(e)  


# Q100) Demonstrate multiple inheritance with two parent classes providing different functionalities to a child class.
class Animal:
    def eat(self):
        print("This animal eats food.")
class Bird:
    def fly(self):
        print("This bird can fly.")
class Parrot(Animal, Bird):
    pass
parrot = Parrot()
parrot.eat()  
parrot.fly()  


# Q101) Write a script that uses the math module to compute the square root, floor, and ceiling of a user-input number.
import math
number = float(input("Enter a number: "))
sq = math.sqrt(number)
flr = math.floor(number)
cei = math.ceil(number)
print(f"The square root of {number} is: {sq}")
print(f"The floor value of {number} is: {flr}")
print(f"The ceiling value of {number} is: {cei}")


# Q102) Write a function that randomly selects an element from a given list using the random module.
import random
lst = list(map(int, input("Enter a list: ").split()))
result=random.choice(lst)
print(f"Randomly selected element: {result}")


# Q103) Write a script that gets the current date and time and formats it as YYYY-MM-DD HH:MM:SS.
import time
current = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", current)
print("Current Date and Time:", formatted)


# Q104) Write a program that lists all files and directories in the current directory using os.listdir().
import os
current_directory = os.getcwd()
files_and_dirs = os.listdir(current_directory)
print("Files and directories in the current directory:")
for item in files_and_dirs:
    print(item)


# Q105) Use the statistics module to compute the mean, median, and mode of a list of numbers.
import statistics
numbers = list(map(int, input("Enter a list: ").split()))
mean = statistics.mean(numbers)
median = statistics.median(numbers)
try:
    mode = statistics.mode(numbers)
except statistics.StatisticsError:
    mode = "No unique mode"
print(f"Mean is: {mean}")
print(f"Median is: {median}")
print(f"Mode is: {mode}")


# Q106) Write a script that takes command-line arguments and prints them.
import sys
print("Command-line arguments:", sys.argv)
print("Arguments without the script name:")
for arg in sys.argv[1:]:
    print(arg)


# Q107) Write a script that reads a JSON file, modifies a value, and writes the updated data back to the file.
import json
filename = "data.json" 
try:
    with open(filename, 'r') as file:
        data = json.load(file)
    if "key_name" in data:
        data["key_name"] = "new_value" 
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("JSON file updated successfully!")
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON from the file {filename}.")


# Q108) Write a program (assuming you have internet access) that fetches data from a public API using the requests module and prints part of the JSON response.
import requests
def fetch_data_from_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("Sample Data from the API:")
            for post in data[:3]: 
                print(f"ID: {post['id']}, Title: {post['title']}\n")
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
fetch_data_from_api()


# Q109) Write a script that extracts all email addresses from a given string using the re module.
import re
text = "Please contact us at support@example.com or sales@mycompany.org for more info."
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_addresses = re.findall(email_pattern, text)
print("Extracted email addresses:", email_addresses)


# Q110) Write a script that uses the logging module to log debug, info, warning, and error messages to a file.
import logging
logging.basicConfig(filename='app.log',
                    level=logging.DEBUG,  
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical error message.")


# Q111) Demonstrate advanced list slicing (e.g., reversing a list with slicing, skipping elements) in a script.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_list = my_list[::-1]
print(f"Reversed list: {reversed_list}")
every_second_element = my_list[::2]
print(f"Every second element: {every_second_element}")
sublist = my_list[2:6]
print(f"Sublist from index 2 to 6 (exclusive): {sublist}")
skip_elements = my_list[1:8:3]
print(f"Skipping elements from index 1 to 8 with step 3: {skip_elements}")
reversed_sublist = my_list[5:1:-1]
print(f"Reversed sublist from index 5 to 2: {reversed_sublist}")
last_three_elements = my_list[-3:]
print(f"Last 3 elements: {last_three_elements}")
reversed_skipped = my_list[::-2]
print(f"Reversed and skipping every other element: {reversed_skipped}")
empty_sublist = my_list[4:2]
print(f"Empty sublist (4 to 2, exclusive): {empty_sublist}")



# Q112) Use a lambda function inside map to transform a list of numbers (e.g., multiply each by 2).
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(f"Transformed list: {result}")


# Q113) Use filter to filter out even numbers from a list, then use functools.reduce to sum the filtered numbers.
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(lambda x: x % 2 != 0, numbers)
sum_of_filtered_numbers = reduce(lambda x, y: x + y, filtered_numbers)
print(f"Sum of filtered odd numbers: {sum_of_filtered_numbers}")


# Q114) Write a script that demonstrates the difference between a list comprehension and a generator expression for large data.
import time
start_time = time.time()
list_comp = [x**2 for x in range(1, 10000001)]  
end_time = time.time()
list_comp_time = end_time - start_time
print(f"List Comprehension Time: {list_comp_time} seconds")
start_time = time.time()
gen_expr = (x**2 for x in range(1, 10000001))
gen_list = list(gen_expr)
end_time = time.time()
gen_expr_time = end_time - start_time
print(f"Generator Expression Time: {gen_expr_time} seconds")


# Q115) Write a simple decorator timer that measures the execution time of a function.
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        execution_time = end_time - start_time 
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")
        return result  
    return wrapper
@timer
def example_function():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total
example_function()


# Q116) Implement a context manager using the with statement that opens a file, writes text, and closes the file automatically.
class FileWriter:
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False
with FileWriter('example.txt') as f:
    f.write("Hello, this is a test line written to the file.")
print("Text has been written to the file and the file is automatically closed.")


# Q117) Write a Python program that spawns two threads: one prints numbers 1 to 5, the other prints letters A to E.
import threading
import time
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(0.5)  
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(0.5)  
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both threads have finished execution.")



# Q118) Use the multiprocessing module to run a function in parallel processes and aggregate the results.
import multiprocessing
def square_number(number):
    return number * number
def aggregate_squares(numbers):
    with multiprocessing.Pool() as pool:
        results = pool.map(square_number, numbers)
    return sum(results)
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]  
    total_sum = aggregate_squares(numbers)  
    print(f"The sum of squares is: {total_sum}")


# Q119) Write a simple asynchronous function using asyncio that prints a message, waits 1 second, and prints another message.
import asyncio
async def print_messages():
    print("Message 1: Starting the task...")
    await asyncio.sleep(1)  
    print("Message 2: Task completed after 1 second.")
asyncio.run(print_messages())


# Q120) Write a script that repeatedly asks the user for a number, catches ValueError if the input is invalid, and stops when a valid number is entered.
while True:
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)
        print(f"You entered the number: {number}")
        break  
    except ValueError:
        print("That's not a valid number. Please try again.")
