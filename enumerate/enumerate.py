print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

for friend in friends:
    print(friend)

# want them numbered

i = 0

for friend in friends:
    print(i, friend)
    i += 1

# want them numbered starting from 1 not 0

i = 1

for friend in friends:
    print(i, friend)
    i += 1

# using enumerate, nut starts from 0

for num, friend in enumerate(friends):
    print(num, friend)

# using option of introducing starting number

for num, friend in enumerate(friends, 1):
    print(num, friend)

# moving names lower down the list

for num, friend in enumerate(friends, 51):
    print(num, friend)
