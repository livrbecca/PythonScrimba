# Make a string by repeating letter x, n times

# pseudo code:
# ============
# set outputString to be an empty string

# for 1 to count

# 	append character to end of outputString

# return outputString


# method 1
def repeatString(character, count):
    outputString = ""
    new_string = character * count
    outputString += new_string
    print(outputString)


repeatString("A", 3)


# method 2

def repeatString2(charcter, count):
    outputString = ""
    for num in range(1, count):
        outputString += charcter
    print(outputString)


repeatString2("B", 4)


