def scramblies(str1, str2):
    str1_count = {}

    for letter in str1:
        if letter in str1_count:
            str1_count[letter] += 1
        else:
            str1_count[letter] = 1

    for letter in str2:
        if letter in str1_count and str1_count[letter] > 0:
            str1_count[letter] -= 1
        else:
            return False
    return True


print(scramblies('rdworld', 'world'))
print(scramblies('katas', 'steak'))
