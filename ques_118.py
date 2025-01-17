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
