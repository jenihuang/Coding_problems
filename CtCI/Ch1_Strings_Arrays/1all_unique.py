import unittest


def unique(word):
    '''returns True if all unique char otherwise False'''
    # O(n) time and space

    length = len(word)
    s = set(word)
    s_length = len(s)
    return length == s_length


def unique2(word):
    '''same as above, no additional space required'''
    # O(n) time and O(1) space


    total_ascii = [False for i in range(128)]
    for letter in word:
        value = ord(letter)
        if total_ascii[value]:
            return False
        total_ascii[value] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique2(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
