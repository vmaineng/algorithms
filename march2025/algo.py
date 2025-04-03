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
