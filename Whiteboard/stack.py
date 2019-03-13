class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return '{}'.format(self.value)


class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def __repr__(self):
        result = []
        node = self.head

        while node:
            result.append(node.value)
            node = node.next
        return str(result)

    def push(self, value):
        n = Node(value)

        prev = self.head
        self.head = n
        self.head.next = prev
        self.count += 1

    def pop(self):
        if self.head:
            selected = self.head
            self.head = self.head.next
            self.count -= 1
            return selected
        else:
            return None

    def peek(self):
        return self.head.value

    def is_empty(self):
        return (self.head is None)

    def empty(self):
        self.head = None
        self.count = 0

    def length(self):
        return self.count


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
s = Stack()
s.push(n1)
s.push(n2)
s.push(n3)
