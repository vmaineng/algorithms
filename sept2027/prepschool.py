#splits a string into strings of two chars into array
#if string contains odd, missing second char will have an underscore it

#parameter:can be lowercase or uppercase characters, no spaces
#return: a list of two chars, but if it's odd, then the second char will have underscore
#ex: 'hello' => ['he', 'll', 'o_']
#ex: 'star' => ['st', 'ar']
#ex: ''=> []

#at least one character

#iterate word
#calc even or odd for the string,
#concat '_' at the end of the last digit if odd
#create an empty string; slice up to two characters at the same time
#add in two characters at a time
#push in the pair in the final result

# if len(word) % 2 == 0
#'a'

def splitPairs(word): 
    result = []

    if len(word) % 2 != 0:
        word = word + '_'

    for idx in range(0, len(word), 2): #hello_
        pair = word[idx: idx+2] #'he', 'll', 'o_'
        result.append(pair) #['he', 'll', 'o_']

    return result

# print(splitPairs('hello'))
# print(splitPairs('star'))
        
#check to see if string has same amount of x's and o's
#return boolean
#

def checkXO(word):
    word = word.lower()
    return word.count('x') == word.count('o')

print(checkXO('xoo1bco'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def valid(self, node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        
        return self.valid(node.val, left, right) and self.valid(left, node.val, right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #receive the root node of a tree
        #return boolean

        return self.valid(root, float("-inf"), float("inf"))

        class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #receive a rotated list
        #return the position of the target we are looking at
        #ex: 

        #using two left pointers 
        #find middle
        #check if middle <= target <= right, then go right


        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            if nums[left] <= nums[middle]: 
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #receive a list of pivoted points
        #return the idx of the target value
        #ex: 

        #find middle
        #check if the left val < = middle
        #then check if target wouild fall in between
        #else check right
        #check if val would fall in between
        #else return - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            
            if nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return - 1

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes)-1

        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next= None

        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #receive the head of linked list
        #return the linkedlist where nth node is removed
        #ex: 1 -> 2 -> 3, 1 => return head.next

        if not head:
            return None


        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
            
        if count == n:
            return head.next

        curr = head
        for node in range(count - n - 1):
            curr = curr.next
        curr.next = curr.next.next
            
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #receive a list of linked list
        #return a linked list where nodes are added from outside in
        #ex: 

        #add nodes to a list
        #start from left to right
        #add them in together
        #and return the head


        if not head:
            return []

        res = []
        cur = head
        while cur:
            res.append(cur)
            cur = cur.next

        i = 0
        j = len(res) - 1

        while i < j:
            res[i].next = res[j]
            i += 1
            if i > j:
                break
            res[j].next = res[i]
            j -= 1
        res[i].next = None        

        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #receive the head of a linked lsit
        #return the list where n node is removed
        #ex: 

        if not head:
            return None

        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        if count == n:
            return head.next
        
        curr = head
        for i in range(count - n - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head

        class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #receive an integerval
        #return intervals that overlap each other
        #ex: 

        #sort the intervals
        #add the first interval into result
        #check start, end of second interval compared to first


        intervals.sort(key=lambda x:x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i] #[1,5]
            prev_start, prev_end = intervals[i - 1] #[1,3]

            if cur_start <= prev_end: #3 <= 1
            
                result[-1][-1] = max(prev_end, cur_end)
            else:
                result.append(intervals[i])
        return result

    class Solution:

    def checkPalindrome(self, s, left, right):

        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True
            


    def validPalindrome(self, s: str) -> bool:
        #receive a string
        #return boolean
        #ex: 

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.checkPalindrome(s, left + 1, right) or self.checkPalindrome(s, left, right - 1)
            
            left += 1
            right -=1
        return True

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        #receive the root tree
        #return boolean if targetsum can be found
        #ex:

        if not root and targetSum == 0:
            return True
        
        if not root and targetSum > 0:
            return False

        
        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)

        leftSum = root.val + left
        rightSum = root.val + right

        return leftSum == targetSum or rightSum == targetSum
            
       


        