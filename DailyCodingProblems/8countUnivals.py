'''
count univals in a binary tree
all leaves are univals
whole tree has to be unival
'''

class Node(object):
	def __init__ (self,value,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right

	def __eq__ (self,other):
		if self is None or other is None:
			return False
		else:
			return self.value == other.value


def countUni(root):
	if not root:
		return (0, True)

	else:
		value1,flag1 = countUni(root.left)
		value2,flag2 = countUni(root.right)
		if root.left == root.right and flag1 and flag2:
			return ((1 + value1 + value2), True)
		else:
			return ((value1 + value2), False)

N1 = Node(0)
N2 = Node(1)
N3 = Node(0)
N4 = Node(1)
N5 = Node(0)
N6 = Node(1)
N7 = Node(1)

N1.left = N2
N1.right = N3
N3.left = N4
N3.right = N5
N4.left = N6
N4.right = N7

print(countUni(N1))






