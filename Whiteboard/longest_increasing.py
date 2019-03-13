import unittest


def longest_inc(nums):
    biggest = 0
    count = 1

    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            count += 1
        else:
            if count > biggest:
                biggest = count
            count = 1

    if count > biggest:
        biggest = count

    return biggest


class Test(unittest.TestCase):
    data = [
        ([0, 1, 2], 3),
        ([0, 2, 1, 3, 5, 10], 4),
        ([-6, 2, 8, -2, 0, -1], 3)
    ]

    def test_compress_string(self):
        for [test_case, expected] in self.data:
            result = longest_inc(test_case)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
