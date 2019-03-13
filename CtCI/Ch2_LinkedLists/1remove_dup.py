import unittest
from ll import Node, LinkedList


def remove_dup(ll):
    seen = {}

    current = ll.head
    seen.add(current.value)

    while current.next:
        if current.next.value not in seen:
            seen.add(current.next.value)
        else:
            current.next = current.next.next
        current = current.next

    return ll
