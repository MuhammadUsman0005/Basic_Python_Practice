# Topic: Tuple Basics in Python
# This file introuduces the basic concepts of tuples in Python.
# A tuple is an immutable, ordered collection of elements that can store items of different data types. Tuples are defined using parentheses () and are useful for storing fixed data that should not change.
#-----------------------------------------
#🔻Creating a tuple
#-----------------------------------------
# Create a tuple using parentheses ()
simple_tuple = (1, 2, 3, 4)          # A tuple of integers
print("Simple Tuple:", simple_tuple)
# Create a tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True) # Integer, string, float, boolean
print("Mixed Tuple:", mixed_tuple)
# Create a tuple with a single element (note the comma)
single_element_tuple = (12,)    # Comma is necessary to define a single element tuple
print("Single Element Tuple:", single_element_tuple)
# Create an empty tuple
empty_tuple = ()        # An empty tuple
print("Empty Tuple:", empty_tuple)
# Create a tuple without parentheses (tuple packing)
packed_tuple = 12,13,14   # Parenthese are optional for packing
print("Packed Tuple:", packed_tuple)
#-----------------------------------------
#🔻Characteristics of Tuples
#-----------------------------------------
# Tuples are immutable, meaning their elements cannot be changed after creation
try:
    simple_tuple[0] = 100      # This will raise an error
except TypeError as e:
    print("Error:", e)
# Tuples are ordered, meaning elements mentained their insertion order
print("First element of simple_tuple:", simple_tuple[0])  # Always returns 1
# Tuples allow duplicates, same value can appear multiple times
duplicate_tuple = (1, 2, 2, 3)  # Duplicates are allowed
print("Tuple with Duplicates:", duplicate_tuple)
#------------------------------------------
#🔻Basic Operations with Tuples
#------------------------------------------
# Length of a tuple
tuple_length = len(simple_tuple)  # Returns the number of elements in the tuple
print("Length of simple_tuple:", tuple_length)
# Concatenation of tuples: Combine two or more tuples using the + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2  # Results in (1, 2, 3, 4, 5, 6)
print("Concatenated Tuple:", concatenated_tuple)
# Repetition of tuples: Repeat a tuple using *
repeated = tuple1 * 2
print("Repeated Tuple:", repeated)  # Results in (1, 2, 3, 1, 2, 3)
# Membership test: Check if an element exists in a tuple using 'in'
print("Is 2 in simple_tuple?", 2 in simple_tuple)  # Prints True
print("Is 5 in simple_tuple?", 5 in simple_tuple)  # Prints False
#-------------------------------------------
#🔻Unpack a tuple into individual variables
a, b, c, d = (10, 20, 30, 40)  # Assigns 10 to a, 20 to b, 30 to c, and 40 to d
print("Unpacked Values:", a, b, c, d)  # Prints: Unpacked Values: 10 20 30 40
#🔻Unpacking with fewer variables using *
numbers = (1,2,3,4,5)
first, *middle, last = numbers  # first gets 1, middle gets [2, 3, 4], last gets 5
print("Unpacked with *:", first, middle, last)  # Prints: Unpacked with *: 1 [2, 3, 4] 5