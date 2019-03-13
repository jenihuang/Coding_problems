#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
# start variable aCount and bCount equal to zero
# compare index 0,1,2 for a and b and increment the count respectively
# final = [aCount,bCount]
def compareTriplets(a, b):
	aCount = 0
	bCount = 0
	for i in range(3):
		if a[i]== b[i]:
			continue
		elif a[i] > b[i]:
			aCount += 1
		else:
			bCount += 1

	final = [aCount,bCount]
	return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



