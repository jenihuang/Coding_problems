'''
convert both strings to arrays
look for the longer array
for each letter in longer string, find it in the shorter string
if found delete from both
after going through everything return len sum of both arrays
'''

def makeAnagram(a,b):
	a = list(a)
	b = list(b)
	if len(a) >= len(b):
		longer = a
		shorter = b
	else:
		longer = b
		shorter = a

	both = []
	for letter in longer:
		if letter in shorter:
			both.append(letter)
			shorter.remove(letter)

	for letter in both:
		longer.remove(letter)

	return (len(longer) + len(shorter))

print(makeAnagram('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke'))




