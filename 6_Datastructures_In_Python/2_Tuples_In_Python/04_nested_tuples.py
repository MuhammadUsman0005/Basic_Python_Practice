# Topic: Nested Tuples in Python
# This file demonstrates nested tuples in Python, which are tuples containing other tuples as elements.
# Nested tuples are useful for representing multi-dimensional or hierarchical data, such as matrices or structured records.

# -------------------
# 1. Creating Nested Tuples
# -------------------
# A nested tuple is a tuple where one or more elements are themselves tuples.
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))  # A 3x3 nested tuple (like a matrix)
print("Nested tuple:", nested_tuple)

# Nested tuples can be irregular 
irregular_nested = ((1, 2), (3, 4, 5), (6,))  # Different lengths
print("Irregular nested tuple:", irregular_nested)

# Deeply nested tuples (tuples within tuples within tuples)
deep_nested = ((1, (2, 3)), (4, (5, 6)))  # Two levels of nesting
print("Deeply nested tuple:", deep_nested)

# -------------------
# 2. Accessing Elements in Nested Tuples
# -------------------
# Use multiple indices to access elements: tuple[outer_index][inner_index]
first_element = nested_tuple[0][0]  # Accesses 1 (first element of first subtuple)
print("First element (nested_tuple[0][0]):", first_element)

# Access an entire subtuple
first_subtuple = nested_tuple[0]  # Gets (1, 2, 3)
print("First subtuple (nested_tuple[0]):", first_subtuple)

# Access elements in deeply nested tuples
deep_element = deep_nested[0][1][0]  # Accesses 2
print("Deep nested element (deep_nested[0][1][0]):", deep_element)

# Negative indexing works too
last_element = nested_tuple[-1][-1]  # Accesses 9
print("Last element (nested_tuple[-1][-1]):", last_element)

# -------------------
# 3. Iterating Over Nested Tuples
# -------------------
# Use nested loops to iterate over all elements
print("Iterating over nested tuple:")
for subtuple in nested_tuple:
    for item in subtuple:
        print(item, end=" ")  # Prints: 1 2 3 4 5 6 7 8 9
print()  # Newline for clarity

# Use indices for more control
print("Iterating using indices:")
for i in range(len(nested_tuple)):
    for j in range(len(nested_tuple[i])):
        print(f"Element at [{i}][{j}]: {nested_tuple[i][j]}")

# Use enumerate for index and value
print("Iterating with enumerate:")
for i, subtuple in enumerate(nested_tuple):
    for j, item in enumerate(subtuple):
        print(f"Element at [{i}][{j}]: {item}")

# -------------------
# 4. Practical Application: Nested Tuples as Matrices
# -------------------
# Example: Represent a 3x3 matrix and calculate row sums
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Matrix:", matrix)
row_sums = [sum(row) for row in matrix]  # Sum each row
print("Row sums:", tuple(row_sums))  # Convert to tuple: (6, 15, 24)

# Example: Transpose a matrix (swap rows and columns)
transposed = tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))
print("Transposed matrix:", transposed)
