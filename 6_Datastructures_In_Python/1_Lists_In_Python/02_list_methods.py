# Topic: Useful list methods in Python
# Sample list for demonstration
sample_list = ["apple","banana","cherry","date"]
#--------------------------------------------------

#🔻Append method: Adds an item to the end of the list
sample_list.append("grapes")
print("After append: ",sample_list) # ['apple','banana','cherry','date','grapes']

#🔻insert() : Adds item at a specfic index
sample_list.insert(2,"orange")
print("After insert: ",sample_list) # ['apple',banana','orange','cherry','date','grapes']

#🔻extend(): Adds another list to the current list
sample_list.extend(["kiwi","mango"])
print("After extend: ",sample_list) # ['apple','banana','orange',cherry','date','grapes','kiwi','mango']

#🔻remove(): Removes first matching item
sample_list.remove("banana")
print("After remove: ",sample_list) # ['apple','orange','cherry','date','grapes','kiwi','mango']

#🔻pop(): Removes item at a given index (or last if no index given)
sample_list.pop(3)
print("After pop: ",sample_list) # ['apple','orange','cherry','grapes','kiwi','mango']

#🔻clear(): Removes all items from the list
sample_list.clear()
print("After clear: ",sample_list) # []

#🔻index(): Returns index of first matching item
index = sample_list.index("cherry")
print("Index of 'cherry': ",index) # Index of  'cherry': 2

#🔻count(): Counts how many times an item appears
print("Count of 'apple': ",sample_list.count("apple")) # Count of 'apple': 1

#🔻sort(): Sorts the list in ascendinig order
numbers = [3,6,2,7,8,1,5,4]
numbers.sort()
print("Sorted numbers: ",numbers) # [1,2,3,4,5,6,7,8]

#🔻reverse(): Reverses the order of the list
numbers.reverse()
print("Reversed numbers: ",numbers) # [8,7,6,5,4,3,2,1]