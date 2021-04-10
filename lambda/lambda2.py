def join_list_no_duplicates(list_a, list_b):
    return list(set(list_a + list_b))


list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6, 7]

print(join_list_no_duplicates(list_a,list_b))

# as a lambda

no_dupes = lambda list_a, list_b: list(set(list_a + list_b))
print(no_dupes(list_a, list_b))

# sorting exercise 

signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # Lexicographic sort

#write sorting by integer, so 2, 3, 17 etc
# bypass letters by slicing, 3rd  character to get to the first digit, specify no ending position
# want it to sort on intergers, so use int
print(sorted(signups, key = lambda id:int(id[3:]))) # Integer sort


# sorting exercise 2

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

player_list.sort(key = lambda player: player.score)
# can add reverse = True after player.score
print([player.name for player in player_list])