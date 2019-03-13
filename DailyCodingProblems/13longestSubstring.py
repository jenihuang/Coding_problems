'''Given an integer k and a string s, 
find the length of the longest substring that 
contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
the longest substring with k distinct characters is "bcb".
'''

'''

start an index variable at 0
start a final variable
for loop range length of s
	reset test variable to empty
	reset count to 0
	while count doesn't equal k
		if test is empty
			add current letter to test
			increment count by 1
			increment index by 1
		else test is not empty
			if letter is different than last one in test
			add letter to test
			increment count by 1
			

	compare length of test to final
	if greater than final, replace final

return final
'''


def find_longest_substring(k, s):

	final =[]
	index = 0

	for i in range(len(s)):
		test =[]
		count = 0
		index = i
		while count <= k:
			if index == len(s):
				break
			current = s[index] 
			if not test:
				test.append(current)
				index += 1
				count += 1
			else:
				if count == k:
					if current in test:
						test.append(current)
						index += 1
					else:
						break
				else:
					test.append(current)
					index += 1
					count += 1

		if len(test) > len(final):
			final = test
	return final


print(find_longest_substring(3,'abcabadba'))

print(find_longest_substring(2,'abcbcbcacabacabba'))



			







