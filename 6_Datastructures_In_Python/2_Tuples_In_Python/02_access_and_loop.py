# Topic: This file demonstrates how to access elements in a tuple and how to loop through a tuple in Python. It covers indexing, slicing, and using loops.
# This builds on the basics introduced in 01_tuple_basics.py, focusing on practical ways to work with tuple data.

#--------------------------------------------------------
#🔻Accessing Tuple Elements
#---------------------------------------------------------
sample_tuple = (10, 20, 30, 40, 50)
print("Sample Tuple:", sample_tuple)

# Access elements using positive indexing
first_element = sample_tuple[0]   # Gets 10
last_element = sample_tuple[4]    # Gets 50
print("First Element:", first_element)
print("Last Element:", last_element)

# Access elements using negative indexing
last_element_neg = sample_tuple[-1]  # Gets 50
second_last_element = sample_tuple[-2]  # Gets 40
print("Last Element (Negative Index):", last_element_neg)
print("Second Last Element (Negative Index):", second_last_element)

#---------------------------------------------------------
#🔻Slicing Tuples
#---------------------------------------------------------
# Slicing allows accessing a range of elements: tuple[start:stop:step]
# - start: index to start from (inclusive)
# - stop: index to stop at (exclusive)
# - step: how many indices to skip (default is 1)
sliced_tuple = sample_tuple[1:4]  # Gets (20, 30, 40)
print("Sliced Tuple (1:4):", sliced_tuple)

# Slicing with step
sliced_with_step = sample_tuple[0:5:2]  # Gets (10, 30, 50)
print("Sliced Tuple with Step (0:5:2):", sliced_with_step)

# Slicing with negative indices
reverse_subset = sample_tuple[-3:-1]  # Gets (30, 40)
print("Sliced Tuple with Negative Indices (-3:-1):", reverse_subset)

# Full slice (copying the entire tuple)
full_copy = sample_tuple[:]   # Gets (10, 20, 30, 40, 50)
print("Full Copy of Tuple:", full_copy)

# Reversing a tuple using slicing
reversed_tuple = sample_tuple[::-1]  # Gets (50, 40, 30, 20, 10)
print("Reversed Tuple:", reversed_tuple)
#---------------------------------------------------------
#🔻Looping\Iteration Through a Tuple:
#---------------------------------------------------------
# Using a for loop to iterate through each element in the tuple
print("Iterating with a for loop:")
for item in sample_tuple:
    print(item, end=' ')   # Prints: 10 20 30 40 50
print()  # New line after loop

# Use a for loop with range to access indices
print("Iterating with range:")
for i in range(len(sample_tuple)):
    print(f"Element at index {i}: {sample_tuple[i]}", end=' ')

# Use enumerate() to get both index and value
print("\nIterating with enumerate:")
for index, value in enumerate(sample_tuple):
    print(f"Index {index} has value {value}", end=' ')  

# Use a while loop to iterate through the tuple
print("\nIterating with a while loop:")
index = 0
while index < len(sample_tuple):
    print(f"Element at index {index}: {sample_tuple[index]}", end=' ')
    index += 1

#----------------------------------------------------------------
#🔻Practical Examples: Processing Tuple Data
#----------------------------------------------------------------
# Example: Summing all elements in a tuple
numbers = (1, 2, 3, 4, 5)
total = 0
for number in numbers:
    total += number
print("\nTotal Sum of Numbers Tuple:", total)  # Outputs: 15

# Example Find element greater than a threshold
threshold = 3
filtered = [num for num in numbers if num > threshold]
print("Elements greater than threshold (3):", filtered)  # Outputs: [4, 5]

# Example: Finding the maximum element in a tuple
max_value = max(numbers)
print("Maximum value in the tuple:", max_value)  # Outputs: 5

# Example: Finding the minimum element in a tuple
min_value = min(numbers)
print("Minimum value in the tuple:", min_value)  # Outputs: 1
