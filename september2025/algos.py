from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #receive a root node for a binary tree
        #return an integer where the max sum of all nodes are from the youngest level

        #ex:   10
        #.     /\
        #.    4. 5
        #    /\ 
        #   6 2

        #1st round: level 1: 10
        #2nd level: 4 + 5 = 9
        #3rd level: 6 + 2 = 8 

        #return 1

        #initialize a queue that will help with BFS
        #intitalize a total variable
        #initialize a level variable
        #capture the root node as the current node
        #add the current node into the queue
        #add up the total for the level
        #check if the level is greater than what we have currently seen, 
        #if level is greater, update the total and the level
        #check the new level


        #edge case: 
        #if the root node is empty, return 0

        if not root:
            return 0

        queue = deque([root])
        maxTotal = float("-inf")
        maxLevel = 0
        level = 1

        while queue:
            level_size = len(queue)
            currTotal = 0

            for node in range(level_size):
                node = queue.popleft()
                currTotal += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            if currTotal > maxTotal:
                maxTotal = currTotal
                maxLevel = level
        
            level += 1
        return maxLevel
    
    from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #receive a root node
        #return the smallest level at which the total is the biggest
        #

        #intiialize a deque with the root
        #intialize a maxtotal, level, maxLevel
        #iterate while the deque still has levels
        #add the current nodes to the queue
        #add up total
        #if they have a left or right nodes, to the queue
        #check if total is greater than max total
        #update totaland level
        #increment total
        #return level

        if not root:
            return 0

        maxLevel = 0
        level = 1
        maxTotal = float('-inf')
        queue = deque([root])

        while queue:
            total = 0

            for node in range(len(queue)):
                current = queue.popleft()
                total += current.val

                if (current.left):
                    queue.append(current.left)
                if(current.right):
                    queue.append(current.right)
            if total > maxTotal:
                maxTotal = total
                maxLevel = level

            level += 1
        return maxLevel


        

