# Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the array, return -1.

# Examples:

# csWhereIsBob(["Jimmy", "Layla", "Bob"]) ➞ 2
# csWhereIsBob(["Bob", "Layla", "Kaitlyn", "Patricia"]) ➞ 0
# csWhereIsBob(["Jimmy", "Layla", "James"]) ➞ -1
# Notes:

# Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB" or "bob").

#SOLUTION

def csWhereIsBob(names):
    name = "Bob"
    if name in names:
        return names.index(name)
    else:
        return -1
