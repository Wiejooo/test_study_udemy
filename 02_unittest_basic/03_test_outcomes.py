import unittest


def area(width, height):
    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The numbers must be of type int or float.')
    if not (width > 0 and height > 0):
        raise ValueError('The width and height must be positive numbers.')

    return width * height


class TestArea(unittest.TestCase):

    def test_area_1(self):
        self.assertEqual(area(4, 5), 20, 'message')

    def test_area_2(self):
        self.assertEqual(area(4, 5), 21, 'message')

    def test_area_3(self):
        raise AssertionError('Error massage.')

    def test_area_4(self):
        raise TypeError('Error massage.')


if __name__ == '__main__':
    unittest.main(verbosity=2)
