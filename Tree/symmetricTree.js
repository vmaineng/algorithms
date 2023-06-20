const isSymmetric = (root) => {
  //use dfs

  //if root is empty, return null
  //pass in left root, pass in right root
  //if left is empty, right is empty, length does not equal the same, return false
  //check if root on other side is same side as the other side

  if (!root) return;
  return isMirror(root.left, root.right);

  function isMirror(leftNode, rightNode) {
    if (
      (!leftNode && rightNode) ||
      (!rightNode && leftNode) ||
      (leftNode && rightNode && leftNode.val !== rightNode.val)
    )
      return false;
    if (leftNode && rightNode)
    //looking at left node values, right node values first time
        //second recursive call, look at the right side to compare to the leftNode vals
      return (
        isMirror(leftNode.left, rightNode.right) &&
        isMirror(leftNode.right, rightNode.left)
      );
    return true;
  }
};

console.log(isSymmetric([1, 2, 2, 3, 4, 4, 3]));
