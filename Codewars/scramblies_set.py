def scramble(str1, str2):
    ''' returns True if str2 can be created using letters in str1, else False'''

    if len(str1) < len(str2):
        return False

    # s1 = set(str1)
    s2 = set(str2)

    for letter in s2:
        if str1.count(letter) < str2.count(letter):
            return False

    return True


print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('rdworld', 'world'))
print(scramble('katas', 'steak'))
