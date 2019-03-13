def minimumBribes(q):
	bribes = 0
	for i in range(len(q)-1,-1,-1):
		print('i' + str(i))
		if q[i] - (i + 1) > 2:
			return('Too chaotic')
		for j in range(max(0, q[i] - 2),i):
			print('j' + str(j))
			if q[j] > q[i]:
				print('true' + str(i) + str(j))
				bribes+=1
	return(bribes)

print(minimumBribes([2,1,5,3,4]))