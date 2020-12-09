# Create a function that given an integer, returns an integer where every digit in the input integer is squared.

# Examples:

# csSquareAllDigits(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
# csSquareAllDigits(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9


# SOLUTION

def csSquareAllDigits(n):
    
    #given an intenger return every digit in the input squared
    
    newNum = [int(num)**2 for num in str(n)]
    
    res = int("".join(map(str, newNum)))
    
    return  res