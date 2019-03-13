def find_indices(arr, n):
    '''return indicies of two numbers that sum to n if exists'''
    # O(n) time and space

    map_dict = {}

    for i in range(len(arr)):
        map_dict[arr[i]] = i

    for num in arr:
        if n - num in map_dict:
            return map_dict[num], map_dict[n - num]

    return None


print(find_indices([1, 3, 4, 5, 3, 7], 9))  # 2,3
print(find_indices([1, 3, 4, 5, 3, 7], 8))  # 0,5
print(find_indices([1, 3, 4, 5, 3, 7], 7))  # 4,2
print(find_indices([1, 3, 4, 5, 3, 7], 6))  # 0,3
print(find_indices([1, 3, 4, 5, 3, 7], 5))  # 0,2
print(find_indices([1, 3, 4, 5, 3, 7], 4))  # 0,4
print(find_indices([1, 3, 4, 5, 3, 7], 3))  # None
