# single line function definitions

print('Lambda Functions')

# reg function 
def square(x):
    return x*x
print(square(3))

# Lambda
# name = lambda-parameter: expression
square1 = lambda x: x*x
print(square1(4))

# single line function definition
def square2(x): return x*x
print(square2(16))

# lambda 

db = lambda x, y: 2*x*y
print(db(10, 5))

# strip - Remove spaces at the beginning and at the end of the string
# reuglar function 
def name_and_alias(name, alias):
    return name.strip().title() + ':' + alias.strip().title()

print(name_and_alias(" OliviA Walker ", " rbecca"))

# as a Lambda

name_and_alias1 = lambda name, alias: name.strip().title() + ':' + alias.strip().title()
print(name_and_alias1(" OliviA ", "  ollY"))

# as one line function def

def name_and_alias2(name,alias): return name.strip().title() + ':' + alias.strip().title()
print(name_and_alias2("      oli", "ollY"))

# Sorting names function w lambda

people = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

people.sort(key = lambda name: name.split(" "))
# add [-1] to sort by last name
print(people)