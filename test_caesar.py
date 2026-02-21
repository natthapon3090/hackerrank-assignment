import unittest
from caesar_cipher import caesar_cipher


class TestCaesar(unittest.TestCase):

    def test_lower(self):
        self.assertEqual(caesar_cipher("abc",2),"cde")

    def test_upper(self):
        self.assertEqual(caesar_cipher("XYZ",2),"ZAB")

    def test_symbol(self):
        self.assertEqual(caesar_cipher("abc-123",2),"cde-123")


if __name__=="__main__":
    unittest.main()
