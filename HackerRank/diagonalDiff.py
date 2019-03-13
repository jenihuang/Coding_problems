#!/bin/python3

import math
import os
import random
import re
import sys

# start variable leftSum and rightSum
# 
def diagonalDifference(arr):
	leftSum = 0
	rightSum = 0
	count = 0
	for i in range(n):
		leftSum += arr[i][i]

	for i in reversed(range(n)):
		rightSum += arr[count][i]
		count += 1

	return abs(leftSum - rightSum)







