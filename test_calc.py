from main import main
import unittest

class TestStringMethods(unittest.TestCase):
    def test_simple_calc_without_new_amounts_monthly(self):
        result = main(1000, 10, 1, 0)
        self.assertEqual(result, 1100)
        result = main(1000, 10, 2, 0)
        self.assertEqual(result, 1210)
        result = main(1000, 10, 3, 0)
        self.assertEqual(result, 1331)


    def test_calc_with_months_amount(self):
        result = main(1000, 10, 1, 100)
        self.assertEqual(result, 1200)


    def test_calc_with_months_amount_frequency_of_2_months(self):
        result = main(1000, 10, 2, 100)
        self.assertEqual(result, 1420)


    def test_calc_with_months_amount_frequency_of_2_months(self):
        result = main(1000, 10, 5, 100)
        self.assertEqual(result, 2221.02)
        

if __name__ == '__main__':
    unittest.main()