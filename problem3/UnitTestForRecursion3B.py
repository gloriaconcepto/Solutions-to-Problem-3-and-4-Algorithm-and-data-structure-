#-------------------------------------------------------------------------------
# Name:       Unit test   Fibonacci sequence recursively
# Purpose:
#
# Author:      mmk and emeka
#
# Created:     04/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
import Recursion3BFibonacci as fib
import unittest
class TestFibonacciSequence(unittest.TestCase):
     """
    Test fibonacci result
    """
     def test_fibonacci_recursive(self):
        """
        Test that the unsorted list  returns the smallest number in the list
        From mathematic the fibonacci of 5 is 8
        """
        result = fib.fibonacci_recursive(5)
        self.assertEqual(result, 8)





if __name__ == '__main__':

     unittest.main()
