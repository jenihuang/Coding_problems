#!/bin/python3

import math
import os
import random
import re
import sys

# make two variables min and max
# could sort and sum first four then last four

def miniMaxSum(arr):
	arr.sort()
	minimum = sum(arr) - arr[4]
	maximum = sum(arr) - arr[0]

	print(str(minimum) + " " + str(maximum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)







