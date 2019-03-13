'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [15, 3, 10, 7] and k of 17, return true since 10 + 7 is 17.
'''

def canAddIter(aList, k):
	if len(aList) == 0:
		return False
	for i in aList:
		if i == k:
			return True
		elif i < k:
			r = k - i
			for j in aList[1:]:
				if j == r:
					return True
	return False

def canAddRec(aList, k):
	if k in aList:
		return True

	for item in aList:
		if item < k:
			remaining = k - item
			recall = canAddRec(aList[1:],remaining)
			if recall:
				return True
			else:
				continue
	return False

def solution(aList, k):
    seen = []
    for num in aList:
        if k - num in seen:
            return True
        seen.append(num)
    return False


print(canAddRec([15,3,10,7],17))
print(canAddIter([15,3,10,7],17))
print(solution([15,3,10,7],17))
