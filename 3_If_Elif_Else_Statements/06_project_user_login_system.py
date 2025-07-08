# Project: Simple User Login System using if-elif-else
# This project will clear all concept about conditional statements.

#-----------------------------------------
# stored credentials
correct_username = "python"
correct_password = "python@123"
# Input form user

username = input("Enter username: ")
password = input("Enter password: ")

if correct_username == "" or correct_password == "":
    print("Username or Password can not be empty!")
elif username == correct_username and password == correct_password:
    print("Login successful!")
elif username != correct_username and password == correct_password:
    print("Incorrect username.Try again!")
elif username == correct_username and password != correct_password:
    print("Incorrect password.Try again!")
else:
    print("Both username and password are incorrect.")