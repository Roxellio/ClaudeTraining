import unittest
from math import pi as math_pi
# cannot import 009_bla_main.py due to it begins with number.
# rename it first if want to actually try this.
# ignoring it for now since it's not too important
from main import calculate_pi


class TestCalculatePi(unittest.TestCase):
    """Test cases for the calculate_pi function"""
    
    def test_pi_to_5_digits(self):
        """Test that pi is calculated correctly to 5 decimal places"""
        result = calculate_pi(5)
        expected = 3.14159
        self.assertEqual(result, expected)
    
    def test_pi_to_5_digits_accuracy(self):
        """Test that pi to 5 digits is within acceptable range"""
        result = calculate_pi(5)
        # Pi to 5 decimal places should be 3.14159
        self.assertAlmostEqual(result, math_pi, places=5)
    
    def test_pi_to_2_digits(self):
        """Test that pi is calculated correctly to 2 decimal places"""
        result = calculate_pi(2)
        expected = 3.14
        self.assertEqual(result, expected)
    
    def test_pi_to_10_digits(self):
        """Test that pi can be calculated to 10 decimal places"""
        result = calculate_pi(10)
        self.assertAlmostEqual(result, math_pi, places=10)
    
    def test_default_parameter(self):
        """Test that default parameter is 5 digits"""
        result = calculate_pi()
        self.assertEqual(result, 3.14159)
    
    def test_pi_value_in_range(self):
        """Test that calculated pi is in reasonable range"""
        result = calculate_pi(5)
        self.assertGreater(result, 3.14)
        self.assertLess(result, 3.15)
    
    def test_compare_with_math_pi(self):
        """Test that our calculation matches Python's math.pi"""
        result = calculate_pi(5)
        math_pi_rounded = round(math_pi, 5)
        self.assertEqual(result, math_pi_rounded)


if __name__ == '__main__':
    unittest.main()
