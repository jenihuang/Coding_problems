#N step staircase can go up 1 or 2, list unique ways to step
'''
make a tree starting with 0 as root
next child is 1 or 2
next child is 1 or 2
keep going until the steps are up

repeat same thing with tree with 2 as root

'''

def countStairs(start,N):
	if start == N:
		return 1
	if start > N:
		return 0
	else:
		return countStairs(start+1,N) + countStairs(start+2,N)

for i in range(1,11):
	print(i, countStairs(0,i))








