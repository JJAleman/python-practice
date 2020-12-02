
"""
Challenge #6:
Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.
- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.
Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    # Your code here
    #this will work on a sting and lower the charaters sister function upper()
    txt_lower = txt.lower()
    return txt_lower.count('x') == txt_lower.count('o')

def XO(txt):
    #lower case our txx
    txt_lower = txt.lower()
    x_count = 0
    o_count = 0

    #loop over each char, and count x and o
    for char in txt_lower:
        #check if char is X or O
        if char == 'x':
            x_count += 1
        elif char == 'o':
            o_count += 1
    return x_count == o_count

print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))