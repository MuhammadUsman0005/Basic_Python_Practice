# Topic: Nested if Statements in Python
# 'Nested if' means: using an if inside another if
# It is used when one condition depends on another.
#-----------------------------------------------------------------

#🔻Example 1: Check login with correct username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "python":
    if password == "python@123": print("Welcome learners!")
    else: print("Incorrect Password!")
else: print("Invalid username!")

#🔻Example 2: Check if a student passed and got A+ grade
marks = int(input("Enter your marks: "))
if marks >= 50:
    if marks >= 90:
        print("You got A+ grade.")
    else: print("But no A+ grade.")
else:
    print("You failed.")

#🔻Example 3: Age verification + nationality check
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")
if age >= 18:
    if nationality == "pakistani":
        print("You are eligible to vote in Pakistan.")
    else: print("Only Pakistani citizens can vote.")
else:
    print("You are underage.")