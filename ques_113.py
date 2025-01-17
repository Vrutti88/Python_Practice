# Q113) Use filter to filter out even numbers from a list, then use functools.reduce to sum the filtered numbers.
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(lambda x: x % 2 != 0, numbers)
sum_of_filtered_numbers = reduce(lambda x, y: x + y, filtered_numbers)
print(f"Sum of filtered odd numbers: {sum_of_filtered_numbers}")
