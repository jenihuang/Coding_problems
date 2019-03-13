'''
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain 
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

1. iterate through list and see if n-1 is in list
2. if not in list, save n-1 as temp, save n as lowest
3. next number see if n-1 in list, if not, compare to saved lowest to see which is lower and resave temp, lowest
4. return temp

'''

def find_int(lst):

	for i in range(len(lst)):
		if i == 0:
			lowest = lst[i]
			temp = lowest - 1
		if (lst[i]-1) in lst:
			continue
		elif lst[i] <= 1:
			continue
		else:
			if lowest > lst[i]:
				temp = lst[i] - 1
				lowest = lst[i]
	if temp == 0:
		temp = max(lst) + 1

	return temp
'''
for range in length of list
start from index 0 and see what num at that index
go to index num-1 if exists
it doesn't exist negate current index
'''

def find_int2(lst):

	for i in lst:
		if i <= 0:
			lst.remove(i)
	i = 0

	for index in range(len(lst)):
		try:
			nextIndex = lst[i] - 1: #2,0
				lst[nextIndex] = - lst[nextIndex] #-1,-3
				i = nextIndex #2,0
		except IndexError:
			lst[index] = - lst[index]
			nextIndex = index + 1

	return lst



print(find_int2([2,10,500,1,4]))
print(find_int2([3,4,1]))
print(find_int2([1,2,0]))




