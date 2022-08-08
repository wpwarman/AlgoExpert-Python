from binarytree import build

print("Depth First Search")

# Create the BST
nodes = [10, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14, None, None]
BST = build(nodes)
visitedNodes = set()
total = 0

def dfs(visitedNodes, BST, currentNode, total):
	print(f"The value of the current node is {currentNode.value}")
	total = total + currentNode.value
	if currentNode not in visitedNodes:
		visitedNodes.add(currentNode)
		if currentNode.left:
			dfs(visitedNodes, BST, currentNode.left, total)
		if currentNode.right:
			dfs(visitedNodes, BST, currentNode.right, total)
		if not currentNode.right and not currentNode.left:
			print(f"I've hit rock bottom: {total}")
			
print(BST)
dfs(visitedNodes, BST, BST[0], total)