#!/usr/bin/env checkio --domain=py run triangle-angles

# https://py.checkio.org/mission/triangle-angles/

# You are given the lengths for each side on a triangle.    You need to find all three angles for this triangle.    If the given side lengths cannot form a triangle (or form a degenerated triangle),    then you must return all angles as 0 (zero).    The angles should be represented as a list of integers inascending order.    Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).
# 
# 
# 
# Input:The lengths of the sides of a triangle as integers.
# 
# Output:Angles of a triangle in degrees as sorted list of integers.
# 
# Precondition:
# 0 < a,b,c ≤ 1000
# 
# 
# END_DESC

import math


def degree(a, b, c):
    return round(math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))))


def checkio(a, b, c):
    sides = sorted([a, b, c], reverse=True)
    if sum(sides[1:]) <= sides[0]:
        return [0, 0, 0]

    return sorted([degree(a, b, c), degree(b, a, c), degree(c, a, b)])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"