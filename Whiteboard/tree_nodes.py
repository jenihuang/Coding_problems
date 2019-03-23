from collections import deque


class Node(object):
    """Node in a tree.

    Create tree:
        >>> e = Node(99, [])
        >>> f = Node(7, [])
        >>> g = Node(7, [])
        >>> c = Node(3, [e])
        >>> d = Node(4, [f, g])
        >>> b = Node(2, [])
        >>> a = Node(1, [b, c, d])

    Tests:
        >>> a.length()
        7

        >>> a.has_dup()
        True

        >>> a.is_found(3)
        True

        >>> a.is_found(5)
        False

        >>> a.find(4).data
        4

        >>> a.find(3).data
        3

        >>> a.find(12)
        False
        
        >>> a.insert_node(Node(100, []), 99)
        >>> e.children[0].data
        100

        >>> a.remove_node(99)
        >>> c.children[0].data
        100


    """

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def length(self):
        """returns number of nodes in the tree"""
        count = 1

        if not self.children:
            return count
        else:
            for child in self.children:
                count += child.length()
        return count

    def has_dup(self):
        """returns True if any two nodes have duplicates"""

        a = set()

        return self.has_dups_helper(a)

    def has_dups_helper(self, dups):

        if self.data in dups:
            return True
        else:
            dups.add(self.data)
            for child in self.children:
                if child.has_dups_helper(dups):
                    return True
        return False

    def is_found(self, value):
        """returns True if value is found in the tree"""
        if self.data == value:
            return True
        if self.children:
            for child in self.children:
                if child.is_found(value):
                    return True
        return False

    def find(self, value):
        """returns highest ranking node with that value"""
        q = deque()
        q.append(self)

        while q:
            out = q.popleft()
            if out.data == value:
                return out
            else:
                q.extend(out.children)

        return False

    def insert_node(self, node, value):
        """inserts node as a child of node in tree with specified value"""

        parent = self.find(value)
        if parent:
            parent.children.append(node)
        else:
            raise Exception('value not found')

    def remove_node(self, value):
        """remove nodes with given value"""
        if self.data == value:
            first = self.children[0]
            self.data = first.data
            self.children.remove(first)
        else:
            self.remove_node_helper(value, None)

    def remove_node_helper(self, value, parent):
        if self.data == value:
            parent.children.extend(self.children)
            parent.children.remove(self)
        else:
            for child in self.children:
                child.remove_node_helper(value, self)


class BinarySearchNode(object):
    """Binary tree node.

    Create tree:
        >>> h = BinarySearchNode(9)
        >>> i = BinarySearchNode(12)
        >>> e = BinarySearchNode(10, h, i)
        >>> f = BinarySearchNode(2)
        >>> g = BinarySearchNode(4)
        >>> d = BinarySearchNode(6)
        >>> c = BinarySearchNode(8, d, e)
        >>> b = BinarySearchNode(3, f, g)
        >>> a = BinarySearchNode(5, b, c)

    Tests:
        >>> a.print_tree()
        5
        3
        8
        2
        4
        6
        10
        9
        12

        >>> a.find(8).data
        8

        >>> a.find(10).data
        10

        >>> a.length()
        9

        >>> z = BinarySearchNode(20)
        >>> a.insert(z)
        >>> i.right.data == z.data
        True
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_tree(self):
        q = deque()
        q.append(self)

        while q:
            out = q.popleft()
            print(out.data)
            if out.left:
                q.append(out.left)
            if out.right:
                q.append(out.right)

    def find(self, value):
        """returns node in BST with given value"""
        if self.data == value:
            return self
        if not self.left and not self.right:
            return False
        else:
            l_child = self.left.find(value)
            r_child = self.right.find(value)
            return l_child or r_child

    def length(self):
        """return number of nodes in the tree"""
        count = 1

        if not self:
            return 0
        else:
            if self.left:
                count += self.left.length()
            if self.right:
                count += self.right.length()
        return count

    def insert(self, node):
        """insert into BST at proper location"""
        if not self.left and node.data < self.data:
            self.left = node
        elif not self.right and node.data > self.data:
            self.right = node
        else:
            if node.data < self.data:
                self.left.insert(node)
            else:
                self.right.insert(node)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
