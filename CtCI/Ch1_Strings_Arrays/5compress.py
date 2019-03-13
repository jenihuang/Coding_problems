import unittest


def compress_string(chars):
    '''return compressed string or original string if longer'''
    # O(n) time, O(1) space

    compressed = ''
    count = 1

    for i in range(len(chars) - 1):
        if chars[i] == chars[i + 1]:
            count += 1
        else:
            compressed += chars[i]
            compressed += str(count)
            count = 1

    compressed += chars[i]
    compressed += str(count)

    if len(chars) <= len(compressed):
        return chars
    else:
        return compressed


class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef'),
    ]

    def test_compress_string(self):
        for [test_string, expected] in self.data:
            result = compress_string(test_string)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
