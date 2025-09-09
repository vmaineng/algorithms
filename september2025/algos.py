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


        from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        #receive a root of a binary tree
        #return a list back of the right nodes only

        #edge case, if empty, return an empty list
        #else, traverse only on the right side only

        queue = deque([root])
        result = []
        right_node_val = None

        if not root:
            return result

        while queue:
            for node in range(len(queue)):
                current = queue.popleft()
                right_node_val = current.val

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(right_node_val)
        return result

def subtract_sum(number):
    #receive a number
    #return the fruit assocated with the number
    
    #ex: 34 => 3+4 = 7
    #34 -7= 27 => 'apple'
    
    #initialize a total
    #iterate through number
    #add them up
    #subtract from first number
    #check if num in list
    #return fruit
    
    fruits = {1: "kiwi",
              2: "pear",
    3:"kiwi",
    4:"banana",
    5:"melon",
    6:"banana",
    7:"melon",
    8:"pineapple",
    9:"apple",
    10:"pineapple",
    11:"cucumber",
    12:"pineapple",
    13:"cucumber",
    14:"orange",
    15:"grape",
    16:"orange",
    17:"grape",
    18:"apple",
    19:"grape",
    20:"cherry",
    21:"pear",
    22:"cherry",
    23:"pear",
    24:"kiwi",
    25:"banana",
    26:"kiwi",
    27:"apple",
    28:"melon",
    29:"banana",
    30:"melon",
    31:"pineapple",
    32:"melon",
    33:"pineapple",
    34:"cucumber",
    35:"orange",
    36:"apple",
    37:"orange",
    38:"grape",
    39:"orange",
    40:"grape",
    41:"cherry",
    42:"pear",
    43:"cherry",
    44:"pear",
    45:"apple",
    46:"pear",
    47:"kiwi",
    48:"banana",
    49:"kiwi",
    50:"banana",
    51:"melon",
    52:"pineapple",
    53:"melon",
    54:"apple",
    55:"cucumber",
    56:"pineapple",
    57:"cucumber",
    58:"orange",
    59:"cucumber",
    60:"orange",
    61:"grape",
    62:"cherry",
    63:"apple",
    64:"cherry",
    65:"pear",
    66:"cherry",
    67:"pear",
    68:"kiwi",
    69:"pear",
    70:"kiwi",
    71:"banana",
    72:"apple",
    73:"banana",
    74:"melon",
    75:"pineapple",
    76:"melon",
    77:"pineapple",
    78:"cucumber",
    79:"pineapple",
    80:"cucumber",
    81:"apple",
    82:"grape",
    83:"orange",
    84:"grape",
    85:"cherry",
    86:"grape",
    87:"cherry",
    88:"pear",
    89:"cherry",
    90:"apple",
    91:"kiwi",
    92:"banana",
    93:"kiwi",
    94:"banana",
    95:"melon",
    96:"banana",
    97:"melon",
    98:"pineapple",
    99:"apple",
    100:"pineapple"
             }
    
    total = 0
    for n in str(number):
        total += int(n)
    
    newNum = number - total
    
    if newNum in fruits:
        return fruits[newNum]
    
    #return #fruit name like "apple"

    from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #receive a root node of a binary tree
        #return a list back of the right nodes only

        #initialize an empty list
        #iterate through the queue of root nodes
        #set up a right node value
        #add in left node, and right node
        #add in right node in list
        #return list

        if not root:
            return []

        result = []
        rightNodeVal = None
        queue = deque([root])
        
        while queue:
          
            for node in range(len(queue)):
                current = queue.popleft()
                rightNodeVal = current.val
                
                if (current.left):
                    queue.append(current.left)
                
                if (current.right):
                    queue.append(current.right)
            result.append(rightNodeVal)
        return result
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #receive the root node of a tree
        #return the max depth (the deepest level the farthest node is in) (an integer)

        #ex:     3
        #       / \
        #.     2.  4
        #     / \
        #  null  5

        #ex: return 3

        #edge cases :if it's empty, return 0
    
        #initialize an empty variable called levels
        #keep traversing through the nodes, add 1 to each level
        #return level

        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        print(left_depth, right_depth)

        return 1 + max(left_depth, right_depth)
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #receive two root nodes of a binary tree
        #return boolean - true if all leaf nodes are same values, else False

        #edge cases: if root1 is empty, but root 2 is not, return False 
        #if root1 is not empty, but root 2 is , return False

        #iterate through the tree
        #go deep left as possible, 
        #check if there are no child nodes, add the value into a list
        #iterate through root2, check if there are no child nodes, add the value into a list
        #check if the list values are equal to each other, return true if they are, else False

        if root1 and not root2:
            return False
        if not root1 and root2:
            return False

        result1 = []
        result2 = []

        self.collectLeafNodes(root1, result1)
        self.collectLeafNodes(root2, result2)
    
        return result1 == result2

    def collectLeafNodes(self, node: Optional[TreeNode], result: List) -> list:
        if not node:
            return []

        if not node.left and not node.right:
            result.append(node.val)
            return
        
        self.collectLeafNodes(node.left, result)
        self.collectLeafNodes(node.right, result)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #receive root node
        #return the max levels in tree

        #traverse through left and through right and add one

        #if no root nodes, return 0

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)


        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #receive the root node of a binary tree
        #return an integer of good nodes that are increasing

        #if not root, return 0

        #initialize good nodes to 0

        #iterate left and iterate right
        #check if the next node is >= currentnode.val
        #if it is, increment good nodes val
        #else, keep going
        #return goodnodes val

        goodNodes = 0

        if not root:
            return goodNodes

        left = self.goodNodes(root.left)
        right = self.goodNodes(root.right)

        if left > current.val:
            goodNodes += 1
        
        return goodNodes
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #receive the root node of a binary tree
        #return an integer of good nodes that are increasing

        #if not root, return 0

        #initialize good nodes to 0

        #iterate left and iterate right
        #check if the next node is >= currentnode.val
        #if it is, increment good nodes val
        #else, keep going
        #return goodnodes val

        def dfs(node, max_so_far):
            if not node:
                return 0
            
            good = 1 if node.val >= max_so_far else 0

            new_max = max(max_so_far, node.val)

            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)
            return good
        return dfs(root, root.val)
        
        