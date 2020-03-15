import unittest

from palindrome._init_ import isPalindrome


class TestPalindrome(unittest.TestCase):
    def test_sentence(self):
        """
        Test if input is a palindrome
        """
        s = "Able was I, ere I saw Elba"
        result = isPalindrome(s)
        self.assertEqual(result, 1)

    def test_string(self):
        """
        Test if input is a palindrome
        """
        s = "AblewaSiesawelba"
        result = isPalindrome(s)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
