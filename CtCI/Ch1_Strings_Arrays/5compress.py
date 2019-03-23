import unittest


def compress_string(message):
    '''returns compressed string given a string input'''

    # start a string counter for consecutive characters seen
    consecutive = 1
    result_list = []

    # iterate through the input string and compare current char to next char
    # increment consecutive as needed and append to result_list when next char is no longer the same
    for i in range(len(message) - 1):
        if message[i] == message[i + 1]:
            consecutive += 1
        else:
            result_list.append(message[i])
            if consecutive > 1:
                result_list.append(str(consecutive))
            consecutive = 1

    # check edge case if last two letters were the same
    if message[-1] == message[-2]:
        result_list.append(message[i])
        result_list.append(str(consecutive))

    # check edge case if last letter is different
    if consecutive == 1:
        result_list.append(message[-1])

    result_str = ''.join(result_list)
    return result_str


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
