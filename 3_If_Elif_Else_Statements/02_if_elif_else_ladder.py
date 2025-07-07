# Topic: if-elif-else Ladder in Python

# Use this when there are multiple conditions to check 
# Only the first True condition will learn
# if 'if' condition False, then first elif condition will run, suppose if first elif conditon is False then next elif if all above conditone becomes False then else condtion will run.

#------------------------------------------------------
#🔻Example 1: Grading System
marks = eval(input("Enter your marks(0 to 100): "))

if marks >= 90:
    print("Grade: A+")
elif marks >=80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Failed")

#🔻Example 2: Traffic light color
color = input("Enter traffic light color: ")

if color == "red":
    print("Stop!")
elif color == "yellow":
    print("Get ready")
elif color == "green":
    print("Go!")
else:
    print("Invalid color")
