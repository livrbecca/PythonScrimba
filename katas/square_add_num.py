
# print(2**2)

# square the numbers, put them in a list

# add up the numbers in that list

# method 2
def sq(numbers):
    sq_list = []
    total = 0
    for n in numbers:
        sq_num = pow(n, 2)
        sq_list.append(sq_num)
        total = sum(sq_list)
        print(total)


sq([1, 2, 3])


# method 1
def square_sum(numbers):
    array_of_num = []
    added = 0
    for n in numbers:
        sq = n**2
        array_of_num.append(sq)
        added = sum(array_of_num)
    print(added)


square_sum([])
