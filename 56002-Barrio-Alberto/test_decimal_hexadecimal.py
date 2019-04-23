import unittest
from decimal_hexadecimal import decimal_to_hexadecimal

class TestHexadecimal(unittest.TestCase):
    def test_decimal_5_to_hex(self):
        result=decimal_to_hexadecimal(5)
        self.assertEqual(result, '5')

    def test_decimal_10_to_hex(self):
        result=decimal_to_hexadecimal(10)
        self.assertEqual(result, 'A')

    def test_decimal_17_to_hex(self):
        result=decimal_to_hexadecimal(17)
        self.assertEqual(result, '11')

    def test_decimal_16_to_hex(self):
        result=decimal_to_hexadecimal(16)
        self.assertEqual(result, '10')

    def test_decimal_4095_to_hex(self):
        result=decimal_to_hexadecimal(4095)
        self.assertEqual(result, 'FFF')
    
    def test_decimal_1234_to_hex(self):
        result=decimal_to_hexadecimal(1234)
        self.assertEqual(result, '4D2')

    def test_decimal_234_to_hex(self):
        result=decimal_to_hexadecimal(234)
        self.assertEqual(result, 'EA')

if __name__ == '__main__':
    unittest.main()