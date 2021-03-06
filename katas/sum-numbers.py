# return sum of all numbers in list

# pseudo code

# function:
# =========
# name: sumList

# parameter: numbers: list of numbers

# return type: number

# pseudo code:
# ============
# set runningTotal to 0

# for each number n in numbers
# 	increment runningTotal by n

# return runningTotal


# method one

def sumList(arr):
    runningTotal = 0
    for n in arr:
        runningTotal += n
    print(runningTotal)


sumList([5, 10, 1])

# method two

def sumList2(arr):
    total = sum(arr)
    print(total)


sumList2([5, 10, 1])
