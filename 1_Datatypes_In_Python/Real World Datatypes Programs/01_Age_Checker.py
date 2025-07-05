age = int(input("Enter your age: "))

is_adult = age >=18           # here is fixed value which is age greater than 18 or equal to 18
print(f"Age: {age} (Type: {type(age)})")    # f"string  {variable}" -> in this template we can display string and variable both together.
print(f"Adult status: {is_adult} (Type: {type(is_adult)})")

if is_adult:              # if age >= 18
    print("You can vote.")
else:
    years_left = 18 - age
    print(f"Wait {years_left} years to vote")