#make 3 variables pos, neg, zero
#for item in array, increment count per variable respectively
#print ratios
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
	pos = 0
	neg = 0
	zero = 0
	for i in arr:
		if i == 0:
			zero += 1
		elif i < 0:
			neg += 1
		else:
			pos += 1

	print(pos/len(arr))
	print(neg/len(arr))
	print(zero/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)







