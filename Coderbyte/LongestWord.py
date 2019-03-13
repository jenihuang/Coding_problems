#iterate through string
#if letter is in valid letters, add letter to test
#else letter is not in valid letters, compare length of test and length of final
#if length test greater than final, replace final with test
#reset test to empty string
#else length test less than final
#reset test to empty string
#return final
#at the end, redo the test to see length of string

import string
def LongestWord(sen): 
    valid = list(string.ascii_letters)

    test = ""
    final = ""

    for letter in sen:
        if letter in valid:
            test += letter
        else:
            if len(test) > len(final):
                final = test
                test = "" 
            else:
                test = ""
    if len(test) > len(final):
        final = test
    return final
    
# keep this function call here  
print(LongestWord("fun&!! time"))
