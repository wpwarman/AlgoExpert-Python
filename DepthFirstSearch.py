from binarytree import build, Node

print("Depth First Search")

# Create the BST
nodes = [10, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14, None, None]
BST = build(nodes)
visitedNodes = set()
currentNode = BST[0]

def dfs(visitedNodes, BST, currentNode):
	if currentNode not in visitedNodes:
		print(f"The value of the current node is {currentNode.value}")
		visitedNodes.add(currentNode)
		if currentNode.left:
			dfs(visitedNodes, BST, currentNode.left)
		if currentNode.right:
			dfs(visitedNodes, BST, currentNode.right)
		
print(BST)
dfs(visitedNodes, BST, currentNode)