# Topic: Looping through strings using for loop
# A string is a sequence of characters, and we can loop through each character one by one using a 'for' loop.
#---------------------------------------------------

#🔻Example 1: Print each character of a string
name = "Usman"
for char in name:
    print("Letter: ",char)
# OUTPUT:
# Letter: U
# Letter: s
# Letter: m
# Letter: a
# Letter: n
#-------------------------------------------------------

#🔻Example 2: Print how many vowels are in the string
text = "Welcome to Python Programming language"
vowel_count = 1
for vowel in text:
    if vowel.lower() in "AEIOUaeiou":
        vowel_count += 1
print("Total vowels: ",vowel_count)
#--------------------------------------------------

#🔻Example 3: Reverse a string using loop
word = "Python"
reversed_word = ""
for ch in word:
    reversed_word = ch + reversed_word
print("Orignal: ",word)
print("Reversed: ",reversed_word)
#----------------------------------------------

#🔻Example 4: Replace all spaces with dashes
sentence = "I am learning Python."
new_sentence = ""
for ch in sentence:
    if ch == " ":
        new_sentence += "-"
    else:
        new_sentence += ch
print("Modified sentence: ",new_sentence)
#-----------------------------------

#🔻Example 5: Print only digits from a string
data = "My age is 21 and my roll is 02221"
for ch in data:
    if ch.isdigit():
        print("Digit found: ",ch)