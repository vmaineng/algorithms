class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0)}
        x=y= 0
        for way in path:
            if way == 'N':
                y += 1
                
            elif way == 'E':
                x += 1
                
            elif way == 'S':
                y-= 1
                
            else:
                x-=1
               

            if (x,y) in visited:
                return True
            visited.add((x,y))
            
        return False
        
        def vowel_indices(word):
	#receive a string of letters
    #return vowels index in a list
    
    #ex: 
    
    result = []
    vowels = 'aeiouy'
    
    for i, char in enumerate(word.lower()):
        if char in vowels:
            result.append(i + 1)
    return result

def in_array(array1, array2):
    #receive a list of two lists of lowercase letters
    #return a list back that are substrings of the string in 2
    #ex: 
    
    #iterate through the list of strings
    #check if in a1 exists in a2
    #add to the result list
    #return result list sorted
    
    result = set()
    for word in array1:
        curr = word
        for word2 in array2:
            if curr in word2:
                result.add(curr)
                break
    return sorted(result)

def dir_reduc(arr):
    #receive a list of directions
    #return a list of directions back that is simplified
    #ex: 
    
    #iterate through the words
    #check the word right next to it to see if it's adjacanet kind
    #if not, add to result list
    
    pairs = {
        'NORTH': 'SOUTH',
        'EAST': 'WEST',
        'SOUTH': 'NORTH',
        'WEST': 'EAST'
    }
    
    stack = []
    for direct in arr:
        if stack and direct == pairs[stack[-1]]:
            stack.pop()
        else:
            stack.append(direct)
                     
    return stack

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #receive a list of integers
        #return the values that equal up to target of 0
        #ex: 
        #iterate through the 3sums
        #check if all of them equal 0 
        #return the values in a list

        nums.sort()

        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: 
                    r -=1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #receive a list of integers
        #return min value found in O(log n) time
        #ex: [3,4,5,1,2] => 
        #     l   m    r
        #iterate through using binary search
        #keep track of the value seen in mid
        #is it smaller than mid
        #if so, udpate mid
        #then check to the left of it if l < r
        #then move l if r is smaller
        #else move r
        #find the mid

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
        
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #receive a binary tree
        #return the amount of nodes 
        #ex: 

        #if node from root to the tree < max val
        #increment count

        
        max_val = float("-inf")

        if not root:
            return 0

        def dfs(node, max_val):
            if not node:
                return 0
            count = 0

            if node.val >= max_val:
                count += 1
            max_val = max(max_val, node.val)
    
            left_node = dfs(node.left, max_val)
            right_node = dfs(node.right, max_val)

            return count + left_node + right_node
        return dfs(root, float("-inf"))

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0 
            
            res = 1 if node.val >= max_val else 0 
            max_val = max(max_val, node.val)
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            return res
        return dfs(root, root.val)
        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #receive a list of integers
        #return the num that's repeated twice
        #ex: 

        #could do O(n^2)

        #use an object to track what's number been seen

        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return num
            
        