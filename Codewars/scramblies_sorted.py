def scramble(str1, str2):
    ''' returns True if str2 can be created using letters in str1, else False'''
    #12K ms passed all tests

    if len(str1) < len(str2):
        return False

    l1 = sorted(str1)
    l2 = sorted(str2)

    try:
        first = l1.index(l2[0])
    except:
        return False
    
    index = 0

    for i in range(len(l1)):
        if l1[i] == l2[index]:
            index += 1
            if index == len(l2):
                return True


    return False


print(scramble('cedewaraaossoqqyt','codewars'))


