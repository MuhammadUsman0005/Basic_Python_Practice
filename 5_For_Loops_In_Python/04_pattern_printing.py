# Topic: Pattern Printing uisng nested for loops
# Patterns help improve logic and loop understanding.
#------------------------------------------------------

#🔻Pattern 1: Right-Angle Traingle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*",end= " ")
    print()
# OUTPUT:
# *
# * *
# * * *
# * * * *
# * * * * *
#----------------------------------------------

#🔻Pattern 2: Right-Angle Traingle (A,B,C...)
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
#-------------------------------------------

#🔻Pattern 3: Right-Angle Traingle (numbers)
for i in range(1,rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")  
    print()
# OUPUT:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#----------------------------------------------

#🔻Pattern 4: Inverted Traingle
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
# OUTPUT:
# * * * * *
# * * * *
# * * *
# * *  
# * 
#--------------------------------------

#🔻Pattern 5: Pyramid Shape
for i in range(1,rows + 1):
    for space in range(rows - 1): # print spaces
        print(" ",end=" ")
    for star in range(2 * i - 1): # print stars
        print("*",end=" ")
    print()
# OUTPUT:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *