# soemtimes you may want to combine itterables (things you can itterate through)

nums = [1, 2, 3, 4]
letters = ['a', 'b', 'c', 'd']
names = ['John', 'Eric', 'Michael', 'Graham', 'Joe']

combo = list(zip(nums, letters, names))
# can also use dict instead of list bt only for key:value
print(combo)
# matches the tuples by index number

#unzip *
num, let, nam = zip(*combo)
print(num, let, nam)


# Translation app

keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'
keys = keys.split()
values = values.split()
print(keys, values)

en_sv_dict = dict(zip(keys, values))
print(en_sv_dict)

# dictionary comprehension, second method
# unsure of this one, ask isabel
new_dict = {key:value for key, value in zip(keys, values)}
print(new_dict)

#unzipping method 1
en, sv = list(en_sv_dict.keys()), list(en_sv_dict.values())
print(en, sv)

#unzipping method 2

en1, sv1 = zip(*en_sv_dict.items())
print(en1, sv1)
