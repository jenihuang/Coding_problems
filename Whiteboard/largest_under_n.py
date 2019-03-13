def find_largest(nums, n):
    if nums[0] >= n:
        return None
    elif nums[-1] < n:
        return len(nums) - 1
    else:
        high = len(nums) - 1
        low = 0
        while high - low > 1:
            mid = (low + high) // 2
            if nums[mid] >= n:
                high = mid - 1
            else:
                low = mid

        return low


print(find_largest([1, 2, 2, 4, 5, 8], 6))  # 4

print(find_largest([3, 3, 3, 4], 4))  # 2

print(find_largest([2, 4], 3))  # 0

print(find_largest([1, 3, 4, 4, 4, 4, 4, 4, 7, 9], 4))  # 1

print(find_largest([3, 4, 5], 2))  # none

print(find_largest([3, 4, 5], 8))  # 2

print(find_largest([3], 2))  # none

print(find_largest([3], 5))  # 0
