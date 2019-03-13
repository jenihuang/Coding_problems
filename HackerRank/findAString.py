#recursive call to shorter and shorter string until none left
#basecase is substring not in string
#else recall function on string.find(substring) to the end
def count_substring(string, sub_string):
    if sub_string not in string:
    	return 0
    else:
    	start = string.find(sub_string) + 1
    	return 1 + count_substring(string[start:],sub_string)

print(count_substring("ABCDCDC","CDC"))