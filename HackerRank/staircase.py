#make a variable starting at n
#while n > 0
#print(#*n)
#n -= 1

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
if __name__ == '__main__':
    n = input()
def staircase(n):

    t = 1
    space = n-1
    while t <= n:
        print(" "*space + "#"*t)
        t += 1
        space -= 1

staircase(int(n))



