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
def inOrderTraverse(tree, array):
    #starts from bottom left, to top, to bottom right
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array
    


def preOrderTraverse(tree, array):
    # starts from root, to left, to right
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    # bottom left, to bottom right, to top
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

def inOrderTraverse(tree, array):
    #create a stack
    #check if the tree not empty
    #set the node to current tree node
    # while the stack or the current is not empty:
    #while current is not empty:
    #add the curr node to the stack
    #then go left, and capture all nodes
    #pop it off 
    #add to the array
    #then repeat with items on right side
    stack = []
    if tree is not None:
        curr = tree
    while stack or curr is not None:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        array.append(curr.value)
        curr = curr.right
    return array


def preOrderTraverse(tree, array):
    # initialize a stack
    #if tree is not empty, add in top root node's value
    #while stack still has items to go through
    #pop off of current node
    #add to the array
    #go right, then go left, then pop off stack (b/c can only pop off from the end)
    #then add to the array
    #return array

    stack =[]
    if tree is not None:
        stack.append(tree)
    while stack:
        curr = stack.pop()
        array.append(curr.value)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return array
        


def postOrderTraverse(tree, array):
    #initialize a stack
    #go 

    stack = []
    if tree is not None:
        stack.append(tree)
    while stack:
        curr = stack.pop()
        array.append(curr.value)
        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)
    return array[::-1]

def other_angle(a, b):
    #receive two integers, positive and whole numbers
    #return the 3rd angle
    #ex: 30, 60 => 90
    #ex: 40, 50 => 180 - 90 => 90
    
    #brute force:
    #calculate the total of a + b - 180
    #return the third angle
    
    thirdAngle = 180 - (a + b)
    return thirdAngle



def twice_as_old(dad_years_old, son_years_old):
    #receive two whole positive integers
    #return the years the father was twice as old as son
    
    #ex: (42, 0) => 42
    
    #ex: (24, 12) => 0
    
    #brute force, take dad's year / son's year anad float it donw
    
    #take son's age * 2 and subtract from dad's age
    
    return abs(dad_years_old - (son_years_old * 2))