def find_uniq(arr):
    n = None
    duplicate = None
    test = arr[0]
    
    for i in range(1,3):
        if arr[i] == test:
            duplicate = arr[i]
            break
        else:
            duplicate = arr[i]
    
    s = set(arr)
    for i in s:
        if i != duplicate:
            n = i
        
    return n   # n: unique integer in the array