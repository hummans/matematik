import unittest
from matematik.formula.arithmetic import add, add_nums, arr_sum, tup_sum
from matematik.formula.arithmetic import subtract, subtract_nums, arr_subtract
from matematik.formula.arithmetic import tup_subtract, multiply, multiply_nums
from matematik.formula.arithmetic import arr_multiply, tup_multiply


class Test_add(unittest.TestCase):
    '''
    testing the function: add()
    '''

    def test_if_returning_type_is_int(self):
        self.assertEqual(type(add(1, 1)), type(2))

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(add(5, 10), 15)

    def test_if_it_works_with_negative_nums(self):
        self.assertEqual(add(-10, -7), -17)


class Test_add_nums(unittest.TestCase):
    '''
    testing the function: add_nums()
    '''

    def test_if_reurning_type_is_int(self):
        self.assertEqual(type(add_nums(1, 1)), type(2))

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(add_nums(10, 10, 20), 40)

    def test_if_it_works_with_negative_nums(self):
        self.assertEqual(add_nums(-10, -5, 11), -4)


class Test_arr_sum(unittest.TestCase):
    '''
    testing the function: arr_sum()
    '''

    def test_if_test_if_returning_type_is_int(self):
        self.assertEqual(type(arr_sum([1, 1, 1])), type(3))

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(arr_sum([10, 5, 15]), 30)

    def test_if_it_works_with_negative_nums(self):
        self.assertEqual(arr_sum([10, -15, -10, 5]), -10)


class Test_tup_sum(unittest.TestCase):
    '''
    testing the function: tup_sum()
    '''

    def test_if_reurning_type_is_int(self):
        self.assertEqual(type(tup_sum((1, 1, 1))), type(10))

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(tup_sum((10, 15)), 25)

    def test_if_it_works_with_negative_nums(self):
        self.assertEqual(tup_sum((-10, 10, -5)), -5)


class Test_subtract(unittest.TestCase):
    '''
    testing the function: subtract()
    '''

    def test_if_the_returning_type_is_int(self):
        self.assertEqual(type(subtract(5, 2)), type(10))

    def test_if_the_funciton_returns_a_true_value(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_if_the_function_works_when_first_arg_is_negative(self):
        self.assertEqual(subtract(-10, 5), -15)


class Test_subtract_nums(unittest.TestCase):
    '''
    testing the function: subtract_nums()
    '''

    def test_if_the_returning_type_is_int(self):
        self.assertEqual(type(subtract_nums(10, 5, 2)), type(10))

    def test_if_the_funciton_returns_a_true_value(self):
        self.assertEqual(subtract_nums(10, 2, 2, 2), 4)

    def test_if_the_function_works_when_first_arg_is_negative(self):
        self.assertEqual(subtract_nums(-100, 10, 10), -120)


class Test_arr_subtract(unittest.TestCase):
    '''
    testing the function: arr_subtract()
    '''

    def test_if_the_test_if_the_returning_type_is_int(self):
        pass

    def test_if_the_function_returns_a_true_value(self):
        pass


if __name__ == "__main__":
    unittest.main()
