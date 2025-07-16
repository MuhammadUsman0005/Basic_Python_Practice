# Topic: Tuple Methods in Python
# This file demonstrates the built-in methods available for tuples in Python and their applications.
# Tuples are immutable, so they have only two built-in methods: count() and index().

# -------------------
# 1. Tuple Methods Overview
# -------------------
# Tuples have two built-in methods due to their immutability:
# - count(value): Returns the number of occurrences of a value in the tuple.
# - index(value[, start[, end]]): Returns the index of the first occurrence of a value.
sample_tuple = (1, 2, 2, 3, 4, 2, 5)
print("Sample tuple:", sample_tuple)

# -------------------
# 2. Using count() Method
# -------------------
# count() returns how many times a specified value appears in the tuple
count_of_2 = sample_tuple.count(2)  # Counts occurrences of 2
print("Number of times 2 appears:", count_of_2)  # Prints 3

# Count for a value not in the tuple
count_of_10 = sample_tuple.count(10)  # Returns 0 since 10 is not in the tuple
print("Number of times 10 appears:", count_of_10)  # Prints 0

# Example with mixed data types
mixed_tuple = (1, "apple", True, "apple", 3.14)
count_of_apple = mixed_tuple.count("apple")  # Counts occurrences of "apple"
print("Mixed tuple:", mixed_tuple)
print("Number of times 'apple' appears:", count_of_apple)  # Prints 2

# -------------------
# 3. Using index() Method
# -------------------
# index() returns the index of the first occurrence of a value
index_of_2 = sample_tuple.index(2)  # Finds first occurrence of 2
print("Index of first 2:", index_of_2)  # Prints 1

# index(value,start,end) with start and end parameters
index_of_2_after_2 = sample_tuple.index(2, 2, 6)  # Search for 2 between indices 2 and 5
print("Index of 2 between indices 2 and 5:", index_of_2_after_2)  # Prints 5

# index() raises ValueError if the value is not found
try:
    sample_tuple.index(10)  # 10 is not in the tuple
except ValueError as e:
    print("Error finding index of 10:", e)

# -------------------
# 4. Practical Applications of Tuple Methods
# -------------------
# Example: Counting duplicates in a dataset
grades = ("A", "B", "A", "C", "A", "D", "B")
print("Grades tuple:", grades)
a_count = grades.count("A")
print("Number of 'A' grades:", a_count)  # Prints 3

# Example: Finding the position of an element
tasks = ("todo", "in_progress", "done", "todo")
first_todo = tasks.index("todo")
print("Index of first 'todo' task:", first_todo)  # Prints 0

# Example: Checking for presence before using index()
value = "done"
if value in tasks:
    print(f"Index of '{value}':", tasks.index(value))  # Prints 2
else:
    print(f"'{value}' not found in tasks")
