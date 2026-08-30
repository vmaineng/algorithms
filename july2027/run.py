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

        