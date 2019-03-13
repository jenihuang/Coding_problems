import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
# y = mx + b
# m1x + b1 = m2x + b2
# m1x - m2x = b2 - b1
# x = (b2 - b1)/(m1 - m2)


# def kangaroo(x1, v1, x2, v2):

#     if v1 != v2:
#         intersection = (x2 - x1) / (v1 - v2)
#     else:
#         if x1 != x2:
#             return 'NO'

#     if intersection == int(intersection):
#         if v1 > v2 and x1 <= x2:
#             return 'YES'
#         elif v1 == v2 and x1 == x2:
#             return 'YES'
#         elif v1 < v2 and x1 >= x2:
#             return 'YES'
#         else:
#             return 'NO'
#     else:
#         return 'NO'


class Kangaroo(object):
    def __init__(self, x, v):
        self.start = x
        self.speed = v

    def compare(self, other):
        if self.start <= other.start and self.speed > other.speed:
            return 'YES'
        elif self.start == other.start and self.speed == other.speed:
            return 'YES'
        elif self.start >= other.start and self.speed < other.speed:
            return 'YES'
        else:
            return 'NO'

    def intersect(self, other):
        if self.compare(other) == 'YES':
            x = (other.start - self.start) / (self.speed - other.speed)
            if x == int(x):
                return 'YES'
            else:
                return 'NO'
        else:
            return 'NO'
