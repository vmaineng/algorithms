// Given the root of a binary tree, 
// invert the tree, and return its root.

const invertTree = (root) => {
//root of a tree (parent node)
//return the tree with nodes flipped
//     4
//   3    5
// 2        9
// => 

//     4
//   5   3
// 9       2


//if tree root is empty, return null; 
//recusively pass in the nodes
//tell left node to replace right node
//return the root

if (!root) return root;

invertTree(root.left);
invertTree(root.right);

let curr = root.left;
root.left = root.right;
root.right = curr;

return root


}

console.log(invertTree([4,5,3,9,2]))