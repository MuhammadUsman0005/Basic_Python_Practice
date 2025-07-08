# Topic: break and continue statements in while loops
# 'break' stops the loop completely
# 'continue' skips current loop step and goes to next iteraion

#-------------------------------------------------
#🔻Example 1: Use of break
print("Counting until user enters 0:")
while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        print("Loop stoped by user.")
        break
    print("You entered: ",number)

#-----------------------------------------------
#🔻Example 2: Use of continue
num = 0
while num < 10:
    num += 1        # move to next number
    if num % 2 == 0:
        continue
    print("Odd number: ",num)

#---------------------------------------------------
#🔻Example 3: Password checker with limited tries
correct_password = "python@123"
attempt = 0
while attempt < 3:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("Access Granted!")
        break
    else: print("Wrong Password! Try again!")
    attempt += 1
if attempt == 3:
    print("Too many wrong attempts. Access denied.")
