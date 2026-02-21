import unittest
from two_characters import two_characters


class TestTwo(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(two_characters("beabeefeab"),5)

    def test_case2(self):
        self.assertEqual(two_characters("aaaa"),0)


if __name__=="__main__":
    unittest.main()
