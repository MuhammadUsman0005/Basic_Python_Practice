# Topic: Real Life Programs using for loop
# These examples show how 'for' loop is used in practical scenarios.

#🔻Program 1: Multiplication Table
num = int(input("Enter a number to generate table: "))
print(f"\nMultiplication Table of {num}:")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
#______________________________________________________

#🔻Program 2: Sum of even numbers form 1-100
even_sum = 0
for i in range(2,101,2):
    even_sum += i
print("\nSum of even numbers (1-100): ",even_sum)
#-----------------------------------------------------

#🔻Program 3: Factorial of a number
num = int(input("Enter a number for factorial: "))
factorial = 1
for i in range(1,num + 1):        
    if num == 0:
        print("Enter a number greater than 0!")
    else:
        factorial *= i     # Factorial: e.g. 5! = 5x4x3x2x1
print(f"Factorial of {num} is {factorial}.")
#--------------------------------------------------------------

#🔻Program 4: Password validator (check for digit and length)
password = input("Enter your password: ")
has_digit = False
for i in password:
    if i.isdigit():
        has_digit = True
        break
if len(password) >= 8 and has_digit:
    print("Strong Password!")
else:
    print("Weak Password. Use at least 8 characters and include a digit.")
#------------------------------------------------------------------

#🔻Example 5: Count how many digits are in a sentence
text = input("Enter a sentence with numbers: ")
number_count = 0
for ch in text:
    if ch.isdigit():
        number_count += i
print("Total digits in the sentence: ",number_count)
