# Find max item in list

# function:
# =========
# name: maxInList

# parameter: numbers: list of numbers

# return type: number

# pseudo code:
# ============
# set biggest to first number in list
# for each number n in list
# 	if n is greater than biggest
# 		set biggest to n
# return biggest

def maxInList(arr):
    biggest = arr[0]
    for n in arr:
        if n > biggest:
            biggest = n
    print(biggest)


maxInList([256, 124, 84, 649, 967, 598, 49, 52])
