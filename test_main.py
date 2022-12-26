import unittest
import main


class Testinput_into_entry(unittest.TestCase):

    # substraction check
        def test_minus(self):
            main.operand1 = '-'
            self.assertTrue(float(main.equal) > 0)

    # division by zero
        def test_one(self):
            main.operand1 = '/'
            self.assertTrue((main.equal) == '∞')

    # multiplication of a negative number
        def test_multiplication_one_minus(self):
            main.operand1 = '*'
            self.assertTrue(float(main.equal) < 0)

    # multiplication of two negative numbers

        def test_multiplication_two_minus(self):
            main.operand1 = '*'
            self.assertTrue(float(main.equal) > 0)

    # check output after division
        def test_float_division(self):
            main.operand1 = '/'
            self.assertTrue(main.equal % 1 > 0)

