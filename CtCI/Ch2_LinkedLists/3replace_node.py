import unittest


def remove(node):

    node.value = node.next.value
    node.next = node.next.next
