const mergeTrees = (root1, root2) => {
    //if tree1 is empty, return tree2 and vice versa

    //intiailize a node to add the value from tree1 to tree 2 in 
    //the respective area

    //traverse through left nodes, then traverse through right nodes
    //then return the node

    if (!root1 || !root2) return root1 || root2;

    root1.val += root2.val

   root1.left = mergeTrees(root1.left, root2.left)
   root1.right = mergeTrees(root1.right, root2.right)

    return root1
}

console.log(mergeTrees([1,3,2,5], [2,1,3,null,4,null,7]))