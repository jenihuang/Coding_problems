class Node:

    def __init__(self, value, nextNode=None, prev=None):
        self.value = value
        self.next = nextNode
        self.prev = prev


class LinkedList:

    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.length = 0
        if values:
            self.add_many(values)

    def add(self, value):

        n = Node(value)

        if self.tail:
            self.tail.next = n
            self.tail = n
        else:
            self.head = n
            self.tail = n

        self.length += 1

    def add_many(self, values):
        for v in values:
            self.add(v)

    def remove(self, value):

        current = self.head
        prev = None

        while current:
            if current.value == value:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                elif self.head == current:
                    self.head = current.next
                elif self.tail == current:
                    prev.next = None
                    self.tail = prev
                else:
                    prev.next = current.next

                self.length -= 1
                break
            else:
                prev = current
                current = current.next
