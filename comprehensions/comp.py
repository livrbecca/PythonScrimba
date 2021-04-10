# LIST COMPREHENSIONS

numbers = [1,2,3,4,5,6,7,8,9]

new_list = []

# squaring the numbers and inserting them into the new array

for num in numbers:
    new_list.append(num*num)
print(new_list)


# comprehension version 

new_list1 = [num*num for num in numbers]
print(new_list1)

# give me a list with num for each num in numbers if num is even

# attempt 1, returns Booleans
new_list2 = [num % 2 == 0 for num in numbers]
print(new_list2)

# returns even numbers
new_list3 = [num for num in numbers if num % 2 == 0 ]
print(new_list3)

# return odd numbers
new_list4 = [num for num in numbers if num % 2 != 0 ]
print(new_list4)

# using filter / lambda
new_list5 = filter(lambda num: num % 2 == 0, numbers)
print(list(new_list5))


# I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
# comprehensions
# ask where num came from

new_list6 = [(letter, num) for letter in 'spam' for num in range(4)]
print(new_list6)


# DICTIONARY COMPREHENSIONS

movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
"Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]

year =[1971,1975,1979,1982,1983,2014]

names = ['John','Eric','Michael','Graham','Terry','TerryG']

print(list(zip(movies, year)))