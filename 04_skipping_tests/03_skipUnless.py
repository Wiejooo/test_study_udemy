import unittest
import sys


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('win'), f'It is not Windows, it is {sys.platform}')
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('linux'), f'It is not Linux, it is {sys.platform}')
    def test_case_3(self):
        self.assertEqual('aws'.upper(), 'AWS')
