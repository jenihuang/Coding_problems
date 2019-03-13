
def a_to_i(string_ints):
    '''given a string of integers, return the integer without using int function'''

    zero_code = ord('0')
    result = 0
    neg = False
    pos_string = string_ints

    if string_ints[0] == '-':
        neg = True
        pos_string = string_ints[1:]

    for char in pos_string:
        # integer surpasses largest integer becomes negative
        if result < 0:
            return None
        else:
            char_code = ord(char)
            integer = char_code - zero_code
            result = result * 10 + integer
    if neg:
        result = -result

    return result
