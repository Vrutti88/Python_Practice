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
