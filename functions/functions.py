# function exercise
def greeting(name="Jane", age=21, color="red"):
    print(
        f"Hello {name}, you are age {age} and will be {age + 1} years old next birthday")
    print(f"we hear you like the color {color}!")


# name = input("whats your name?: ").capitalize()
# age = int(input("whats your age?: "))
# color = input("favourite color?: ").lower()
# greeting(name, age, color)

# functions - named notation
# name your agruments so they can be input in any order
# example: greeting(age=27, name="brian",color="Blue")
# makes code more readable

# Return statements

def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return f"{amount, tax, total_amount}"


    # without return, it prints None
    # adding [] turned it into a list, can print parts of the list
    # {} turns it to a set, adding f"{xyz}"" turns to a string
price = value_added_tax(100)
print(price, type(price))

# Comparisons and Booleans

# = assign
# == compare
# != not equal
# <= less than or equal to
# >= greater than or equal to
# 'in' operator, denotes membership, also "not in"
print("o" in "John")
# Identity - checks if two values are identical using 'is'
a = [3, 7, 42]
b = a
print(a == b)  # True
print(a is b)  # True, occupy same memory space in the computer
# Booleans - 0's and empty objects = False, everything else is true

# Conditionals: if statements

is_raining = True
is_cold = False
print("Good morning")
if is_raining and is_cold:
    print("Bring umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring umbrella")
elif is_cold and not(is_raining):
    print("Bring a jacket")
else:
    print("Weather is mild")


amount = 59
if amount <= 50:
    print("purchase approved")
else:
    print("enter PIN")
