import unittest

from calculator.calc_math import SimpleMathCalculator


def setUpModule():
    print('setting up...')
    global calc
    calc = SimpleMathCalculator()


def tearDownModule():
    print('tearing down...')
    global calc
    del calc


class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(4, 7), 11)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(calc.mul(10, 5), 50)

    def test_true_div(self):
        self.assertEqual(calc.true_div(10, 5), 2)

    def test_floor_div(self):
        self.assertEqual(calc.floor_div(10, 5), 2)
