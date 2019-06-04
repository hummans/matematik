# Title: Arithmetic Multiplication
#
# Desc: In this module you can find functions for multiplyin up different types
#       integers inside different objects and data structures
#
# Authors: Demir Antay -- demir99antay@gmail.com -- @demirantay
#


def multiply(num1, num2):
    '''
    definition: name(arg1, arg2)
    objective : returns the multiplication of two arguments
    '''
    return num1 * num2


def multiply_nums(*args):
    '''
    definition: name(*args, . . .) {...}
    objective : you can give as many arguments as you want to this function
                e.g. func(1, 5, 6) or func(9, 1002, 234)
    '''

    result = 1

    for argument in args:
        result *= argument

    return result


def arr_multiply(array):
    '''
    definition: func( array[] ) {...}
    objective : multiplies every element in the given array
    '''

    result = 1

    for element in array:
        result *= element

    return result


def tup_multiply(tuple):
    '''
    definition: func(tuple) {...}
    objective : multiplies every element in the given tuple
    '''

    result = 1

    for element in tuple:
        result *= element

    return result
