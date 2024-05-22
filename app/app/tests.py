""" Example Test """
from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """ test the cal module"""
    def test_add_numbers(self):
        """adding number together"""
        res = calc.add(5,6)
        self.assertEqual(res,11)
    
    def test_substract(self):
        """substracting numbers"""
        res=calc.sub(10,2)
        self.assertEqual(res,8)