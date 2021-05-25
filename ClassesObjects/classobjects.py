# Class - custom made data type, blueprint, make something out of it, an object
# classes are blueprints, objects are the actual things you build from the class
# variables are called attributes
# need to initialise the function
# mistake reminder: need a space after 'def'
# def = method
# self is a reference to the object thats active
class Movie:
    def __init__(self, title, year, score, have_seen):
        self.title = title
        self.year = year
        self.score = score
        self.have_seen = have_seen

    def nice_print(self):
        print("Title:", self.title)
        print("Year of production:", self.year)
        print("IMDB Score:", self.score)
        print("I have seen it:", self.have_seen)


film_1 = Movie("The Proposal", 2002, 7.2, True)
film_2 = Movie("Black Panther", 2019, 8.5, True)

print(film_1.title, film_1.score)
film_2.nice_print()  # called film_2 with the nice print method
films = [film_1, film_2]
films[0].nice_print()
