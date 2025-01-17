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
