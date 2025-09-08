from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leftSideView(self, root):
        #receive a root node of a binary tree
        #return a list of node values for left nodes going from right to left BFS

        #initilize a result list
        #initialize a leftNode value

        #insert root node into a queue
        #popleft and update value for leftNode
        
        #add in right child node to queue
        #add in left child node to queue

        #add in leftNodeVal to result's queue
        #return result

        if not root:
            return []

        result = []
        queue = deque([root])
        leftNodeVal = None

        while queue:
            for node in range(len(queue)):
                current = queue.popleft()
                leftNodeVal = current.val

                if (current.right):
                    queue.append(current.right)
                if (current.left):
                    queue.append(current.left)
            result.append(leftNodeVal)
        
        return result

    print(leftSideView([1,2,3,None,5,None,4]))