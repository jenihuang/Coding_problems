def expanded_form(num):
    s = str(num)
    string = list(s)
    final = ''
    n = len(string) - 1
    for i in range(len(string)):
        if n == len(string) - 1:
            final += (string[i] + "0" * n)
            n -= 1
        elif n != len(string) - 1 and string[i] != "0":
            final += (" + " + string[i] + "0" * n)
            n -= 1
        else:
            n -= 1
    return final
