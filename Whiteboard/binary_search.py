def binary_search(arr, n):
    sm = 0
    lg = len(arr) - 1

    while sm < lg:
        mid = (sm + lg) // 2
        if n == arr[mid]:
            return mid

        elif n > arr[mid]:
            sm = mid + 1

        else:
            lg = mid - 1

    return None


print(binary_search([1, 2, 3, 4, 5, 7, 9], 8))
