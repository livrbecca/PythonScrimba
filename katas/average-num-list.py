# return average of all numbers in a list (add together then divide by how many)

# function:
# =========
# name: calculateAverage

# parameter: numbers: list of numbers

# return type: number

# pseudo code:
# ============
# set runningTotal to 0
# set count to 0

# for each number n in numbers
# 	increment runningTotal by n
# 	increment count by 1

# set average to runningTotal divided by count

# return average

def calculateAverage(arr):
    runningTotal = 0
    count = 0

    for n in arr:
        runningTotal += n
        count += 1
    average = runningTotal / count
    print(average)


calculateAverage([5, 5, 5, 5, 6])
