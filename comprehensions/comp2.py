# DICTIONARY COMPREHENSIONS

movies = ["And Now for Something Completely Different", "Monty Python and the Holy Grail",
          "Monty Python's Life of Brian", "Monty Python Live at the Hollywood Bowl", "Monty Python's The Meaning of Life", "Monty Python Live (Mostly)"]

year = [1971, 1975, 1979, 1982, 1983, 2014]

names = ['John', 'Eric', 'Michael', 'Graham', 'Terry', 'TerryG']

# movie and year combined as tuples
print(list(zip(movies, year)))

# dict comprehension
# give me a dict('movies': year) for each movies, year in zip(movies, year)
print("--------------")

# dict {}, movie:yr are the parameters, for movie, yr (also a paramaters) in zip movies year, the real named variables
new_dict = {movie:yr for movie, yr in zip(movies, year)}
print(new_dict)

# movies before 1983

new_dict1 = {movie:yr for movie, yr in zip(movies, year) if yr < 1983}
print(new_dict1)

# movies before 1983 and start with python
# new method on strings: .startswith("")
print("--------------")
new_dict2 = {movie:yr for movie, yr in zip(movies, year) if yr < 1983 and movie.startswith('Monty')}
print(new_dict2)

# concatinating with persons fave
print("--------------")
n1 = [[name + "s fave movie was " + movie + " from " + str(yr)] for name, movie, yr in zip(names, movies, year) if yr < 1981]
print(n1)