def find_shifted_num(nums, n):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        low_value = nums[low]
        mid_value = nums[mid]
        high_value = nums[high]

        if n == low_value:
            return low
        if n == mid_value:
            return mid
        if n == high_value:
            return high
        if low_value <= mid_value:
            # left half is sorted
            if n <= mid_value:
                if n >= low_value:
                    high = mid
                else:
                    return None
            else:
                low = mid + 1
        else:  # low_value > mid_value
            if n <= mid_value:
                high = mid
            else:  # n > mid_value
                if n > high_value:
                    high = mid
                else:
                    low = mid
    return None


print(find_shifted_num([2, 1, 1, 2], 2))

print(find_shifted_num([2, 3, 4, 1, 1, 2], 2))

print(find_shifted_num([5, 6, 1, 2, 3, 4], 7))

print(find_shifted_num([5, 6, 1, 2, 3, 4], 5))

print(find_shifted_num([5, 6, 1, 2, 3, 4], 6))

print(find_shifted_num([5, 6, 1, 2, 3, 4], 1))

print(find_shifted_num([5, 6, 1, 2, 3, 4], 2))

print(find_shifted_num([5, 6, 1, 2, 3, 4], 3))

print(find_shifted_num([5, 6, 1, 2, 3, 4], 4))
