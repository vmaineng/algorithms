const binaryTreePaths = (root) => {
//if root is empty return, 
//initialize an array to capture the individual path
//return a recursive path of binary tree(leftside, rightside)
//push the path in to an array
//if it has no more value, then it is a leaf

// if (!root) return null;

let result = [];

function traverse(node, path){ 
    //if node is empty, return
    if (!node) return;
    //create a path
    const setPath = path === "" ? node.val + "" : path + "->" + node.val
    if(!node.left && !node.right) result.push(setPath)
    //traverse left and create a path
    if (node.left) traverse(node.left, setPath)
    //traverse right and create a path
    if (node.right) traverse(node.right, setPath)
}
traverse(root, "")
return result;
}

console.log(binaryTreePaths([1, 2,3, null, 5]))