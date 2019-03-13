#start a counter at 0
#represent every D as -1 and every U as 1
#everytime -1 becomes 0 increment final by 1
def countingValleys(n, s):
	count = 0
	final = 0
	for letter in s:
		if count == -1 and letter == "U":
			final += 1
		if letter == "U":
			count += 1
		else:
			count -= 1
	return final

print(countingValleys(8,'UDDDUDUU'))

