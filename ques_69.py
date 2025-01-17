# Q69) Write a recursive function that computes the sum of all elements in a list.
def recursive(lst):
    if not lst:
        return 0
    return lst[0] + recursive(lst[1:])
num = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = recursive(num)
print(f"The sum of the elements is: {result}")
