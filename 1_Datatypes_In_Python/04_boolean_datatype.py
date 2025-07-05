# Concept : bool (Boolean)
# Boolean store only two values : Ture or False
# Used in decision making

'''
Example: Check if a user is eligible to vote.
Conditions:
-Age should be 18 or more
-Must have a valid NIC (National Identity Card)
'''

age = 20

has_NIC = True

if age >= 18 and has_NIC:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


print("Data type of has_NIC is: ",type(has_NIC))  # type() function is used to check type of datatype

