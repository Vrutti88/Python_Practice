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
