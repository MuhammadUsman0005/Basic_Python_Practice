# Project: Number Guessing Game using while loop
# We will use random module to select a number.

import random           # for generating random number
# Step I: Generate a random number from 1 to 10.
secret_number = random.randint(1,10)
# Step II: Set tries
tries = 0

print("WELCOME TO NUMBER GUESSING GAME!")
print("I'm thinking of a number between 1 and 10.")

# Step III: Loop until user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    tries += 1
    if guess == secret_number:
        print(f"Correct! You guessed it in {tries} tries.")
        break
    elif guess < secret_number:
        print("Try a higher number!")
    else:
        print("Try a lower number!")
print("GAME OVER!")