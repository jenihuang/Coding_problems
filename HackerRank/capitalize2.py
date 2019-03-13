#iterate through index in len(string)
#if index == 0, add uppercase letter to final
#if letter not in ascii.letters() that means it's a space add it to final
#
import string
def solve(s):
	final = ""
	valid = string.ascii_letters
	flag = False
	for i in range(len(s)):
		if i == 0:
			final += s[i].upper()
		elif s[i] == " ":
			flag = True
			final += s[i]
		elif flag == True:
			final += s[i].upper()
			flag = False
		else:
			final += s[i]
	return final


print(solve("hello  world lol"))