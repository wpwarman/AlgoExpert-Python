from binarytree import build

print("Find the Closest Value in a BST")

# Create the BST
nodes = [10, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14, None, None]
BST = build(nodes)
target = 12

print("The BST:")
print(BST)
print("The Target: ", target)

# Visit each node
print("List of the node values: ", list(BST))
print("Value of a the 7th node: ", list(BST)[6].value)