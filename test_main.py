import unittest
from main import input_into_entry
point_count = 0
class Testinput_into_entry(unittest.TestCase):

    def test_input(self):
        if 1 == '0' or 1 == '':
            print(1)
        else:
            print(1)

    def test_input_point(self):
        global point_count
        if point_count == 0 and '' == '':
            point_count = point_count + 1
            print('0' + '.')
        elif point_count == 0:
            point_count = point_count + 1
            print('.')

    def test_plus_minus(self):
        if 1 != '0':
            if float(1) > 0:
                print(str('-' + '1'))
            else:
                print(1)
