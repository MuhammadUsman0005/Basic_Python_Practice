# Topic: Nested For loop in Python
# A nested for loop means: one for loop inside another
# Mostly used for patterns,tables,grids,matrix,etc.
#---------------------------------------------------------

#🔻Example 1: Print a 3x3 grid using *
for i in range(3):     # outer loop rows
    for j in range(3):  # inner loop columns
        print("*",end=" ")
    print()          # move to next line after inner loop

# OUTPUT:
# * * *
# * * *
# * * *
#-------------------------------

#🔻Example 2: Print number pattern
for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()

# OUTPUT:
# 1 2 3
# 1 2 3
# 1 2 3
#---------------------------------------

#🔻Example 3: Multiplication Table (1 to 3)
for i in range(1,4):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}") 
    print("-"*20)      # line break between tables
#---------------------------------------------------

#🔻Example 4: Alphabet Traingle
rows = 5
for i in range(1,rows + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")  # chr(65) = A, 66 = B, etc.
    print()
# OUPUT:
# A
# A B
# A B C
# A B C D
# A B C D E