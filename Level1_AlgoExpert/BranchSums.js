// This is the class of the input root.
// Do not edit it.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function branchSums(root) {
  console.log("Inside");
  sum = 0;
  sum = visitNode(root);
  console.log(sum);
}

function visitNode(node){
  sum = sum + node.value;
  node.visited = true;
  if(node.left && node.left.visited != true){
    visitNode(node.left);
  };
  if(node.right && node.right.visited != true){
    visitNode(node.right);
  };
  return sum;
}

// Do not edit the lines below.
exports.BinaryTree = BinaryTree;
exports.branchSums = branchSums;



BST = branchSums(4)
print(BST.value)