# Concept: String indexing and slicing
'''
1.📌Indexing:
Each character in a string has a position (index).
Indexing starts form 0 (left to right), and -1 (rigth to left). 
'''
name = "Python language"
# indexing position (positive)
print("First letter: ",name[0])       # P
print("Fifth letter: ",name[5])       # n

# indexing position (negative)
print("Last letter: ",name[-1])       # e
print("Second letter: ",name[-2])     # g


'''
📌 Slicing:
It gives a part(slice) of the string.
Stop is not included. space is also count.
string[start:stop]      start (inclusive)  stop(exclusive)
'''
print("First name: ",name[0:6])         # Python
print("Last word: ", name[7:15])        # language

'''
Advanced Slicing:
string_name[start:stop:step]
'''
# step slicing                                     
print("Every second character: ",name[::2])     # Pto agae
# Reversed the string
print("Reversed: ",name[::-1])          # egaugnal nohtyP

'''
📌 Shortcuts:
- name[:]    -> full string
- name[::-1] -> reverse string
- name[:n]   -> first n characters
- name[-n:]  -> last n characters
'''

print("First 5 letters: ", name[:6])     # Python
print("Last 8 letters: ",name[-9:])      # language