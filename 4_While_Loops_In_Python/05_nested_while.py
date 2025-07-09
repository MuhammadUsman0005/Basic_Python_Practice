# Topic: Nested While Loops in Python
# A while loop inside another while loop is called "nested loop"

# --------------------------
#🔹Example 1: Print square pattern of stars (5x5)

row = 1
while row <= 5:
    col = 1
    while col <= 5:
        print("*", end=" ")  # print stars in the same line
        col += 1
    print()  # move to next line after inner loop finishes
    row += 1

# --------------------------
#🔹Example 2: Multiplication table (1 to 3)

i = 1
while i <= 3:
    j = 1
    while j <= 10:
        print(f"{i} x {j} = {i*j}")
        j += 1
    print("-" * 20)
    i += 1

# --------------------------
#🔹Example 3: Simple Login Menu (until user logs in)

# Stored credentials
username = "usman"
password = "123"

while True:
    print("\nLogin Menu")
    user_input = input("Enter username: ")
    pass_input = input("Enter password: ")

    if user_input == username and pass_input == password:
        print("✅ Login successful!")
        
        # Now enter a nested menu
        while True:
            print("\nMenu:\n1. Say Hello\n2. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("Hello, Usman!")
            elif choice == "2":
                print("Logged out.")
                break  # exit inner loop (menu)
            else:
                print("Invalid choice")
        break  # exit outer loop (login)
    else:
        print("Invalid credentials. Try again.")