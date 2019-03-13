def scramble(str1, str2):
    ''' returns True if str2 can be created using letters in str1, else False'''
    #9267 ms failed 7

    if len(str1) < len(str2):
        return False

    s1 = set(str1)
    s2 = set(str2)


    extra = list(s1.difference(s2))
    missing = list(s2.difference(s1))

    if missing:
        return False

    count = 0

    for letter in str1:
        if letter in extra:
            count += 1

    a = len(str1) - count
    b = len(str2)

    if a >= b:
        return True
    else:
        return False


print(scramble('katas','steak'))


