import unittest


def area(width, height):
    if not (isinstance(width, (int, float)) and
            isinstance(height, (int, float))):
        raise TypeError('The numbers must be of type int or float.')
    if not (width > 0 and height > 0):
        raise TypeError('The width and height must be positive numbers.')

    return width * height


class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 5), 20, 'message')


if __name__ == '__main__':
    unittest.main(verbosity=2)
