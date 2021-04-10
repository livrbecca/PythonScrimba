# sort vs sorted

my_list = [1,5,3,7,2] #mutable, can change them
my_dict = {'car':4,'dog':2,'add':3,'bee':1} #mutable
my_tuple = ('d','c','e','a','b') #immutable
my_string = 'python' #immutable

# lists
# sort - doesn't return anything, just sorts the list
# sorted - function, returnd new object that has been sorted

print(my_list,'original')
#my_list.sort()
#print(my_list,'with sort()')
print(sorted(my_list), "with sorted function")

# sorting a list of lists

my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_llist)) # sorted by first element, follows a, b, c order

# lambda

my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]

print(sorted(my_llist, key = lambda item : item[2]))
# item[] is where you specificy which item in the list you want to sort on
# 0 is words
# 1 is the middle digit
# 2 is the last