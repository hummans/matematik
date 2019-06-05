import unittest
from matematik.arithmetic.subtract import subtract, subtract_nums, arr_subtract
from matematik.arithmetic.subtract import tup_subtract


class Test_subtract(unittest.TestCase):
    '''
    testing the function: subtract() from module:subtract.py
    '''

    def test_if_the_returning_type_is_int(self):
        self.assertEqual(type(subtract(5, 2)), type(10))

    def test_if_the_funciton_returns_a_true_value(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_if_the_function_works_when_first_arg_is_negative(self):
        self.assertEqual(subtract(-10, 5), -15)


class Test_subtract_nums(unittest.TestCase):
    '''
    testing the function: subtract_nums() from module: subtract.py
    '''

    def test_if_the_returning_type_is_int(self):
        pass

    def test_if_the_funciton_returns_a_true_value(self):
        pass

    def test_if_the_function_works_when_first_arg_is_negative(self):
        self.assertEqual(subtract_nums(-100, 10, 10), -120)
