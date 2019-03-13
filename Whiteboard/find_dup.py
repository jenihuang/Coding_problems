
from math import ceil, floor


def find_duplicate(arr):
    '''given array of size n and numbers 1 through n-1, return any duplicate'''
    # dictionary counter O(n) space and time
    # sort array in place and iterate O(nlogn) time and constant space
    # binary search O(nlogn) time and constant space no modifying original

    sm = 1
    lg = len(arr) - 1
    mid = (sm + lg) / 2

    while ceil(sm) != floor(lg):
        more = 0

        for n in arr:
            if n > mid:
                more += 1

        if more > mid:
            sm = mid

        else:
            lg = mid  # lg 2.5

        mid = (sm + lg) / 2  # mid 1.75

    return int(lg)


print(find_duplicate([2, 3, 2, 4, 1]))
print(find_duplicate([1, 2, 3, 4, 5, 6, 4]))
print(find_duplicate([2, 4, 2, 4, 1]))
print(find_duplicate([1, 1, 1, 1, 1]))
