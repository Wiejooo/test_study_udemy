import unittest
from employee.emp import Employee


class TestEmployee(unittest.TestCase):

    def test_correct_email(self):
        emp = Employee('Jackob', 'Knowhow', 100000)
        self.assertEqual(emp.email, 'jackob.knowhow@mail.com')

    def test_correct_email_after_name_change(self):
        emp = Employee('Jackob', 'Knowhow', 100000)
        emp.first_name = 'Jakub'
        self.assertEqual(emp.email, 'jakub.knowhow@mail.com')

    def test_correct_email_after_surname_change(self):
        emp = Employee('Jackob', 'Knowhow', 100000)
        emp.last_name = 'Wiejak'
        self.assertEqual(emp.email, 'jackob.wiejak@mail.com')

    def test_correct_tax(self):
        emp = Employee('Jackob', 'Knowhow', 100000)
        self.assertEqual(emp.tax, 17000)

    def test_correct_bonus(self):
        emp = Employee('Jackob', 'Knowhow', 100000)
        emp.apply_bonus()
        self.assertEqual(emp.salary, 110000)
