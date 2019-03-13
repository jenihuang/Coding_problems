'''
make dictionary of number key to letter value
make blank testString variable
make blank comboList variable

for digit in range 0 to length of num-1, 
	if first two digits are in mapping keys:
		add letter value to testString
		if digit is currently zero, that means missing last digit
		add letter value of last digit to testString
		if digit is not zero, that means missing first digit
		add first digit letter value to beginning of testString
		append wordto comboList and reset testString to blank
	make for loop that iterates over each digit and adds the value
	append to comboList
			

return length of comboList
'''

letters = '0abcdefghijklmnopqrstuvwxyz'
mapping = {}
for i in range(1,27):
	mapping[str(i)] = letters[i]

def countMessageWays(num):
	num = str(num)
	testString = ''
	comboList = []

	for i in range(len(num)-1):
		if num[i:(i+2)] in mapping:
			testString += mapping[num[i:(i+2)]]
			if i == 0:
				testString += mapping[num[-1]]
			else:
				testString = mapping[num[0]] + testString
			comboList.append(testString)
			testString = ''

	for i in num:
		try:
			testString += mapping[i]
		except KeyError:
			break

	return comboList

print(countMessageWays(101))


