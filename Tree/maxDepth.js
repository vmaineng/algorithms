//given the root of a binary tree, return its max depth
//a binary tree's max depth is the number of nodes along
//the longest path from the root node down to the 
//farthest leaf node

const maxDepth = (root) => {
    //root of the tree - first node on top
    //return the max level of the farthest root down the tree
    //[3, 9, 20, null, null, 15, 7, null, 4, 5] => 4 levels

    //if root is empty, return depth as 0;

    //using dfs, 
    //each function call will present a subtree which has a root node
    //pass in left and right node
    //increase levels + 1
    //return levels

    if (!root) return 0;

    let leftDepth = maxDepth(root.left);
    let rightDepth = maxDepth(root.right);

    return Math.max(leftDepth, rightDepth) + 1; //add 1 to account for the current node (parent)


}