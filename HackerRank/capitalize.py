#Change to list using .split()
#for item in list, capitalize index0
def solve(s):
	s = s.split()
	final = []
	for i in s:
		letter = i[0]
		rest = i[1:]
		a = letter.upper()
		final.append(a+rest)

	final = " ".join(final)

	return final

print(solve("chris alan"))