def increment_string(strng):
    #separate word from number by iterating through letters
    #turn number into int
    #if number is blank make it "1"
    #rejoin the two parts
    strng = strng[::-1]
    array = list(strng)
    word = ""
    number = ""
    final = ""
    stop = None
    for index in range(len(array)):
        try:
            x = int(array[index])
            number += str(x)
        except:
            stop = -index
            break
    number = number[::-1]
    array = array[::-1]
    array = array[:stop]
    for letter in array:
        word += letter

    if number != "":
        i = int(number)
        i += 1
        if len(number) == len(str(i)):
            word += str(i)
            return word
        else:
            diff = len(number) - len(str(i))
            for j in range(diff):
                final += "0"
        final += str(i)
    else:
        word = strng[::-1]
        final = 1
    word += str(final)
    return word

print(increment_string("foo"))
