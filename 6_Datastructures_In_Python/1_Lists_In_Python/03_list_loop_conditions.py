# Topic: Using lists with loops and conditions

#🔻Example 1: Loop through list and print items
fruits = ["apple","grapes","cherry","mango"]
print("Fruits in the basket:")
for fruit in fruits:
    print("-",fruit)
# OUTPUT: Fruits in the/ basket:
#         - apple
#         - grapes
#         - cherry
#         - mango

# -------------------------------
#🔻Example 2: Print only fruits that start with 'a'

print("\nFruits starting with 'a':")
for fruit in fruits:
    if fruit.startswith("a"):
        print(fruit)
# -------------------------------
#🔻Example 3: Check if item exists in list

user_fruit = input("\nEnter a fruit name: ")
if user_fruit in fruits:
    print("This fruit is in the basket!")
else:
    print("This fruit is not found.")
# -------------------------------
#🔻Example 4: Count even numbers in a list

numbers = [12, 45, 33, 22, 90, 5]
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("\nTotal even numbers:", even_count)

# -------------------------------
#🔻Example 5: Add only positive numbers from user input

user_numbers = []
print("\nEnter 5 numbers:")
for i in range(5):
    num = int(input(f"Number {i+1}: "))
    if num > 0:
        user_numbers.append(num)
print("Positive numbers you entered:", user_numbers)