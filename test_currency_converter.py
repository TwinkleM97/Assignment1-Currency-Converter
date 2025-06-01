import unittest
from currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CurrencyConverter()

    def test_basic_conversion(self):
        self.assertEqual(self.converter.convert(100, 'USD', 'EUR'), 85.0)
        self.assertEqual(self.converter.convert(85, 'EUR', 'USD'), 100.0)

    def test_same_currency(self):
        self.assertEqual(self.converter.convert(50, 'USD', 'USD'), 50.0)

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            self.converter.convert(100, 'USD', 'ABC')

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            self.converter.convert(-50, 'USD', 'EUR')

    def test_exchange_rate(self):
        rate = self.converter.get_exchange_rate('USD', 'CAD')
        self.assertEqual(rate, 1.25)

if __name__ == '__main__':
    unittest.main()
