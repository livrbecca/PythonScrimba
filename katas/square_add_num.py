
# print(2**2)

# square the numbers, put them in a list

# add up the numbers in that list


def sq(numbers):
    sq_list = []
    for n in numbers:
        sq_num = pow(n, 2)
        sq_list.append(sq_num)
        total = sum(sq_list)
        print(total)


sq([1, 2, 3])
