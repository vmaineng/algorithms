def findClosestValueInBst(tree, target):
    # receive a BST, and a target node's value
    #return the closest Value in BST, else return the node's value if value matches
    #ex: 3 => 3

    #iterate through the root node
    #check if the value is = target
    #return root node
    #else check if target's value < root ndoe, then traverse left
    #else traverse right

    treeNode = None
    teeDistance = 0

    if tree == target:
        return true
    elif target < tree.value:
        return findClosestValueIn
    


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    def inOrderTraversal(node):
        if node is None:
            return []
        return inOrderTraversal(node.left) + [node.value] + inOrderTraversal(node.right)

    all_values = inOrderTraversal(tree)
    closest = None
    min_diff = float('inf')
    for value in all_values:
        current_diff = abs(value - target)
        if current_diff < min_diff:
            min_diff = current_diff
            closest = value
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:

    def encode(self, strs: List[str]) -> str:
        return '#'.join(strs)
        
    def decode(self, s: str) -> List[str]:
        return s.split('#')
