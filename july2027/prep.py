def charAccum(str):
    #receive a string of chars
    #return the chars
    #ex: 
    result = []
    for idx, char in enumerate(str):
        
        result.append(char * (idx + 1))
        
    return '-'.join(result)

# print(charAccum('abc'))


def weighsMore(str1,str2):
    #take the first num // second num
    #see which one out weighs the other
    #ex: ('1:3','1:2')

    totalOne = int(str1[0]) // int(str1[2])
    totalTwo = int(str2[0]) // int(str2[2])

    return True if totalOne > totalTwo else False
print(weighsMore('1:3','1:2'))

class Dog ():
  def __init__(self, breed):
    self.breed = breed
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
scoobydoo.bark = lambda: "Woof"

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #receive a large unsorted nums array
        #return the kth largest element
        #ex: [3,2,5,1] => 2 
        # [1,2,3,5] => 2 # time: O(n log n); #space: O(n)

        #initialize a max heap
        #iterate through the integers
        #add all of the integers until it reaches the length of k
        #then we are oging to opop it off until we hit k times

        heap = [ ]

        for num in nums:
            heapq.heappush(heap, num) 
            if len(heap) >k:
                heapq.heappop(heap)

        
        return heap[0] #O(logK) #space:O(K)

    class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums *2

    class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #receive an integer of nums
        #return True if value > 1, else False
        #ex: [1,3,5] => False
        #ex: [1, 3,1] => True b/c 1 is duplicate

        #iterate through the array
        #iterate again through the array at second number
        #this will be O(n ^2)

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
             
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        #use a set
        #iterate through
        #check if num exists in set, if not add, in, if it does, return False

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #receive two strings and check if anagrams of each
        #anagram = same amount of letters as each other
        #ex: 'helllo', 'joje => False
        #ex: 'hi', 'ih' => True

        #if not the same length, can return False

        #sort them
        #check ift he sorted versions == other

        if len(s) != len(t):
            return False

        # return sorted(s)== sorted(t)

        #time: O(2nlogn) => O(logn)
        #space: O(2n) => O(n)

        #keep track of chars from one of the words
        #then iterate through the second word
        #if the object is empty, we used all words => return True else return False

        seen = { }

        for char in s:
            seen[char] = seen.get(char, 0) + 1

        for char in t:
            if char in seen:
                seen[char] -= 1
            else:
                return False
        
        return all(count == 0 for count in seen.values())

    class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #receive a list of lowercase chars
        #return the list back in reverse
        #ex: ['h','e'] => ['e','h'] 

        #could use the reverse function
        # return s.reverse()

        #to do it in place - use two pointers
        #starting from left and right
        #keep going until it hits middle and swap them

        left = 0
        right = len(s) - 1

        while left < right:
            s[left],s[right] = s[right], s[left]
            left += 1
            right -=1 
        return s

    class Solution:
    def isPalindrome(self, s: str) -> bool:
        #receive a string of upper and lowercase letters and punctation marks
        #return boolean if it is written backward same as backward
        #ex: could reverse and check if lowercase version is the same
        #omit anything that is not chars

        fixedString = s.lower()
        
        result = []
        for char in fixedString:
            if char.isalnum():
                result.append(char)
        updatedStr = ''.join(result)
        
        # return updatedStr == updatedStr[::-1]

        #time:O(n); space:O(n)

        print(updatedStr)

        left = 0
        right = len(updatedStr) - 1

        while left < right:
            if updatedStr[left] == updatedStr[right]:
                right -=1 
                left += 1
            else:
                return False
        return True


        class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        left = 0

        for right in range(len(nums)):
            if right - left > k:
                seen.remove(nums[left])
                left += 1
            if nums[right] in seen:
                return True
            seen.add(nums[right])
        return False

    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #receive a list of profits
        #return the maxprofit found
        #ex: [1,2,5] => buy at 1, sell at 5, => profit of 4
        
        #iterate through each num
        #buy and sell next day
        #keep track of maxprofit found
        #return maxprofit

        # maxprofit = 0

        # for buy in range(len(prices)):
        #     for sell in range(buy+1, len(prices)):
            
        #         profit = prices[sell] - prices[buy]
        #         maxprofit = max(maxprofit, profit)

        # return maxprofit

        #time:O(n^2) ; space: O(1)

        maxprofit = 0
        buy = 0

        for sell in range(1, len(prices)):
            profit = prices[sell] - prices[buy]
            maxprofit = max(maxprofit, profit)
            if prices[sell] < prices[buy]:
                buy = sell
        return maxprofit

    class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #receive a list of integers
        #return the idx position of the target using binary search


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid -1
        return -1

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #receive two linked lists
        #return the linked lists in order by values
        #ex: 

        #start with a dummy node
        #check which value is smaller from list1 and lsit 2
        #then add it in
        #if we finished one list more than the other, then add in the rest of the list afterwards

        dummy = ListNode()
        head1 = list1
        head2 = list2
        current = dummy
        
        while head1 and head2:
            if head1.val < head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            
            current = current.next

        if head1:
            current.next = head1

        if head2:
            current.next = head2
        return dummy.next

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(node):
            if not node:
                return
            
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return result