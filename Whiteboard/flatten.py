def flatten_list(lst):
    result = []
    for i in range(len(lst)):
        if type(lst[i]) != list:
            result.append(lst[i])
        else:
            l = flatten_list(lst[i])
            for e in l:
                result.append(e)
    return result


print(flatten_list([1, [2, 3, [4]], 5, [6]]))
