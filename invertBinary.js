const invertTree = (root) => {
//if the root is empty, return the root

//BFS - level order traversal would not work b/c it's not a BST
// ! uses DFS b/c started at the most left node
//create queue to store the values
//then shift and unshift out of the queue the values 

if (root === null) return root;

//calling function recursively for left subtree
invertTree(root.left)

//calling function recursively for right subtree
invertTree(root.right)


//swapping node values
let curr = root.left
root.left = root.right
root.right = curr
return root

}

console.log(invertTree([2, 1, 3]))