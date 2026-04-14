def addTree(root):
    if not root:
        return 0
    
    return root.value + addTree(root.left) + addTree(root.right)
def intersection(a, b):
  #receive a two list o fintegers
  #return a list back of items that exist in both

  #iterate through each item in the list
  #check if it's in second list
  #add to the result
  #return result

  # result = []
  # for item in a:
  #   if item in b:
  #     result.append(item) 
  # return result

  #time: O(n * m)
  #space:O(min(n,m))

  #create a unique set of a
  #iterate through b
  #check if set has it
  #return item sin a result

  result = []
  uniqueA = set(a)
  for item in b:
    if item in uniqueA:
      result.append(item)
  return result

  #time: O(n +m)

  def exclusive_items(a, b):
  #receive two list of integers
  #return a list back of integers that do not exist in other

  #ex: 

  #initialize a result
  #iterate through a
  #check if it's not in b
  #add in list

  # result = []
  # for item in a:
  #   if item not in b:
  #     result.append(item)

  # for item in b:
  #   if item not in a:
  #     result.append(item)
  # return result

  #time: O(n * m)
  #space:O(n + m)

  #create a set of both
  uniqueA = set(a)
  uniqueB = set(b)

  result = []
  for num in a:
    if num not in uniqueB:
      result.append(num)

  for num in b:
    if num not in uniqueA:
      result.append(num)
  return result


def all_unique(items):
  #create a set
  #iterate through
  #check if letters exist in the items

  uniqueA = set(items)
  if len(uniqueA) == len(items):
    return True
  else:
    return False
  
  def intersection_with_dupes(a, b):
  #receive two list of integers
  #return a list back of same duplicate amounts found

  #create a pointer in longest list
  #check if the letters are same, return in result


  #keep track of char count
  #iterate through second list
  #check if char is the same and how many amounts there are
  #add the char to the list


  charA = {}
  charB = {}

  for char in a:
    charA[char] = charA.get(char, 0) + 1

  for char in b:
    charB[char] = charB.get(char, 0) + 1

  result = []

  for char in charA:
    if char in charB:
      count = min(charA[char], charB[char])
      result.extend([char] * count)
   
  return result
      

      class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowerS = ''.join(char for char in s.lower() if char.isalnum())
        # return lowerS == lowerS[::-1]


        lowerS = ''.join(char for char in s.lower() if char.isalnum())

        left = 0
        right = len(lowerS) - 1

        while left < right:
            if lowerS[left] != lowerS[right]:
                return False
            left += 1
            right -= 1

        return True
  

  class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #receive a list of int in non-decreasing order
        #return the length of the array back where duplicates have been removed
        #ex: [1,2,3] => 3 

        #initialize a new result
        #iterate through with i and j
        #check if the value is same as last value
        #if not add it to count

        if not nums:
            return 0

        k = 1 #index pointer to help rewrite

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
      
        
class Solution:
    def reverseVowels(self, s: str) -> str:
        #receive a string of upper or lowercase
        #return the string back where vowels are reversed
        #ex: 'hello' => 'holle'

        #iterate through each char
        #check if it exists in vowel
        #add it to the stack
        #then iterate through string again
        #add in from the stack

        stack = []
        vowels='AEIOUaeiou'

        for char in s:
            if char in vowels:
                stack.append(char)
            
        result = ''

        for char in s:
            if char in vowels:
                result += stack.pop()
            else:
                result += char
        return result
    
    class Solution:
    def reverseVowels(self, s: str) -> str:
        #receive a string of upper or lowercase
        #return the string back where vowels are reversed
        #ex: 'hello' => 'holle'

        #iterate through each char
        #check if it exists in vowel
        #add it to the stack
        #then iterate through string again
        #add in from the stack

        vowels=set('AEIOUaeiou')

        left = 0
        right = len(s) -1
        s=list(s)


        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            
            if s[right] not in vowels:
                right -=1 
                continue

            s[left],s[right] = s[right], s[left]
            left += 1
            right -=1
        return ''.join(s)

       class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #receive two list of integers
        #return a list back of same element in both lists
        #ex: [2,4,5], [2,3] => [2]


        #keep count of one of the list
        #iterate through second list, check if char is in it
        #return the char


        counter = {}
        for char in nums1:
            counter[char] = counter.get(char, 0) + 1

        result = []
        for char in nums2:
            if counter.get(char, 0) > 0:
                result.append(char)
                counter[char] = 0
        return result

        # unique1 = set(nums1)
        # result = []
        # for char in nums2:
        #     if char in unique1:
        #         result.append(char)
        # return result

        class Solution:
    def validPalindrome(self, s: str) -> bool:
        #receive a lowercase string
        #return boolean if palindrome after deleting at most one char

        #ex: 'abca' 

        #iterate from left and right
        #check if they are not the same chars
        #then either go in left or right
        #and check if they are same chars
        #if not return False
        #return True after checking everything


        left = 0
        right = len(s) - 1

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1 
            return True


        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left +1, right) or isPalindrome(left, right -1)
            left += 1
            right -=1
        return True

        class Solution:
    def validPalindrome(self, s: str) -> bool:
        #receive a lowercase strings
        #return boolean
        #ex: 


        left = 0 
        right = len(s) - 1 

        def checkPalindrome(left, right):
      
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -=1
            return True

        while left < right:
            if s[left] != s[right]:
                return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)
            left += 1
            right -=1
        return True
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #receive the head of sLL
        #return true if palin, else false

        #check the node value from left to right

        result = []
        current = head

        while current is not None:
            result.append(current.val)
            current = current.next

        left = 0
        right = len(result) - 1

        while left < right:
            if result[left] != result[right]:
                return False
            left += 1
            right -=1
        return True

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #receive a list of integers
        #return top k elements of frequent elements
        #ex: 

        #create a counter and keep track count of values
        #iterate through counter object
        #return max k elements

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        result = []
        while len(result) <k:
            val, key = heapq.heappop(heap)
            result.append(key)
        return result
        
        def sum_numbers_recursive(numbers):
  #receive a list of integers
  #return sum of all numbers in list
  #ex: [2,3,4,5] => 13

  #base case:
  #if num is 0, return 0
  #else iterate through the rest of num + first num


  if len(numbers) == 0:
    return 0

  return numbers[0] + sum_numbers_recursive(numbers[1:])

#time:O(n^2)
#space:O(n^2)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #receive the head of a linked list
        #return the linked list back reversed

        #ex: 1 -> 2 -> 3 -> 4

        #ex: 4 -> 3 -> 2 -> 1
            #             prev    current

        #keep track of the head
        #initialize an extra pointer
        #iterate through the entire linked list until it hits null
        #reverse the pointers and make it point the previous
        #then we return the current

        prev = None
        current = head

        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev
            

            def binary_search(numbers, target):
  #receive a list of sorted integers
  #return the index of target
  #ex: [0,1,2,3] => 3 => idx = 4

  left= 0
  right = len(numbers) - 1

  while left <= right:
    middle = (left + right) // 2
    
    if target < numbers[middle]:
      right = middle - 1
    elif target > numbers[middle]:
      left = middle + 1
    else:
      return middle
  return -1

def binary_search_index(nums, target):
  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = (low + high) // 2
    
    if target < nums[mid]:
      high = mid - 1
    elif target > nums[mid]:
      low = mid + 1
    else:
      return mid
  return low


def square_root(n):
  # for num in range(0, n + 1):
  #   low = 0
  #   high = n
  low = 0
  high = n

  while low <= high:
    mid = (low + high) // 2
    if n < mid * mid:
      high = mid - 1
    elif n > mid * mid:
      low = mid + 1
    else:
      return mid
  return high

      
      def binary_search_index(nums, target):
  low = 0
  high = len(nums) -1 

  while low <= high:
    mid = (low + high) // 2

    if target < nums[mid]:
      high = mid - 1
    elif target > nums[mid]:
      low = mid + 1
    else:
      return mid
  return low
      