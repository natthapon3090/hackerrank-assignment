import unittest
from funny import funny_string


class TestFunnyString(unittest.TestCase):

    def test_funny_true(self):
        # Arrange
        s = "acxz"
        expected = "Funny"

        # Act
        result = funny_string(s)

        # Assert
        self.assertEqual(result, expected)
