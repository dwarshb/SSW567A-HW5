# -*- coding: utf-8 -*-
"""
The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Darshan Bhanushali
"""


def classifytriangle(a, b, c):
    """
    classifytriangle consists of the logic to classify the triangle as right,
    scalene, isosceles and equilateral
    """
    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    try:
        if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
            return 'InvalidInput'
    except ValueError:
        print("InvalidInput")

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    # condition to check if triangle is equilateral
    if a == b and b == c:
        return 'Equilateral'
    # condition to check if triangle is right triangle
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or ((a ** 2) + (c ** 2)) == (b ** 2) or \
            ((b ** 2) + (c ** 2)) == (a ** 2):
        return 'Right'
    # condition to check if triangle is scalene triangle
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'
