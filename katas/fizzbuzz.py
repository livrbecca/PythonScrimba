# fizz buzz: output the correct responses to the first 100 numbers in the game fizz buzz

# function fizzbuzz

# 	  for number n from 1 to 100

# 		    set print_number to true

# 		    if n is divisible by 3 then
# 			      print "Fizz"
# 			      set print_number to false

# 		    if n is divisible by 5 then
# 			      print "Buzz"
# 			      set print_number to false

# 		    if print_number then
# 						print n

# 		    print a newline

def fizzbuzz():
    for n in range(1, 101):
        print_number = True
        if n % 3 == 0:
            print("Fizz")
            print_number = False
        if n % 5 == 0:
            print("Buzz")
            print_number = False
        if print_number:
            print(n)
        print("\n")

fizzbuzz()