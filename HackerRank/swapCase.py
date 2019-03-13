import string
def swap_case(s):
    upper = [x for x in string.ascii_uppercase]
    lower = [x for x in string.ascii_lowercase]
    final = ""
    for letter in s:
        if letter in upper:
            final += (letter.lower())
        else:
            final += (letter.upper())
    return final

print(swap_case("Hello"))