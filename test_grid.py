import unittest
from grid_challenge import grid_challenge


class TestGrid(unittest.TestCase):

    def test_yes(self):
        self.assertEqual(grid_challenge(["abc","ade","efg"]),"YES")

    def test_no(self):
        self.assertEqual(grid_challenge(["cba","daf","ghi"]),"NO")


if __name__=="__main__":
    unittest.main()
