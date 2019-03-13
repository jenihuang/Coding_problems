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
    final = []
    for i in range(len(s)):
        substring_list = find_longest_substring_helper(k, s, i)
        if len(substring_list) > len(final):
            final = substring_list
    return final


def find_longest_substring_helper(k, s, i):
    temp = []  # set of unique letters
    for index in range(i, len(s)):
        current = s[index]
        if len(temp) > k:
            return s[i:index - 1]
        else:
            if current not in temp:
                temp.append(current)

    return s[i:len(s) - i]


print(find_longest_substring(3, 'abcabadba'))

print(find_longest_substring(2, 'abcbcbcacabacabba'))
