# Topic: Logical Operators in Python (and,or,not)
# These operators are used to combine multiple conditions.

#-------------------------------------------------------------
#🔻Example 1: Use of 'and' operator
# Condition is True only if both parts are True.

# 'and' concept:
# false | false = false 
# false | true  = false
# true  | false = false
# true  | true  = true
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").lower()

if age >=18 and nationality == "pakistani":
    print("You are eligible to vote in Pakistan.")
else:
    print("You are not eligible to vote.")

#-------------------------------------------------------------
#🔻Example 2: Use of 'or' operator
# Condition is True only if any one part is True.

# 'or' concept:
# false | false = false 
# false | true  = true
# true  | false = true
# true  | true  = true
day = input("Enter today's day: ").lower()
if day == "saturday" or day == "sunday":
    print("It's weekend!")
else:
    print("It's working day.")

#-------------------------------------------------------------
#🔻Example 3: Use of 'not' operator
# It reverses the result of a condition.

# 'not' concept:
# false | true
# true  | false
is_raining = input("Is it raining? (yes/no): ").lower()
if not is_raining == "yes":
    print("You can go outside.")
else:
    print("Stay indoors.")