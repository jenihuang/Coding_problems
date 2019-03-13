def delete_nth(order, max_e):
    # if N is 1, return a set
    # if N is greater than 1, if list.count item is less than N, then append else continue

    final = []
    for i in order:
        if final.count(i) < max_e:
            final.append(i)
        else:
            continue

    return final
