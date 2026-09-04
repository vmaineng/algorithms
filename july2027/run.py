def findNums(array):
    #receive a list of non-negative int and strings
    #return int only

    return [num for num in array if isinstance(num, int)]

# print(findNums([2, "2"]))


def pantagram(string):
    seen = set()

    for char in string.lower():
        if char not in seen:
            seen.add(char)

        if len(seen) == 26:
            return True
    return False

# print(pantagram("The quick brown fox jumps over the lazy dog"))


#check if string has same amount of x's and o's
#P: string a of x's and o's (upper and lower and could contain other alpha characters)
#r: true if equal amount of x's and o's, else False
#ex: 'AxOdXo' => x: 2, o: 2 => 2 == 2 => True
#ex: 'xOo' => x: 1, o:2 => False

#iterate through the string
#keep track of the count of x and o
#compare our totals to see if they == each other, return True, else False

def countXO(str):
    x = 0
    o = 0

    for char in str.lower(): #x = 1, o = 2
        if char == 'x':
            x += 1
        elif char == "o":
            o +=1

    return x == o #1 == 2 => False

# print(countXO('AxOdXo')) 
# print(countXO('xOo'))


def isItNext(string):
    #receive a string of chars
    #return True if they are not next to it, else False
    #ex: 'abc'=> False

    i = 0

    for char in range(1, len(string)):
        if ord(string[char]) == ord(string[i])+ 1:
            return True
    return False

print(isItNext('abc'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #receive the root of a binary tree
        #return boolean where true if balanced by no more than 1,e lse false

        #iterate through left trees, keep track of it
        #iterate through right trees, keep track of nodes
        #check if it's not off by 1, return true, else return False

        if not root:
            return True

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def getHeight(self, node):
        if not node:
            return 0

        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        return 1 + max(leftHeight, rightHeight)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            current_level= []
            size = len(queue)

            for _ in range(size):
                current = queue.popleft()
                current_level.append(current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
            result.append(current_level)
        return result

    class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #receive a a list of strings
        #return the most common prefix
        #ex: 

        #start out with the first word in the list
        #iterate through the rest of the strings in the list
        #if they are not the same, break and return what you have up to
        #else, return the netire word b/c they are the same prefix

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]

        #time:O(n * m)
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #receive the root node
        #return longest path
        #ex:

        #get the height of the tree


        self.diameter = 0
        self.getHeight(root)
        return self.diameter
        

    def getHeight(self, node):
        if not node:
            return 0 

        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        self.diameter = max(self.diameter, leftHeight+ rightHeight)

        return 1 + max(leftHeight, rightHeight)

        # The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #receive a number from 1 to n:
        #return the number if it was picked
        #ex: 

        # for num in range(1, n + 1):
        #     if guess(num) == 0:
        #         return num

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid - 1
            else:
                left = mid + 1
        
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #receive a binary tree node
        #return binary tree's height true or false

        return self.getHeight(root) != -1

        
    def getHeight(self, node):
        if not node:
            return 0
        leftHeight = self.getHeight(node.left)

        if leftHeight == -1:
            return -1

        rightHeight = self.getHeight(node.right)

        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1
        return 1 + max(leftHeight, rightHeight)

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #receive the root node of a tree
        #return boolean if same tree, else False
        #ex: 

        #iterate through left and right
        #if they aren't the same, return False immediately,e lse return True after traversing

        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #receive the root node
        #return True if valid bst else false
        #ex: 

        if not root:
            return True

        if root.left < root.val < root.right:
            return True
        else:
            return False

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #receive the root of a binary tree
        #return the length of any two nodes 
        #ex:

        #if root is empty, return 0 b/c no path
        #else get the height
        #look at the left height vs right height to get diameter
        self.diameter = 0
        self.getHeight(root)
        return self.diameter


    def getHeight(self, node):
        if not node:
            return 0
        
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)

        self.diameter = max(self.diameter, leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)


        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if you get a root node and a subroot node
        #return if subtree is part of a node
        #ex:

        if not subRoot:
            return True
        
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False