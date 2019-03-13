def array_diff(a, b):
    final = []
    for i in a:
        if i not in b:
            final.append(i)

    return final
