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


    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #receive head of a linked list
        #return the n'th node removed
        #ex: 

        #keep track of count
        #if count == head
        #return after head.next
        
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

        for i in range(count - n - 1):
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
        #receive the head of ll 
        #return a new ll where linked list is alternated for each one

        #ex:

        #add nodes into a list
        #two pointers

        if not head:
            return None

        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i = 0
        j = len(nodes) - 1

        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i > j:
                break
            
            nodes[j].next = nodes[i]
            j -=1
        nodes[i].next = None

        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #do two pointers
        #go fast and slow
        #find middle, reverse middle
        #then keep pointer on the new list
        #and add it back in

        if not head:
            return None
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        second = slow.next
        slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        slow = head
        curr = prev

        while curr:
            tmp1, tmp2 = slow.next, curr.next
            slow.next = curr
            curr.next = tmp1
            slow, curr = tmp1, tmp2

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #receive a list of intervals
        #return the list merged
        #ex: 

        #sort
        #check prevend <= current start
        #if so update the end
        #else merge in the intervals

        intervals.sort(key=lambda x:x[0])

        results = [intervals[0]]

        for i in range(1, len(intervals)):
            if results[-1][-1] >= intervals[i][0]:
                results[-1][1] = max(results[-1][-1],intervals[i][1] )
            else:
                results.append(intervals[i])
        return results

            # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        #receive the root node of a tree
        #return tboolean
        #ex: 

        #base case: if we know you are a leaf, return targetsum val - root.node.val
        #else: traverse through left and and traverse right right

        if not root:
            return False

        if not root.left and not root.right:
            return targetSum - root.val == 0
        
        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
       

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #receive a string 
        #return an int of longest substring count
        #ex: 

        #iterate through the list with two pointers
        #keep track of characters seen in hash map
        #if characters in set
        #return longest length seen

        unique = set()
        longest = 0

        left = 0
        right = 0

        while right < len(s):
            if s[right] not in unique:
                unique.add(s[right])
                longest = max(longest, right-left + 1)
                right += 1
            else:
                unique.remove(s[left])
                left +=1
        
        return longest

        def square_root(n):
  #receive an integer
  #return the integer that is the square root of it
  #ex: 2 -> 2
  #use left and right of b1 up to n 
  #check if the number * number is equal to n
  #return the n 

  if n < 2:
  return n


  left = 1
  right = n // 2

  while left <= right:
    mid = (left + right) // 2

    if mid * mid == n:
      return mid
    elif mid * mid <= n:
      left = mid + 1
    else:
      right =mid - 1
  

def find(arr, ele):
    return arr.index(ele) if ele in arr else 'Not found'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        #receive the root node of a tree
        #return boolean - true if we can go from root to leaf and the total == targetSum, else False
        #ex:       3
        #         /. \
        #      3     5
        # 8 => True
        # 10 => False
        #

        #base case - if not the root is empty and targetsum != 0, return false
        #recursive case - keep calling the current node , subtract from targetSum 
        #return a boolean if we meet targetSum

        if not root:
            return False

        if not root.left and not root.right:
            return targetSum - root.val == 0

        targetSum -= root.val

        return (
        self.hasPathSum(root.left, targetSum) or
         self.hasPathSum(root.right, targetSum)
         )

        def min_in_rotated_sorted_array(nums):
  #receive a list of int 
  #return the min element found
  #ex: [5,6,7, 8,2,3,4] => 2
  #     l      m     r
  #           l   m r
  

  #find mid, 
  #check if left <= mid == sorted
  # or else check if mid < = right ; if not smallest exist over here

  left = 0
  right = len(nums) - 1

  while left < right:
    mid = (left + right) // 2
    if nums[mid] < nums[right]:
      right = mid
    else:
      left = mid + 1
  return nums[left]
    
      def find_in_rotated_sorted_array(nums, target):
  left = 0
  right = len(nums) - 1

  while left <= right: 
    mid = (left + right) // 2

    if nums[mid] == target:
      return mid
      
    if nums[left] <= nums[mid]:
      if nums[left] <= target <= nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    elif nums[mid] < nums[right]:
      if nums[mid] <= target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1

  return -1

    def max_subarray_sum_size_k(nums, k):
  #receive a list and an int
  #return max sum found in window of 3

  #ex: 

  #keep track of current sum
  #iterate through the list of integers up to 3 max_subarray_sum_size_k
  #return max sum found

  # max_sum = float('-inf')

  # for i in range(len(nums)):
  #   current = sum(nums[i: i+k])
  #   max_sum = max(max_sum, current)
  # return max_sum

  current = sum(nums[0:k])
  max_sum = current

  for i in range(len(nums) - k ):
    current -= nums[i]
    current += nums[i + k]
    max_sum = max(max_sum, current)
  return max_sum

def subarray_target_sum_size_k(nums, target, k):
  #receive a list of integers
  #return how many subarrays make the target
  #ex: 

  #keep a count
  #check if the current subarray == target, increase count

  
  current_sum = sum(nums[0:k])
  count = 1 if current_sum == target else 0
  
  for i in range(len(nums) - k):

    current_sum -= nums[i]
    current_sum += nums[i + k]
    if current_sum == target:
      count += 1
  return count

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #receive an integer
        #return the missing num
        #ex: [0,1,2, 4] => 3 

        #is array sorted? 
        #iterate from 0 to n 
        #check if n - 1 is there
        #if not return the missing num
        

        for i in range(0, len(nums)-1):
            if nums[i] != 0:
                if nums[i] != nums[i] -1 :
                    return nums[i] - 1
            else:
                if nums[i] != nums[i] + 1 :
                    return nums[i] + 1

        class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #receive an integer
        #return the missing num
        #ex: [0,1,2, 4] => 3 

        #is array sorted? 
        #iterate from 0 to n 
        #check if n - 1 is there
        #if not return the missing num

        res = len(nums)
        
        for i in range(len(nums)):
            res += i - nums[i]
        return res

        class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #receive a list of integers
        #return the two index that equals up to the target (but it's 1 index)
        #ex: 

        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+ 1]


        sums = { }

        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in sums:
                return [sums[difference], i + 1]
            sums[numbers[i]] = i + 1
        
        #{2: 0, 3: 1}
        #
def has_substring_anagram(s, anagram):
  #receive a string of lowercase chars
  #return if it has anagram in s

  #ex: 

  #create a set of the s and anagram
  #check if anagram letters are in s when reach the end


  anagram_set = set(anagram)
  window = set(s[0: len(anagram)])

  if anagram_set == window:
    return True

  for i in range(0, len(s)-len(anagram)):
    window.remove(s[i])
    window.add(s[i+len(anagram)])

    if anagram_set == window:
      return True
    
  return False
      
      
from collections import Counter

def count_substring_anagrams(s, anagram):
  #receive a len of count_substring_anagrams
  #return the occurence of how many times it shows up
  #ex: 

  anagram_count = Counter(anagram)
  window = Counter(s[0:len(anagram)])
  count = 0

  if anagram_count == window:
    count += 1

  for i in range(0, len(s) - len(anagram)):
    window[s[i]] -= 1
    window[s[i+len(anagram)]] += 1

    if anagram_count == window:
      count += 1

  return countv

def find_subarray_sum(nums, target_sum):
  #receive a list of integers
  #return the start and end index 

  #ex: 

  #create a left and right
  #right moves to the end
  #if the current target > target, move left to right
  #else keep moving right to find_subarray_sum

  #([3, 1, 4, 9, 2, 1, 7], 10) 
   #             l
  #             r 
  # total: 2

  #([1, 2, 3, 7, 5], 12)
  #     l
  #              r
  #tota=13
  left = 0
  right = 0
  current_sum = 0
  
  while right < len(nums):
    current_sum += nums[right]
      
    while current_sum > target_sum:
      current_sum -= nums[left]
      left += 1
      
    if current_sum == target_sum:
      return (left, right)
    right += 1
    
      
      
      
                


  
        
        