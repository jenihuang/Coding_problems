import unittest


def rotate_arr(arr):
    results = []
    for j in range(len(arr)):
        results.append([])
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr[i])):
            results[j].append(arr[i][j])
    return results


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_arr(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_arr(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
