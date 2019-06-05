import unittest
from matematik.arithmetic.add import add, add_nums, arr_sum, tup_sum


class Test_add(unittest.TestCase):
    '''
    testing the function: add() inside the module: add.py
    '''

    def test_if_returning_type_is_int(self):
        self.assertEqual(type(add(1, 1)), type(2))

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(add(5, 10), 15)

    def test_if_it_works_with_negative_nums(self):
        self.assertEqual(add(-10, -7), -17)


class Test_add_nums(unittest.TestCase):
    '''
    testing the function: add_nums() inside the module: add.py
    '''

    def test_if_reurning_type_is_int(self):
        self.assertEqual(type(add_nums(1, 1)), type(2))

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(add_nums(10, 10, 20), 40)

    def test_if_it_works_with_negative_nums(self):
        self.assertEqual(add_nums(-10, -5, 11), -4)


class Test_arr_sum(unittest.TestCase):
    '''
    testing the function: arr_sum() inside the module: add.py
    '''

    def test_if_test_if_returning_type_is_int(self):
        self.assertEqual(type(arr_sum([1, 1, 1])), type(3))

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(arr_sum([10, 5, 15]), 30)

    def test_if_it_works_with_negative_nums(self):
        self.assertEqual(arr_sum([10, -15, -10, 5]), -10)


class Test_tup_sum(unittest.TestCase):
    '''
    testing the function: tup_sum() inside the module: add.py
    '''

    def test_if_reurning_type_is_int(self):
        self.assertEqual(type(tup_sum((1, 1, 1))), type(10))

    def test_if_function_returns_a_true_value(self):
        self.assertEqual(tup_sum((10, 15)), 25)

    def test_if_it_works_with_negative_nums(self):
        self.assertEqual(tup_sum((-10, 10, -5)), -5)


if __name__ == "__main__":
    unittest.main()
