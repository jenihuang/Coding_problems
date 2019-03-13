import unittest


def is_pal(chars):

    chars = chars.lower()
    char_count = {}
    length = len(chars)

    for char in chars:
        if char == ' ':
            length -= 1
        elif char in char_count:
            char_count[char] += 1

        else:
            char_count[char] = 1

    if length % 2 == 0:
        even = True
    else:
        even = False

    if even:

        for count in char_count.values():
            if count % 2 != 0:
                return False

        return True

    else:
        single = False
        for count in char_count.values():
            if count % 2 != 0 and single:
                return False
            elif count % 2 != 0:
                single = True

        return True


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_is_pal(self):
        for [test_string, expected] in self.data:
            actual = is_pal(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
