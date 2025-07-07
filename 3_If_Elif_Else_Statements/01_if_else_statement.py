# Topic: if-else Statement in Python
# The 'if' block runs when the condition is True.
# The 'else' block runs when the condition (if) is False.

#🔻Example 1: Check even or odd number
number = eval(input("Enter a number: "))   #eval()  function can take all type of datatype

if number % 2 == 0:
    print("This is an EVEN number.")    # indentation is very important in Python.
else:
    print("This is an ODD number.")
#------------------------------------------
#🔻Example 2: Check age for voting.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#🔻Example: 3 check password match or not
password = input("Enter password: ")
if password == "python@124":
    print("Access Granted!")
else:
    print("Wrong Password!")
    