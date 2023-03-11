# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Darshan Bhanushali
"""

import unittest
from triangle import classifytriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """
    Consists of the different test cases used to test the program
    """
    # define multiple sets of tests as functions with names that begin

    def testrighttriangle_a(self):
        """
        Test to check if triangle is a right triangle
        """
        self.assertEqual(classifytriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')


    def testrighttriangle_b(self):
        """
        Test to check if triangle is a right triangle
        """
        self.assertEqual(classifytriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')


    def testequilateraltriangles(self):
        """
        Test to check if triangle is an equilateral triangle
        """
        self.assertEqual(classifytriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')


    def testupperlimit(self):
        """
        Test to check upper limit of sides of triangle
        """
        self.assertEqual(classifytriangle(308, 407, 534), 'InvalidInput', '308, 407, 534 are invalid inputs')


    def testlowerlimit(self):
        """
        Test to check lower limit of sides of triangle
        """
        self.assertEqual(classifytriangle(-7, -15, -22), 'InvalidInput', '-7, -15, -22 are invalid inputs')

    #
    def testiftriangle(self):
        """
        Test to check if given sides do not form a triangle
        """
        self.assertEqual(classifytriangle(1, 4, 5), 'NotATriangle', '1, 4, 5 should not be a triangle')


    def testisoscelestriangle_a(self):
        """
        Test to check if the given triangle is an isosceles triangle
        """
        self.assertEqual(classifytriangle(6, 6, 5), 'Isosceles', '6,6,5 should be isosceles')


    def testisoscelestriangle_b(self):
        """
        Test to check if the given triangle is an isosceles triangle
        """
        self.assertEqual(classifytriangle(5, 7, 7), 'Isosceles', '5,7,7 should be isosceles')


    def testscalenetriangle(self):
        """
        Test to check if the given triangle is a scalene triangle
        """
        self.assertEqual(classifytriangle(7, 9, 11), 'Scalene', '7, 9, 11 should be scalene')


    def teststringtriangle(self):
        """
        Test to check if string input for sides of a triangle is valid
        """
        self.assertEqual(classifytriangle('a', 'b', 'c'), 'InvalidInput', 'String inputs should be invalid')


    def testfloattriangle(self):
        """
         Test to check if float input for sides of a triangle is valid
        """
        self.assertEqual(classifytriangle(5.2, 3.5, 8.9), 'InvalidInput', 'Float inputs should be invalid')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
