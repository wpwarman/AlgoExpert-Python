print("Branch Sums")
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	BST = BinaryTree(root)
	print(BST)
	return BST

def buildTree(array):
	print(a)
	while len(a):
		node = BinaryTree(a.pop())
		node.left = BinaryTree(a.pop())
		node.right = BinaryTree(a.pop())
	return node
	


a = [6,7,82,1,25,44,2,96,54]
print(a)
buildTree(a)
print(a)


BST = branchSums(4)
print(BST.value)