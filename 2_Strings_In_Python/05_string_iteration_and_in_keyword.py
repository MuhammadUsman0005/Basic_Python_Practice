# Concept: Iterating through strings and using 'in' keyword.
# NOTE: This flie uses 'for loop' and if statement concepts.
# For full explanation, you can visit their individula folders in this repository.

name = "Python language"

#🔻Loop through string (character by character)
print("Characters in the name: ")
for char in name:
    print(char)

#------------------------------
#🔻Count how many times a character appears
target = "a"
count = 0
for char in name:
    if char.lower() == target:
        count += 1
print(f"'{target}' appears {count} times in the name.")   # OUPUR: 'a' appears 2 times in the name.

#-----------------------------
#🔻Use of 'in' keyword
# To check if a character or word exists in a string

if "Python" in name:
    print("'Python' is found in a name.")
if "z" not in name:
    print("'z' is not in the name.")

#----------------------------------

#🔻Find vowels in the name
message = "Learning Python is a fun."
VOWELS = "aeiouAEIOU"

for char in message:
    if char in VOWELS:
        print(char, end=" ")       # OUPUT: Vowels found
print()       # new line

#----------------------------
# REAL LIFE EXAMPLE: Password must contain @
password = "python@0123"

if '@' in password:
    print("Password accepted.")
else:
    print("Password must contain '@' symbol.")