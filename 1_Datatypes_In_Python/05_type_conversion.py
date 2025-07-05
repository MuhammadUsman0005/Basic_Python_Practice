# Concept: Type Conversion (Type Casting)
# Used to convert one data type into another
# int(), float(), str(), bool()
'''
Example: 
When we take input from user, it's always a string.
But we may need to convert it into int or float for calculations.
'''

#input() function used to take input from user by default it take string .

age_input = input("Enter your age: ")
# convert to integer
age = int(age_input)

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Convert float to int 
price  = 99.2
new_price = int(price)
print("Price: ",new_price,type(new_price))


# Convert number or integer to boolean
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))      # False
print(bool("abc"))      # True