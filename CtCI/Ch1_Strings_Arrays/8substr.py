import unittest


def is_substring(string, sub):
    return string.find(sub) != -1


def sub(str1, str2):

    if len(str2) > len(str1):
        return False

    double = str2 + str2

    return is_substring(double, str1)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_sub(self):
        for [s1, s2, expected] in self.data:
            actual = sub(s1, s2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
