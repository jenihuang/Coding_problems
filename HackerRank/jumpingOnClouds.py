# steps = 0 to start with
# while index does not equal len(array) -1
# start at index = 0, if index + 2 isn't value 1, then index +=2, else index +=1
# increment steps by 1 every time

def jumpingOnClouds(c):
	steps = 0
	index = 0
	while index != (len(c) - 1):
		try:
			if c[index+2] != 1:
				index += 2
				steps += 1
			else:
				index += 1
				steps += 1
		except IndexError:
			index += 1
			steps +=1
	return steps

def jumpingOnClouds2(c):
	steps = 0
	index = 0
	while index != (len(c) - 1):
		if index + 2 < len(c) and c[index+2] != 1:
			index += 2
			steps += 1
		else:
			index += 1
			steps += 1
	return steps

print(jumpingOnClouds2([0,0,0,1,0,0]))
