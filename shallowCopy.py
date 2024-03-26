import copy

# Create a list
original_list = [1, 2, [3, 4]]

# Perform shallow copy
shallow_copy = copy.copy(original_list)

# Modify the nested list in the shallow copy
shallow_copy[2][0] = 5

# Print the original list and the shallow copy
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)