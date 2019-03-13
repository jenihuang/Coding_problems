def queue_time(customers, n):
    # array length n with each index representing a queue
    # append next customer to array index with lowest number for every customer

    tills = []
    for i in range(0, n):
        tills.append(0)
    for i in customers:
        minimum = min(tills)
        q = tills.index(minimum)
        tills[q] += i

    return max(tills)
