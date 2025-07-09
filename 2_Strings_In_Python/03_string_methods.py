# Concept: String methods (common string methods)
# string in Python have many built-in methods to modify,search, or format them.

text = "Hello, Python learners!"

# 🔻lower() -> convert to lowercase
print(text.lower())    # hello, python learners!

# 🔻upper() -> convert to uppercase 
print(text.upper())    # HELLO, PYTHON LEARNERS!

# 🔻title() -> Capitalize each word
print(text.title())    # Hello, Python Learners!

# 🔻capitalize() -> capitalize first letter only
print(text.capitalize())  # hello, python learners!

# 🔻strip() -> Removes extra spaces form both ends
name = "  Python language    "
print(name.strip())      # "Python language"

# 🔻lstrip(), rstrip()
print(name.lstrip())    # removes only left spaces
print(name.rstrip())    # removes only right spaces

# 🔻replace() -> Replace text
print(name.replace("Python", "C++"))   # Output: C++ language

# 🔻find()  -> finds index of first match 
print(text.find("learners!"))  # returns position of "learners!"
print(text.find("C++"))     # returns -1 if not found

# 🔻count() -> count occurences of a word/letter
print(text.count("e"))    # count e in text , OUTPUT: 3

# 🔻startswith() -> check if string starts with...
print(text.startswith("Hi"))    # False
print(text.startswith("Hello"))  # True

# 🔻endswith() -> check if string ends with...
print(text.endswith("language!"))  # False
print(text.endswith("learners!"))   # True

# 🔻split() -> Break into list
words = name.split()
print(words)               # ['Python', 'language']
words = text.strip().split()        # default split on space, OUTPUT:['Hello','Python', 'learners!']

# 🔻join()  -> join list back into string
joined = " ".join(words)
print(joined)               # Hello, Python learners!

# 🔻isalpha() -> only letters (no space or numbers)
data1 = "Programming"
print(data1.isalpha())      # True
data = "abcHello123"        
print(data.isalpha())       # False

# 🔻isdigit()  -> only digits
numbers = "11243"
print(numbers.isdigit())     # True
print(data.isdigit())      # False

# 🔻isnumeric()  -> only numbers
print("123".isnumeric())    # True
print("1/2".isnumeric())    # True

# 🔻isalnum()  -> letters or digits (no symbols/space)
print("123aancd".isalnum())  # True
print("abc 1243".isalnum())  # False

# 🔻swapcase()  -> swap cases lower to upper, upper to lower
print("PyTHoN".swapcase())   # pYthOn

# 🔻zfill()  -> pad number with zeros
print("2".zfill(3))   # "002"
print("6".zfill(6))   # "000006"

# 🔻center()  -> center align with padding
print("Python".center(15,"*"))   # "*****Python****"