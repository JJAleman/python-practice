"""
Challenge #7:
Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).
Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
def nth_smallest(lst, n):
    # Your code here
    if n > len(lst):
        return None
    #this sorts in place
    lst.sort()
    print(lst)

    #we do n-1 because we need to start at 0
    return lst[ n - 1]

    #another way to sort created another list sorted
    # sorted(lst)

print(nth_smallest([7, 5, 3, 1], 1))
print(nth_smallest([1, 3, 5, 7], 5))