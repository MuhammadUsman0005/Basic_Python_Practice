# Concept: String Formatting
# (Concatenating Text + Variables)

# Let's say we want to print welcome messages.
name = "Usman"
age = 19
city = "Peshawar"
# using + (concatenation)
# convert numberss to string using str()
print("Hello" +name + "! You are "+ str(age)+ "years old and live in "+city+" .")
# OUTPUT: Hello Usman! You are 19 years old and live in Peshawar.
'''
But there is a problem in this method, it becomes messy and harder to read
when variables increases.
'''
#-------------------------------------------------------------------------


# 🔻Using .format() method
print("Hello {}, you are {} years old and live in {}.".format(name,age,city))
# OUTPUT: Hello Usman! You are 19 years old and live in Peshawar.

# we can also use index numbers inside {}
print("Hello {0}, you are {1} years old and live in {2}.".format(name,age,city))
# OUTPUT: Hello Usman! You are 19 years old and live in Peshawar.

#--------------------------------------------------------------------

# 🔻Using f-strings (Recommended in Python latest version)
print(f"Hello {name}, you are {age} years old and live in {city}.")
# we can even use expressions inside f-strings
print(f"In 5 years, {name} will be {age + 5} years old.")
# OUTPUT: In 5 years, Usman will be 24 years old.