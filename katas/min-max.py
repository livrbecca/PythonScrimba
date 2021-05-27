# find min AND max item in list

# pseudocode

# function:
# =========
# name: minAndMaxInList

# parameter: numbers: list of numbers

# return type: tuple (number, number)

# pseudo code:
# ============
# set biggest to first number in list
# set smallest to first number in list

# for each number n in list
# 	if n is greater than biggest
# 		set biggest to n
# 	if n is less than smallest
# 		set smallest to n

# return tuple of (smallest, biggest)

def minAndMaxInList(arr):
    biggest = max(arr)
    smallest = min(arr)

    for n in arr:
        if n > biggest:
            biggest = n
        elif n < smallest:
            smallest = n
    print({smallest, biggest})


minAndMaxInList([1,4,9,2,6,8,7])
