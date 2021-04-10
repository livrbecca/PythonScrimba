for letter in "my hero academia":  # could use any word, not just letter
    print(letter)

print("for loop done")

for num in range(8):
    print(num)
print("for loop2 done")

# range, up to 8 but not
# doing range(2,8) would print from 2 up till 8 but not including 8
# doing range(1, 15, 3) would do the same in steps of 3


friends = ['John', 'Terry', 'Eric', 'Bob', 'George']
for friend in friends:
    print(friend)

print("For Loop3 done!")


# break vs continue statements

friends = ['John', 'Terry', 'Eric', 'Bob', 'George']
for friend in friends:
    if friend == "Eric":
        print(f"Found {friend}!")
       # break
        continue
    print(friend)

print("For Loop3 done!")


# nested loop

friends = ['John', 'Terry', 'Eric']
for friend in friends:
    for number in [1, 2, 3]:
        print(friend, number)


print("For Loop4 done!")

# Exercise

names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

all_names = names + names1
# alternative methods: 
# names.extend(names1)
# names += names1

for index in range(2): # 0, 1, exclude 2
    all_names.append(input('Enter a new name: '))

# alternative method
#guest1 = input("add name to list: ")
#guest2 = input("add another name to list: ")
# all_names.insert(0, guest1)
# all_names.insert(1, guest2)
# print(all_names)

for name in all_names:
    print(f"Dear {name.title()}, you have been invited")
