'''
pop index 0 and append to the end in range d
'''
def rotLeft(a, d):

	for i in range(d):
		temp = a[0]
		a.pop(0)
		a.append(temp)

	print(a)

	return ' '.join(map(str,a))

print(rotLeft([11,22,33,44,55],4))








