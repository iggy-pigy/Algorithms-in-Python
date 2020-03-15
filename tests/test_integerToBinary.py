import unittest

from integersToBinary._init_ import integerToBinary


class TestBinary(unittest.TestCase):
    def test_integer_7(self):
        """
        Test if integer in binary is 111
        """
        num = 7
        result = integerToBinary(num)
        self.assertEqual(result, 111)

    def test_integer_6(self):
        """
        Test if integer in binary is 11
        """
        num = 6
        result = integerToBinary(num)
        self.assertNotEqual(result, 111)


if __name__ == '__main__':
    unittest.main()
