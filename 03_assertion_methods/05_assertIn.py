import unittest


class TestClass(unittest.TestCase):

    def test_case_01(self):
        self.assertIn('@', 'sample@email.com')

    def test_case_02(self):
        tech_stack = ['java', 'sql', 'python', 'aws']
        self.assertIn('python', tech_stack)

    def test_case_03(self):
        tech_stack = ['java', 'sql', 'python', 'aws']
        self.assertIn('c++', tech_stack)

    def test_case_04(self):
        tech_stack = {'java': 'mid', 'python': 'senior'}
        self.assertIn('java', tech_stack)

    def test_case_05(self):
        tech_stack = {'java': 'mid', 'python': 'senior'}
        self.assertNotIn('excel', tech_stack)

