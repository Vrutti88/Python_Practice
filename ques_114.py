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
