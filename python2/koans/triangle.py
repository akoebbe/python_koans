#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    """
    :param a: integer
    :param b: integer
    :param c: integer
    :return: string
    """
    sides = [a, b, c]
    sides.sort()

    if min(sides) < 1:
        raise TriangleError
    elif sides[0] + sides[1] < sides[2]:
        raise TriangleError

    if len(set(sides)) == 2:
        return 'isosceles'
    elif len(set(sides)) == 1:
        return 'equilateral'
    else:
        return 'scalene'



# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
