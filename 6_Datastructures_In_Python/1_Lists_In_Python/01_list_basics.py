# Topic: All important and basic list concepts in Python
# # A list is used to store multiple values in a single variable. It is created using square brackest: []

#🔻Example 1: Creating a simple list
fruits = ["apple","banana","mango","orange"]
print("My fruits list: ",fruits,type(fruits))
# OUTPUT: My fruits list: ["apple","banana","mango","orange"] <class 'list'>
#-------------------------------------------------

#🔻Example 2: A list can contain different data types
mixed_list = [12,"Usman","abc23","Python",True]
print(mixed_list)
#-------------------------------------------------

#🔻Example 3: Accessing list items using index
print("First fruit:", fruits[0])  # Index 0 = apple
print("Lase fruit:", fruits[-1])  # Index -1 = orange | negative index from end
#----------------------------------------------------

#🔻Example 4: Changing a value in the list
fruits[1] = "grapes"  # Change "banana" to "grapes"
print(fruits)       # ["apple","grapes","mango","orange"]
#-------------------------------------------------------

#🔻Example 5: Checking length of list
print("Total fruits in list: ",len(fruits))  # Total fruits in list: 4
#--------------------------------------------------------

#🔻Example 6: Check if an item exists in list
if "apple" in fruits:
    print("Apple is in the list.")
#----------------------------------------------------------

#🔻Example 7: Loop through list
for i,fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")