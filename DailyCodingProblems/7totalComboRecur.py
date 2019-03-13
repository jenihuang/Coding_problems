'''
base case:
if length is zero or 1, return 1
else
if the first two are under 27
return function missing first two plus function missing first one

'''

def totalCombo(num):
	if len(num) <= 1:
		return 1
	else:
		if int(num[:2]) <= 26:
			return totalCombo(num[1:]) + totalCombo(num[2:])
		else:
			return totalCombo(num[1:])
#print(totalCombo('111'))


letters = '0abcdefghijklmnopqrstuvwxyz'
mapping = {}
for i in range(1,27):
	mapping[str(i)] = letters[i]


def printCombo(num):
	if len(num) <= 2 and int(num) <= 26:
		return mapping[num]
	else:
		if int(num[:2]) <= 26:
			return(printCombo(num[:2]) + printCombo(num[2:]))
		else:
			return(printCombo(num[0]) + printCombo(num[1:]))

print(printCombo('111'))



