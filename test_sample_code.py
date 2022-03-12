"""
testing code for sample.
"""
import unittest
from sample_code import square


class TestSampleCode(unittest.TestCase):
    """
    unit testing class.
    """
    def test_square(self):
        """
        testing function for square
        """
        self.assertEqual(square(2),4)
        self.assertEqual(square(5),25)
        self.assertEqual(square(8),64)

if __name__ == '__main__':
    unittest.main()