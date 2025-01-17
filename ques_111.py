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
