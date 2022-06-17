import unittest


def setUpModule():
    print('setting up module...')


def tearDownModule():
    print('tearing down module...')


class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John', 'Smith'])


class TestClass2(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('4.2'.split('.'), ['4', '2'])


class TestClass3(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual('#'.join(['sport', 'danger']), 'sport#danger')
