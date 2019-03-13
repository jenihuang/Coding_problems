'''given n chars, return list of all binary numbers with no conseq 1s'''


def flatten(lst):
    '''given a list of lists, return a flat list'''

    result = []
    for i in range(len(lst)):
        if type(lst[i]) != list:
            result.append(lst[i])
        else:
            l = flatten_list(lst[i])
            for e in l:
                result.append(e)
    return result


def binary_main(n):
    '''given n chars, return list of all binary numbers with no conseq 1s'''

    return flatten(binary_helper(n, ''))


def binary_helper(n, bin_string):
    # base case if bin_string length is equal to n
    if len(bin_string) == n:
        return [bin_string]

    else:
        # if last char is 1, add zero to the next recursive call
        if len(bin_string) > 0 and bin_string[-1] == '1':
            past_zero = binary_helper(n, bin_string + '0')
            # add current string to the list
            past_zero.append(bin_string)
            return past_zero

        # last char is 0, add zero or 1 to the next recursive call
        else:
            past_zero = binary_helper(n, bin_string + '0')
            past_one = binary_helper(n, bin_string + '1')
            # add all valid solutions returned from past_one and current string
            past_zero.append(past_one)
            past_zero.append(bin_string)
            return past_zero


print(binary_main(3))
