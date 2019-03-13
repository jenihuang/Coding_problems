def loop_size(node):
    # initialize turtle and hare variables
    t = node.next
    h = node.next.next

    # while the two pointers don't meet
    while t != h:
        # increment turtle by 1 step
        t = t.next
        # increment hare by 2 steps
        h = h.next.next

    # exit the while loop(turtle and hare are on the same node)

    # increment turtle by 1 step
    t = t.next
    # set count to 1
    count = 1

    # while the two pointers don't meet
    while t != h:
        # increment turtle by 1 step
        t = t.next
        # increment count by 1
        count += 1

    # exited the while loop (they met), return the count
    return count
