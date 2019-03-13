import unittest


def reverse(word):
    '''returns word in reversed order'''
    # O(n) time and space

    start = 0
    end = -1
    a = list(word)

    for i in range(len(word) // 2):
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1

    return ''.join(a)


class Test(unittest.TestCase):
    data = ['abcd', 'hello', 'kayak', ""]

    def test_reverse(self):
        # correct check
        for test_string in self.data:
            actual = reverse(test_string)
            self.assertEqual(''.join(list(test_string)[:: -1]), actual)


if __name__ == "__main__":
    unittest.main()
