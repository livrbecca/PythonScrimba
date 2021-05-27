# count number of vowels in a string


# function:
# =========
# name: isAVowel

# parameter: character: string

# return type: boolean

# pseudo code:
# ============
# if character is 'a' or 'e' or 'i' or 'o' or 'u'
# 	return true
# else
# 	return false

# alternative pseudo code:
# ========================
# return truth of (character is 'a' or 'e' or 'i' or 'o' or 'u')

# function:
# =========
# name: countVowels

# parameter: inputString: string

# return type: number

# pseudo code:
# ============
# set count to 0

# for each character in the string inputString
# 	if isAVowel(character)
# 		increment count by 1

# return count

def isAVowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if letter not in vowels:
        return False
    else:
        return True


def countVowels(inputStr):
    count = 0
    for letter in inputStr:
        if isAVowel(letter):
            count += 1
    print(count)


countVowels("Olivia")
