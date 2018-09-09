#-------------------------------------------------------------------------------
# Name:   Unit test   Reverse list recursively
# Purpose:
#
# Author:      mmk and emeka
#
# Created:     04/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
import Recursion3A as reverse
import unittest

class TestForProblem3ARecursion(unittest.TestCase):
     """
    Test to assert if the list is reverse.
    """
     def setUp(self):
        '''Get the list from the expected function'''
        self.expected = ['anemone', 'mantis', 'shrimp', 'blobfish', 'octopus', 'shark']
        self.result = reverse.return_reverse_list(['shark', 'octopus','blobfish','mantis shrimp', 'anemone'])


     def test_count_eq(self):
        """Will succeed"""
        self.assertCountEqual(self.result, self.expected)



     def test_list_eq(self):
        """Will PASS"""
        self.assertListEqual(self.result, self.expected)





def main():
    pass

if __name__ == '__main__':
    unittest.main()
