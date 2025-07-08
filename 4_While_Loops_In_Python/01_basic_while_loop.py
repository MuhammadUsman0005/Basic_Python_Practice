# Topic: Basic While Loop in Python
# A while loop repeats a block of code as long as the condition is True.

#--------------------------------------------------
#🔻Example 1: Print numbers form 1 to 5
count = 1
while count <= 5:          # condition check
    print("Number: ",count)
    count += 1          # increases the counter by 1 in every loop

#--------------------------------------------------
#🔻Example 2: Ask the user to enter "yes" to continue
user_input = ""
while user_input != "yes":
    user_input = input("Type 'yes' to exit the loop: ")
print("Loop ended because you typed 'yes'.")
# OUTPUT: Type 'yes' to exit the loop: hi
#         Type 'yes' to exit the loop: no
#         Type 'yes' to exit the loop: hello
#         Type 'yes' to exit the loop: yes
#         Loop ended because you typed 'yes'.

#--------------------------------------------------
#🔻Example 3: Coundown form 5 to 1
num = 5
while num >= 1:
    print("#",num)
    num -= 1
print("Coundown finished!")