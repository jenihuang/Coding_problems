import unittest


def is_permutation(a, b):
    '''Returns True if a is permutation of b and vice versa'''
    # O(n) time and space

    if len(a) != len(b):
        return False
    else:
        a_dict = {}

        for letter in a:
            count = a_dict.get(letter, 0) + 1
            a_dict[letter] = count

        for letter in b:
            if a_dict.get(letter) == 0:
                return False
            else:
                a_dict[letter] -= 1
    return True


class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('bababab', 'aaaabbb'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = is_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = is_permutation(*test_strings)
            self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
