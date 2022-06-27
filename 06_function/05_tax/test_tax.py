import unittest
from tax import calc_tax


class TestTax(unittest.TestCase):

    def test_calc_tex_with_incorrect_age_type(self):
        self.assertRaises(TypeError, calc_tax, 100, 0.23, 3.01)

    def test_calc_tex_with_negative_age_value(self):
        self.assertRaises(ValueError, calc_tax, 100, 0.23, -10)

    def test_calc_tex_with_correct_tex_value_at_age_under_18(self):
        self.assertEqual(calc_tax(1000, 0.10, 16), 100)

    def test_calc_tex_with_correct_tex_value_at_age_under_18_tax_up5000(self):
        self.assertEqual(calc_tax(12000, 0.50, 16), 5000)

    def test_calc_tex_with_correct_tex_value_at_age_under_65(self):
        self.assertEqual(calc_tax(1000, 0.10, 60), 100)

    def test_calc_tex_with_correct_tex_value_at_age_above_65(self):
        self.assertEqual(calc_tax(1000, 0.10, 66), 100)

    def test_calc_tex_with_correct_tex_value_at_age_above_65_tax_up8000(self):
        self.assertEqual(calc_tax(17000, 0.50, 66), 8000)
