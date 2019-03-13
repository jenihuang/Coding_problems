#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
# c = s.count("a") gives number of a's in one repeat
# r = n/len(s) gives number of full repititions
# m = n % len(s) gives remaining letters
# for i in range(m): if letter is a, count += 1
# return c*r + count
def repeatedString(s, n):
	c = s.count("a")
	r = n//len(s)
	m = n % len(s)
	count = 0
	for i in range(m):
		if s[i] == "a":
			count +=1
	return c*r+count

print(repeatedString("aba",10))