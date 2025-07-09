# Topic: Basic for loop in Pthon
# A 'for' loop is used to repeat a block of code for a fiexed number of times.
# Most commonly used with a function called 'range()'.

# range() function:
# range(start,stop)  ->  Loop from start to one before stop
# range(stop)        ->  Loop form 0 to stop-1
# range(start,stop,step)  -> Add a step for skipping or reversing
#---------------------------------------------------------

# 🔻Example 1: Print numbers from 1 to 5
# range(1,6) means: start from 1, go up to 5 (6 is not included)
for num in range(1,6):
    print("Number: ",num)
# OUTPUT:  
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5
#--------------------------------------------------------

#🔻Example 2: Print "Hello" 3 times
for i in range(3):        # range(3) means: 0,1,2 three times
    print("Hello!")
#------------------------------------------

#🔻Example 3: Count backwards (from 5 to 1)
for num in range(5,0,-1):  # step (-1) for reverse
    print("Countdown: ",num)
#----------------------------------------------

#🔻Example 4: Print only even numbers
for i in range(2,13,2):
    print("Even number: ",i)
#-----------------------------------------------

#🔻Example 5: Print name 5 times using a loop
name = "Usman"
for i in range(5):
    print(f"{i+1}. Your name is: ",name)