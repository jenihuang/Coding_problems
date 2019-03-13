import unittest
from test import Kangaroo


class TestTest(unittest.TestCase):
    def test_kangaroo(self):
        # k1 starts before k2 and is slower, should return False
        k1 = Kangaroo(0, 3)
        k2 = Kangaroo(4, 2)
        self.assertEqual(k1.intersect(k2), 'YES')

        # k1 and k2 are equally fast and k1 starting point is less, False
        k1 = Kangaroo(0, 2)
        k2 = Kangaroo(5, 3)
        self.assertEqual(k1.intersect(k2), 'NO')

        # k1 and k2 are the same, should return True
        k1 = Kangaroo(21, 6)
        k2 = Kangaroo(47, 3)
        self.assertEqual(k1.intersect(k2), 'NO')

        # k1 is faster than k2 and k1 start point is less, should return True
        k1 = Kangaroo(43, 2)
        k2 = Kangaroo(70, 2)
        self.assertEqual(k1.intersect(k2), 'NO')

        # k2 is faster than k1 and k2 start point is less, should return True
        k1 = Kangaroo(5, 2)
        k2 = Kangaroo(3, 3)
        self.assertEqual(k1.intersect(k2), 'YES')


if __name__ == "__main__":
    unittest.main()
