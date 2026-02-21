import unittest
from alternating_characters import alternating_characters


class TestAlternating(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(alternating_characters("AAAA"),3)

    def test_case2(self):
        self.assertEqual(alternating_characters("ABABAB"),0)

    def test_case3(self):
        self.assertEqual(alternating_characters("AABBAB"),2)


if __name__=="__main__":
    unittest.main()
