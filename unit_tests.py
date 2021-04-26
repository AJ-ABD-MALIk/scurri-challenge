'''
Created on Apr 21, 2021

@author: sogunfowora
'''


import unittest
import numpy as np
from rename_multiples import rename_multiples
from postcode_functions import format_postcode, validate_postcode


class Test_rename_multiples(unittest.TestCase):
    def test_sample_data(self):
        arr = np.arange(1, 16, dtype="object")
        result = list(rename_multiples(arr))
        expected = [1, 2, 'Three', 4, 'Five', 'Three', 7, 8, 'Three', 'Five', 11, 'Three', 13, 14, 'ThreeFive']
        self.assertEqual(expected, result)


class Test_format_postcode(unittest.TestCase):
    def test_sample_postcode(self):
        postcode = 'w 1a 0 ax'
        result = format_postcode(postcode)
        expected = {"format_status": True, "formatted_postcode": "W1A 0AX", "postcode": "w 1a 0 ax", }
        self.assertEqual(expected, result)


class Test_validate_postcode(unittest.TestCase):
    def test_valid_postcode(self):
        postcode = 'W1A 0AX'
        result = validate_postcode(postcode)
        expected = 'Valid Postcode'
        self.assertEqual(expected, result)


class Test_validate_postcode2(unittest.TestCase):
    def test_invalid_postcode(self):
        postcode = 'W1A 0AX1'
        result = validate_postcode(postcode)
        expected = 'Invalid Postcode'
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
