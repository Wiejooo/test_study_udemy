import unittest

from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up class...')
        cls.calc = SimpleMathCalculator()

    @classmethod
    def tearDownClass(cls):
        print('tearing down class...')
        del cls.calc

    def test_add(self):
        self.assertEqual(self.calc.add(4, 7), 11)

    def test_sub(self):
        self.assertEqual(self.calc.sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(self.calc.mul(10, 5), 50)
