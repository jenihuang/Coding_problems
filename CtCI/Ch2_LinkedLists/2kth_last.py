import unittest


def find_kth_last(ll, k):

    a = ll.head
    for i in range(k):
        if not a:
            return None
        a = a.next

    b = ll.head

    while a:
        a = a.next
        b = b.next

    return b
