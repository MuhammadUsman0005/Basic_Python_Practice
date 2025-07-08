# Topic: Comparison Operators in Python
# These operators are used to compare two values.

# List of Comparison Operators:
# == -> equal to
# != -> not equal to
# >  -> greater than
# <  -> less than
# >= -> greater than or equal to
# <= -> less than or equal to


#-------------------------------------------
#🔻Example 1: Grading System
marks = eval(input("Enter your marks(0 to 100): "))

if marks >= 90:
    print("Grade: A+")
elif marks >=80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Failed")

#-------------------------------------------
#🔻Example 2: Check for login using comparison
username = input("Enter username: ")
if username != "python":
    print("Username not found")
else:
    print("Welcome Learner!")