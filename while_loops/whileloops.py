# code that runs repeatedly until a condition tells it to stop

# Three Loop Questions:
# 1. What do I want to repeat?
#  -> message
# 2. What do I want to change each time?
#  -> starts
# 3. How long should we repeat?
#  -> 5 times

i = 0

while i < 5:
    i += 1
    print(f"{i}." + "*"*i + "loops are awesome" + "*"*i)


# Guessing game

num = 76
guess = 0
guess_limit = 5
guess_number = 0

guess = int(input(f"guess a number 1-100: "))
guess_number += 1 # to make it 5 guesses rather than 4 starting from 0

while guess_number < guess_limit:

    if guess != num:
        guess_number += 1
        if guess > num:
            guess = int(input(f"{guess} too high, try again: "))
        else:
            guess = int(input(f"{guess} too low, try again: "))
    if guess == num:
        print(f"congrats! you guessed {num} correctly")
        break

if guess != num:
    print(f"you lost, it was {num}")
