USERNAME = "admin"
PASSWORD = "12345"

input_user = str(input("Username: "))
input_pass = str(input("Password: "))

valid_user = input_user == USERNAME
valid_pass = input_pass == PASSWORD
access_granted = valid_user and valid_pass

if access_granted:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
    if not valid_user:
        print("Invalid username!")
    if not valid_pass:
        print("Invalid password!")