# Datatypes:
# strings - "hello"
# interger / floats - 2, 2.4
# boolean - True or False

# Naming variables
# use underscores, no capitalization
# my_first_variable = "Olivia"

# Escaping
# example: want to save the word 'it's' as a variable
# 'it/'s' - the back slash tells use the character you see, not interpret it as something else

# Knowing what datatype you're dealing with, use type
print(type('hello'))
print(type(1))
print(type(1.64))
print(type(True))

# Typecasting / changing the type
# str()
# int()

# Arithmetic operations
a = 6
b = 2
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

# Strings
msg = 'welcome to Python 101: Strings'
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())  # only the first letter
print(msg.title())  # capitalize each letter
print(len(msg))  # length of string
# count different to len/length
print(msg.count('python'))  # returns 0 because its case sensitive
print(msg.count('Python'))  # 1, counts instances

# Slicing (strings)
# starts at 0
print(msg[0])  # returns w
print(msg[-1])  # gives the last character
print(msg[2:] + " this")  # grabs everything AFTER the 2nd character (e)
print(msg[2:15])  # the 15 is specifing an endpoint, after 2nd and stops at 15th character

one = msg[18]
print(one)
welcome = msg[0:7]
print(welcome)
to = msg[8:10]
print(to)
msg1 = msg[18] + ' ' + msg[:8] + msg[25:29] + msg[7:11] + 'Tyler'
print(msg1.title())  # 1 Welcome Ring To Tyler
print(msg[::-1].title())  # prints string backwards

# Replace
txt = "Hello my name is Olivia"
print(txt.replace("Olivia", "Liv"))

# Membership 'in'
print("Hello" in txt)  # True
print("food" in txt)  # False

# Formatting
name = 'TERRY'
color = 'RED'
sentence = '[' + name + '] loves the color ' + color.lower() + '!'
# formatted, dont forget the 'f'
sentence1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(sentence)
print(sentence1)

# User Input

# name = input("What is your name?: ")
# age = input("whats your age?: ")
# print(f"Hello, {name}. You are {age} years old")

# num1 = int(input("Enter a digit: "))
# num2 = int(input("Enter a second number: 5"))
# answer = num1+num2
# print(answer)

# Lists
friends = ["allie", "john", "bee", "amy", "lia"]
print(friends[2])
print(friends[2:5]) # after the 2nd, counting from 1 not zero
print(len(friends)) #5
print(friends.index("bee")) #2, counting from 0 when its index
print(friends.count("lia"))

numbers = [1, 100, 3, 300, 4, 500, 11]

numbers.sort() # sorts in place
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Adding to the list
numbers.insert(1, 900)  # inserted at position/index 1, its still in reverse from the above
print(numbers)

# Copy list
new_numbers = numbers.copy() # difference between copy v deep copy?

# list exercise

# sales_w1 = [7, 3, 42, 19, 15, 35, 9]
# sales_w2 = [12, 4, 26, 10, 7, 28]
# sales = []

# new_day = int(input("how many did you sell?: "))
# sales_w2.insert(7, new_day)
# print(sales_w2)

# sales = sales_w1 + sales_w2
# print(sales)

# best_day = max(sales)
# worst_day = min(sales)
# print(1.5 * best_day)
# print(1.5 * worst_day)

# Split and join

aa = "Welcome Olivia, how are you"
print(list(aa))  # splits each character including empty spaces
print(aa.split())  # splits words into a list/array

# Tuples & Sets
# Tuples - faster Lists you can't change, immutable
# Sets - unordered, removes any duplicates, faster at finding members inside than lists are
friends1 = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Eric'}
print(friends1)
print(friends_tuple)
print(friends_set)

# Print names that are in both - 'Intersection'
# first_comparison_variable.intersection(second_comparison_variable)

my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}

print(friends_set.intersection(my_friends_set))

# Sets exercise
# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. Create a new cars-list without duplicates

friends2 = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996','V90', '911', '911', 'S', '328', '900']

# 1
print('Eric' in friends2 and 'John' in friends2)

# 2 - how to combine SETS, unordered and no duplicates -  shorter way, | means union
print(friends2.union(my_friends))
print(friends2 | my_friends)

# 3
print(friends2.intersection(my_friends))
print(friends2 & my_friends)

# 4
cars_no_dupl = set(cars)
print(cars_no_dupl)
