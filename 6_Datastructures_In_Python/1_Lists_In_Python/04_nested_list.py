# Topic: Nested Lists in Python

# This script demonstrates the concept of nested lists in Python, from basic to advanced.
# A nested list is a list that contains other lists as its elements.
# Nested lists can represent multi-dimensional data structures, like matrices or hierarchical data.

# -------------------
# 1. Creating a Nested List
# -------------------
# A nested list can have lists as elements, and those lists can also contain lists (multi-level nesting).
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # A 3x3 nested list (like a matrix)
print("Nested list:", nested_list)

# You can also create irregular nested lists where sublists have different lengths.
irregular_nested = [[1, 2], [3, 4, 5], [6]]  # Sublists with different lengths
print("Irregular nested list:", irregular_nested)

# -------------------
# 2. Accessing Elements in a Nested List
# -------------------
# Use multiple indices to access elements in a nested list.
# Syntax: list_name[outer_index][inner_index]
first_element = nested_list[0][0]  # Accesses 1 (first element of the first sublist)
print("First element (nested_list[0][0]):", first_element)

# Access an entire sublist
first_sublist = nested_list[0]  # Gets [1, 2, 3]
print("First sublist (nested_list[0]):", first_sublist)

# For deeper nesting, add more indices
deep_nested = [[1, [2, 3]], [4, [5, 6]]]
deep_element = deep_nested[0][1][0]  # Accesses 2
print("Deep nested element (deep_nested[0][1][0]):", deep_element)

# -------------------
# 3. Modifying Elements in a Nested List
# -------------------
# You can modify elements using indices.
nested_list[1][2] = 60  # Change 6 to 60 in the second sublist
print("After modifying nested_list[1][2]:", nested_list)

# Replace an entire sublist
nested_list[2] = [70, 80, 90]  # Replace [7, 8, 9] with [70, 80, 90]
print("After replacing sublist:", nested_list)

# -------------------
# 4. Iterating Over a Nested List
# -------------------
# Use nested loops to iterate over all elements.
print("Iterating over nested list:")
for sublist in nested_list:
    for item in sublist:
        print(item, end=" ")  # Prints: 1 2 3 4 5 60 70 80 90
print()  # Newline for clarity

# Using indices with range() for more control
print("Iterating using indices:")
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        print(f"Element at [{i}][{j}]: {nested_list[i][j]}")

# -------------------
# 5. List Comprehension with Nested Lists
# -------------------
# List comprehension can simplify creating and manipulating nested lists.
# Example: Create a 3x3 matrix with values from 1 to 9
matrix = [[j + 1 + (i * 3) for j in range(3)] for i in range(3)]
print("Matrix created with list comprehension:", matrix)

# Flatten a nested list (convert to a single list)
flattened = [item for sublist in nested_list for item in sublist]
print("Flattened nested list:", flattened)  # Prints: [1, 2, 3, 4, 5, 60, 70, 80, 90]

# -------------------
# 6. Common Operations on Nested Lists
# -------------------
# Adding a sublist (append)
nested_list.append([100, 200, 300])  # Add a new sublist
print("After appending sublist:", nested_list)

# Removing a sublist
nested_list.pop(3)  # Remove the last sublist
print("After popping sublist:", nested_list)

# Extending a sublist
nested_list[0].extend([10, 11])  # Extend the first sublist
print("After extending first sublist:", nested_list)

# -------------------
# 7. Copying Nested Lists (Shallow vs Deep Copy)
# -------------------
# Shallow copy: Copies the outer list but references the same inner lists
import copy
shallow_copy = copy.copy(nested_list)
shallow_copy[0][0] = 999  # Modifies the first element in both shallow_copy and nested_list
print("Shallow copy modified:", shallow_copy)
print("Original after shallow copy modification:", nested_list)  # Original is affected

# Reset nested_list for clarity
nested_list = [[1, 2, 3], [4, 5, 60], [70, 80, 90]]

# Deep copy: Creates a completely independent copy
deep_copy = copy.deepcopy(nested_list)
deep_copy[0][0] = 888  # Modifies only the deep copy
print("Deep copy modified:", deep_copy)
print("Original after deep copy modification:", nested_list)  # Original is unaffected

# -------------------
# 8. Advanced: Nested List as a Matrix
# -------------------
# Example: Transpose a 3x3 matrix (swap rows and columns)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Original matrix:", matrix)
print("Transposed matrix:", transposed)

# -------------------
# 9. Checking for Elements in a Nested List
# -------------------
# Check if an element exists in any sublist
element = 5
is_present = any(element in sublist for sublist in nested_list)
print(f"Is {element} in nested_list? {is_present}")

# -------------------
# 10. Practical Example: Representing a 2D Grid
# -------------------
# Example: Create a 4x4 grid initialized with zeros
rows, cols = 4, 4
grid = [[0 for _ in range(cols)] for _ in range(rows)]
print("4x4 grid of zeros:", grid)

# Modify specific cells
grid[1][2] = 1  # Set a cell to 1
grid[3][3] = 9  # Set another cell to 9
print("Modified grid:", grid)

# -------------------
# 11. Common Pitfalls
# -------------------
# Pitfall 1: Incorrectly creating a nested list using multiplication
wrong_grid = [[0] * 3] * 3  # Creates references to the same sublist
wrong_grid[0][0] = 99  # Modifies all first elements of each sublist
print("Incorrect grid (all sublists affected):", wrong_grid)

# Correct way: Use list comprehension to create independent sublists
correct_grid = [[0 for _ in range(3)] for _ in range(3)]
correct_grid[0][0] = 99  # Modifies only the intended element
print("Correct grid (only one element changed):", correct_grid)

# -------------------
# 12. Conclusion
# -------------------
# Nested lists are powerful for representing multi-dimensional data.
# Key points:
# - Access elements with multiple indices.
# - Use nested loops or list comprehensions for iteration and creation.
# - Be cautious with shallow vs deep copies.
# - Avoid common pitfalls like using list multiplication incorrectly.