# make the largest number out of the input
# 54421

def des(num):
    num1 = str(num)
    num2 = sorted(num1)
    rev_num = num2[::-1]
    joined_nums = int("".join(rev_num))
    print(joined_nums)
   

des(1234)




# bus exercise 

# Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.

# Task Overview:
# You have to write a function that accepts three parameters:

# cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus excluding the driver.
# wait is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait):
    # cap = 20
    # on = 5
    # wait = 5
    
    sum = on + wait - cap
    
    if sum <= 0:
        return 0
    else:
        return sum
    
    # 5 + 5 - 20 