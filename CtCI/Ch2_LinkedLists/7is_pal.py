from ll import LinkedList, Node
'''pass in an array of appended values into recursion and pop first and check'''

# def is_pal(ll):
#     return is_pal_helper(ll.head, [])


## recursive function doesn't append the first number? why?
# def is_pal_helper(node, arr=[]):
#     if not node.next:
#         out = arr.pop(0)
#         if out == node.value:
#             return True
#         else:
#             return False
#     else:
#         arr.append(node.value)
#         print(node.value, arr)
#         if is_pal_helper(node.next):
#             out = arr.pop(0)
#             if out == node.value:
#                 return True

#         return False

''' use two pointers and create a stack up to the middle to check pal'''


def is_pal(ll):
    slow = fast = ll.head
    stack = []
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        out = stack.pop()
        if slow.value != out:
            return False
        slow = slow.next

    return True


''' create reversed linked list and traverse both together'''
## reversed ll only includes nodes with the first value? why?
# def create_reverse(node, new=LinkedList()):
#     if not node.next:
#         n = Node(node.value)
#         new.add(n)
#         new.head = n
#     else:
#         create_reverse(node.next)
#         n = Node(node.value)
#         new.add(n)

#     current = new.head
#     while current:
#         print(current.value)
#         current = current.next

#     return new


# def is_pal(ll):
#     new_ll = create_reverse(ll.head)
#     current = ll.head
#     reverse = new_ll.head

#     while current and reverse:
#         print(current.value, reverse.value)
#         if current.value != reverse.value:
#             return False
#         current = current.next
#         reverse = reverse.next

#     return True


ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_pal(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_pal(ll_false))
