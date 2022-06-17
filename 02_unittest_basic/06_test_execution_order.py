import unittest


class TestClass(unittest.TestCase):

    def test_case_4(self):
        self.assertTrue('apple'.islower())

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])

    def test_case_2(self):
        self.assertEqual('4.2'.split('.'), ['4', '2'])

    def test_case_3(self):
        self.assertEqual('#'.join(['sport', 'danger']), 'sport#danger')


