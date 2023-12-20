var isSameTree = function(p, q) {
    //root of two trees
    //return true if it matches, return false if the values do not match
   //1                1
//  /  \            /   \
//3    2           3     5   => false b/c 2 !== 5


//use DFS recursion:
//base cases:
//if both roots are empty, return true
//if one root is empty and the other has a value, return false
//if the root values do not match, return false

//return true if left node values === right node values

if (p === null && q === null) return true;
if (p === null || q === null) return false;
if (p.val !== q.val) return false;

return (isSameTree(p.left, q.left) && isSameTree(p.right, q.right))
};