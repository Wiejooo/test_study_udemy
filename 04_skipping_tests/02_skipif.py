import unittest
from datetime import date


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipIf(date.today().day % 2 != 0, f'Skipping odd days. It is {date.today().day}')
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipIf(date.today().day % 2 == 0, f'Skipping even days. It is {date.today().day}')
    def test_case_3(self):
        self.assertEqual('aws'.upper(), 'AWS')
