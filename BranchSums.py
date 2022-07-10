from binarytree import build, Node

print("Branch Sums")

# Create the BST
nodes = [10, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14, None, None]
BST = build(nodes)

print("The BST:")
print(BST)

# Visit each node
print("Visit nodes depth-fist")

Node.hasBeenVisited = False
currentNode = BST[0]
print(currentNode.hasBeenVisited)

while True:
	if currentNode.hasBeenVisited is False:	
		print("The value of the current node is:", currentNode.value)
		if currentNode.left is not None:
			currentNode = currentNode.left
		elif currentNode.right is not None:
			currentNode = currentNode.right
		else:
			currentNode.hasBeenVisited = True
	else:
		print("I hit the bottom")
		break

print("------ And Again -------")

currentNode = BST[0]
while True:	
	if currentNode.hasBeenVisited is False:
		print("The value of the current node is:", currentNode.value)	
		if currentNode.left is not None:
			currentNode = currentNode.left
		elif currentNode.right is not None:
			currentNode = currentNode.right
		else:
			currentNode.hasBeenVisited = True
	else:
		print("Hit the bottom")
		break