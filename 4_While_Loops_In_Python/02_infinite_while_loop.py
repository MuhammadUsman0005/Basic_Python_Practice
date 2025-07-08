# Topic: Infinite While Loop in Python
# An infinite loop runs forever unless we stop it manually.
# We usually avoid them unless we use 'break' or some exit condition.

# --------------------------
#🔻Example 1: Truly infinite loop (Use Ctrl+C to stop)

# WARNING: This will run forever unless manually stopped
# Uncomment to test carefully!
# while True: 
#     print("♾ This is an infinite loop!")
#----------------------------------------------------

#🔻Example 2: Infinite loop with exit option

while True:
    user = input("Type 'exit' to stop: ")
    if user.lower() == "exit":
        print("Loop ended by user.")
        break
    print("Loop is still running...")

#🔻Example 3: Fun counter loop
count = 1

while True:
    print("Count: ",count)
    count += 1
    if count >10:
        print("Stopped after 10 counts")
        break