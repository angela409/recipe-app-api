"""
Sample tests

"""
from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module"""
    

    def test_add_numbers(self):
        """
        Test adding numbers together.
        """
        res = calc.add(5,6)
        self.assertEqual(res, 11)
    
    def test_subtract(self):
        """Test subtract numbers"""

        res = calc.subtract(10,5)
        self.assertEqual(res, 5)