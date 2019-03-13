if __name__ == '__main__':
	n = int(input())

	final = ''
	count = 1
	maximum = 1
	while n != 0:
		remainder = n%2
		final += (str(remainder))
		n = n//2

	final = final[::-1]


	for i in range(len(final)-1):
		if final[i] == '1':
			if final[i+1] == '1':
				count += 1
		if count > maximum:
			maximum = count
		if final[i] == '0':
			count = 1

	print(maximum)
	

