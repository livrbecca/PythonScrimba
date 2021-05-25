# key:values pairs

movie = {
    'title': "Life of Brian",
    'year': 1979,
    'cast': ['John','Eric','Bob','George','Terry']
}

#print(movie)

#print(movie['title'])

#print(movie['budget'])

#print(movie.get('budget')) # get back 'None'

#set a default value
#print(movie.get('budget', 'not found, try again')) 

#update dictionary using [] notaton
movie['title'] = "Casablanca"
movie['budget'] = 250000 # added new entry to dictionary
print(movie)

#commands
#movie.update({})
#d el movie['year']
print(movie.items(), "items") # pair
print(movie.keys(), "keys") # left
print(movie.values(), "values") # right

#loop through items in D

for key, value in movie.items():
    print(key, value)

# putting dictionaries together, 3 methods

python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# method 1: use .update

people = {}
people1 = {}
people2 = {}

people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people)

# 2: comprehension

for groups in (python, holy_grail, life_of_brian) : people1.update(groups)
print(people1)

# 3: unpacking, **name, 

people2 = {**python,**holy_grail,**life_of_brian}
print(people2)

# finding sum of values
print('The sum of the ages: ', sum(people.values())) # works as they're all int's

