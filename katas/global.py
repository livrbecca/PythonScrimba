# GLOBAL
import global

livs_fave_number = 11


def example_one():
    print(f'my fave number is {livs_fave_number}')


example_one()


def example_two(n):
    print('lets do some addition:')
    print(f'{livs_fave_number + n}')


example_two(5)


def broken_example():
   global livs_fave_number 
   livs_fave_number = livs_fave_number + 3
   print(livs_fave_number)


broken_example()
