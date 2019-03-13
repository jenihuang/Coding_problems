class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return '{}'.format(self.value)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def __repr__(self):
        result = []
        node = self.head

        while node:
            result.append(node.value)
            node = node.next
        return str(result)

    def enqueue(self, value):
        n = Node(value)

        if self.head:
            self.tail.next = n

        else:
            self.head = n

        self.tail = n
        self.count += 1

    def dequeue(self):
        selected = self.head
        self.head = self.head.next
        self.count -= 1
        return selected

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
q = Queue()
q.enqueue(n1)
q.enqueue(n2)
q.enqueue(n3)
