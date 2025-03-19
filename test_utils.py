# test_utils.py
import unittest
from utils import square, cube, is_even

class TestUtils(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-3), 9)

    def test_cube(self):
        self.assertEqual(cube(2), 8)
        self.assertEqual(cube(-3), -27)
    
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

if __name__ == "__main__":
    unittest.main()