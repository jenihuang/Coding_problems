class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def create(self, arr):
        self.root = Node(arr[0])
        self.create_helper(arr[1:], self.root)

    def create_helper(self, arr, node):
        if not arr:
            return
        if arr[0] in ['+', '-', '*', '/']:
            r = Node(arr[0])
            r.left, remainder_list = self.create_helper(arr[1:])
            r.right, remainder_list = self.create_helper(remainder_list)
            return
        else:
            return Node(arr[0], arr[1:])

    def traverse(self, node):
        current = node

        if not current.right and current.left:
            print(current.value)
        else:
            if current.left:
                self.traverse(current.left)
            if current.right:
                self.traverse(current.right)
            print(current.value)


t = Tree()
t.create(["*", "2", "+", "1", "2"])
t.traverse(t.root)
