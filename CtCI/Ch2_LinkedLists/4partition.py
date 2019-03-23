'''create 3 sections first, mid, last and join them'''
from ll import LinkedList, Node


def partition(ll, x):
    first_head = first_tail = Node()
    mid_head = mid_tail = Node()
    last_head = last_tail = Node()

    current = ll.head

    while current:
        if current.value == x:
            mid_tail.next = current
            mid_tail = current
        elif current.value < x:
            first_tail.next = current
            first_tail = current
        else:
            last_tail.next = current
            last_tail = current
        current = current.next

    last_tail.next = None

    mid_tail.next = last_head.next

    first_tail.next = mid_head.next

    ll.head = first_head.next


ll = LinkedList()
ll.add_many([10, 0, 99])
print(ll)

partition(ll, ll.head.value)
print(ll)
