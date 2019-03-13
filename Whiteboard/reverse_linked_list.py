'''given a linked list, return a reversed linked list'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return 'Node: {}'.format(self.value)


class LL:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        result = []
        node = self.root

        while node:
            result.append(node.value)
            node = node.next
        return str(result)

    def add(self, node):

        current = self.root

        while current.next:
            current = current.next

        current.next = node

    def reverse(self):
        self.reverse_helper(self.root, None)

    def reverse_helper(self, node, prev):
        if not node.next:
            self.root = node
            node.next = prev
        else:
            self.reverse_helper(node.next, node)
            node.next = prev

    def reverse_iter(self):
        self.reverse_iter_helper(self.root)

    def reverse_iter_helper(self, node):

        current = node
        prev = None

        while current.next:
            future = current.next
            current.next = prev
            prev = current
            current = future

        self.root = current
        current.next = prev

    def print_reverse(self):
        self.print_reverse_helper(self.root)

    def print_reverse_helper(self, node):
        if not node.next:
            print(node)
        else:
            self.print_reverse_helper(node.next)
            print(node)

    def reverse_with_return(self):
        return self.reverse_with_return_helper(self.root)

    def reverse_with_return_helper(self, node):
        if not node.next:
            return [node]
        else:
            node_list = self.reverse_with_return_helper(node.next)
            node_list.append(node)
            return node_list


n = Node(1)
n1 = Node(2)
n2 = Node(3)
ll = LL(n)
ll.add(n1)
ll.add(n2)

# ll.reverse_iter()
print(ll)
ll.reverse()
print(ll)
