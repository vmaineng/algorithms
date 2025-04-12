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

    def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

def findClosestValueInBst(tree, target):
    #receive a root node of a tree, and target of node's value
    #return the node's value that is closest to target's

    #
    #keep track of the node that's closest to target
    #keep track of min diff

    #check if target is < root's node 
    #then traverse the left side
    #else traverse through the right side

    closestNode = None
    minDiff = float('inf')

    if tree.value < target:
        findClosestValueInBst(tree.left, target)
        nodeDiff = tree.left - target
        node = tree.left
        if nodeDiff < minDiff:
            minDiff = nodeDiff
            closestNode = node
    else: 
        findClosestValueInBst(tree.right, target)
        nodeDiff = tree.right - target
        node = tree.right
        if nodeDiff < minDiff:
            minDiff = nodeDiff
            closestNode = node
    return closesetNode

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    return findClosest(tree, target, tree.value)

def findClosest(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosest(tree.left, target, closest)
    elif target > tree.value:
        return findClosest(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def findClosestValueInBst(tree, target):
    return findClosest(tree, target, tree.value)

def findClosest(tree, target, closest):
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosest(tree.left, target, closest)
    elif target > tree.value:
        return findClosest(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def str_count(strng, letter):
    # receive a string of lowercase and uppercase chars
    #return back an integer how many times the letter occurs in the string
    
    #ex: 'hello', 'l' => 2
    #.          i
    #count = 2
    
    #ex: 'zerbra', 'q' => 0
    
    #brute force:
    #initialize a count variable, set it 0 
    #iterate through each individual char
    #check to see if letter is equal the current letter we are at in string
    #if they are, increment count
    #else, move on to the next char in strin
    #return count
    
    count = 0
    for char in strng:
        if char == letter:
            count += 1
    return count

    import re

def validate_pin(pin):
    # received a string - contain letters, numbers, chars
    #return true if valid pin, else false
    #valid pin= 4 or 6 digits of numbers only
    
    #ex: '#345' => False
    #ex: '345' => False
    #ex: 'A1B2C3' => False
    #ex: '567899' => True
    
    #brute force:
    #check to see if the length properties are equal to 4 and 6, return false
    
    
    #check to see if string does not matches only 0-9 chars, return false, else return true
    
    regex = "^\d*$" #"^\d*$"
    return re.match(regex, pin) and (len(pin) == 4 or len(pin) == 6)
#         return True
#     else:
#         return False

def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

    def findClosestValueInBst(tree, target):
    #receive a tree and an integer target
    #return the closest value to the target's value

    #create a helper function that will traverse
    #keep track of the target- closet
    #if the target's closest - current node < target-closes,t update it
    #else traverse left , else traverse right
    #return closest

    return findClosest(tree, target, tree.value)

def findClosest(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
        
    if target < tree.value:
        return findClosest(tree.left, target, closest)
    elif target > tree.value:
        return findClosest(tree.right, target, closest)
    else:
        return closest
        
    


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        def findClosestValueInBst(tree, target):
    return findClosest(tree, target, tree.value)

def findClosest(tree, target, closest):
    if tree is None:
        return closest

    if abs(target-closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosest(tree.left, target, closest)
    elif target > tree.value:
        return findClosest(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minHeightBst(array):
    return constructBST(array, 0, len(array) - 1)

def constructBST(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    node = BST(array[mid])
    node.left = constructBST(array, start, mid - 1)
    node.right = constructBST(array, mid+1, end)
    return node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def minHeightBst(array):
    #receive an array of sorted distinct integers
    #return the root of the bst

    #find the middle of array
    #make it the root of bst
    #traverse through left side of middle and create left tree
    #traverse through right side of middle and create the right tree
    #return the tree

    return minHeight(array,None, 0, len(array) - 1)

def minHeight(array, bst, start, end):
    if start > end:
        return None

    midIdx = (start + end) // 2
    if bst is None:
        bst = BST(array[midIdx])
    else:
        bst.insert(array[midIdx])

    minHeight(array, bst, start, midIdx - 1)
    minHeight(array, bst, midIdx + 1, end)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def findClosestValueInBst(tree, target):
    #receive a tree and target's value
    #return the closest Node that either matches target or is the closest to the target

    #initialize a helper function that will traverse
    #if tree is empty, return the closest node found
    #if the target's value - closest's value is bigger than the target's value - current node's value
    #update the node to the closest
    #check if the target's node is less than tree's node, then traverse left
    #else traverse right
    #return the node

    return closestHelper(tree, target, tree.value)

def closestHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return closestHelper(tree.left, target, closest)
    elif target > tree.value:
        return closestHelper(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        def findClosestValueInBst(tree, target):
    return findClosest(tree, target, tree.value)

def findClosest(tree, target, closest):
    currentNode = tree

    while currentNode is not None:

        if abs(target-closest) > abs(target - currentNode.value):
            closest = currentNode.value
    
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#the other one is done recursively = which uses function call stack
#the other one is done itertively = saves more on spaces

def minHeightBst(array):
    #receive an array of sorted distinct integers
    #return a BST of min height

    #calc the middle of array
    #insert into BST
    #then calc the middle of the left side of array, insert into bst
    #calc the middle of right side, insert into bst
    #return bst

    return minHeightHelper(array, None, 0, len(array) - 1)

def minHeightHelper(array, bst, start, end):
    if end < start:
        return None

    middle = (start + end) // 2
    if bst is None:
        bst = BST(array[middle])
    else:
        bst.insert(array[middle])
    leftNode = minHeightHelper(array, bst, start, middle - 1)
    rightNode = minHeightHelper(array, bst, middle + 1, end)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
def minHeightBst(array):
    #receive an array of sorted distinct integers
    #return a BST of min height

    #calc the middle of array
    #insert into BST
    #then calc the middle of the left side of array, insert into bst
    #calc the middle of right side, insert into bst
    #return bst

    return minHeightHelper(array, 0, len(array) - 1)

def minHeightHelper(array, start, end):
    if end < start:
        return None

    middle = (start + end) // 2
    bst = BST(array[middle])
    bst.left = minHeightHelper(array, start, middle - 1)
    bst.right = minHeightHelper(array, middle + 1, end)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
#to go from iterative to recursive: 
#use the properties of left to assign all left nodes
#use right to assign all right notes

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #receive a grid of m x n 
        #return max area of an island in grid

        #iterate through row and cols
        #if the value is a 1, perform dfs
        #return the size from dfs

        #edge case: if grid is empty, return 0

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            size = 1
            size += dfs(row + 1, col)
            size += dfs(row - 1, col)
            size += dfs(row, col - 1)
            size += dfs(row, col + 1)
            return size

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    size = dfs(row, col)
                    max_area = max(max_area, size)
        return max_area
        