def scramble(str1, str2):
    ''' returns True if str2 can be created using letters in str1, else False'''
    #12K ms failed 2

    if len(str1) < len(str2):
        return False

    l1 = list(str1)
    s2 = set(str2)

    for letter in l1:
        if set(letter).issubset(s2):
            s2.remove(letter)

    if len(s2) == 0:
        return True
    else:
        return False


print(scramble('cedewaraaossoqqyt','codewars'))


