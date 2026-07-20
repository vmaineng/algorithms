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
      
      def square_root(n):
  low = 0
  high = n

  while low<= high:
    mid = (low + high) // 2
    squared = mid * mid

    if squared > n:
      high = mid - 1
    elif squared < n:
      low = mid + 1
    else:
      return mid

  return high
      
      def find_leftmost_index(nums, target):
  low = 0
  high = len(nums) - 1
  leftmost = -1

  while low <= high:
    mid = (low + high) // 2

    if target < nums[mid]:
      high = mid - 1
    elif target > nums[mid]:
      low = mid + 1
    else:
      high = mid - 1
      leftmost = mid
  return leftmost

  def min_in_rotated_sorted_array(nums):
  low = 0
  high = len(nums) - 1

  while low < high:
    mid = (low + high) // 2

    if nums[mid] < nums[high]:
      high = mid
    else:
      low = mid + 1
  return nums[low]

  def elevator(left, right, call):
    #receive integers (whole)
    #return which elever is closest to the call, return a string
    #ex: (0, 1, 0) => "left"
    
    #ex: (2, 1, 1) => 'right'
    #ex: (2, 0, 1) => "right"
    
    #figure out the distance between left - call
    #right - call
    #see which one is the smaller difference, return that specific elevator
    #else return "right"
    
    left_distance = abs(call - left) #0 - 1 = -1
    right_distance = abs(call - right) #0 - 2= -2
    print(left_distance, right_distance)
    
    if left_distance == right_distance:
        return "right"
    
    if right_distance == 0:
        return "right"
    if left_distance == 0:
        return "left"
    
    return "left" if left_distance < right_distance else "right"
        

    
    
#     if right_distance == 0:
#         return "right"
#     elif left_distance == 0:
#         return "left"
#     elif left_distance < right_distance:
#         return "left"
#     elif right_distance < left_distance:
#         return "right"

    
    
    def find_min_index(nums, target):
  low = 0
  high = len(nums) -1 
  leftIdx = -1

  while low <= high:
    mid = (low + high) // 2

    if target < nums[mid]:
      high = mid - 1
    elif target > nums[mid]:
      low = mid + 1
    else:
      high = mid -1
      leftIdx = mid
  return leftIdx

def find_right_index(nums, target):
  low = 0
  high = len(nums) -1 
  rightIdx = -1

  while low <= high:
    mid = (low + high) // 2

    if target < nums[mid]:
      high = mid - 1
    elif target > nums[mid]:
      low = mid + 1
    else:
      low = mid + 1
      rightIdx = mid
  return rightIdx


def count_in_sorted_array(nums, target):
  leftIdx = find_min_index(nums, target)
  rightIdx = find_right_index(nums, target)
  
  if rightIdx == -1:
    return 0
  else:
    return rightIdx - leftIdx + 1
  

  def find_row(grid, target):
  low = 0
  high = len(grid) - 1

  while low <= high:
    mid = (low + high) // 2
    if grid[mid][0] <= target <= grid[mid][-1]:
      return mid
    elif target < grid[mid][0]:
      high = mid - 1
    else:
      low = mid + 1
  return -1

  
def binary_search(grid, target,row):
  low = 0
  high = len(grid[0]) - 1

  while low <= high:
    mid = (low + high) // 2

    if target < grid[row][mid]:
      high = mid - 1
    elif target > grid[row][mid]:
      low = mid + 1
    else:
      return True
  return False

def search_sorted_grid(grid, target):
  row = find_row(grid, target)

  if row == -1:
    return False
  else:
    return binary_search(grid, target,row)


def find_peak(nums):
  #receive a list of integers
  #return the idx of peak where neighbor is higher
  #ex: [2,3,5,4,1] => 2
  #    l    m    h
  #    l m  h
  #      l  h

  #iterate from left and right
  #check the middle
  #check if it's less than thevalue next to it
  #then search left
  #else search right

  low = 0
  high = len(nums) - 1

  while low < high:
    mid = (low + high) // 2

    if nums[mid] < nums[mid + 1]:
      low = mid + 1
    else:
      high = mid
  return low

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def undupe_sorted_linked_list(head):
  #receive the head of a ll
  #return a new linked list of singles
  #ex: 3-> 3 -> 4 => 3-> 4

  #iterate through ll
  #check if it's not the same val, link
  #else move on to the next one 

  dummy = Node(None)
  tail = dummy
  current = head

  while current:
    if current.val != tail.val:
      tail.next = Node(current.val)
      tail = tail.next
    current = current.next
  return dummy.next

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  #receive a list of values
  #return a linked list
  #ex: 

  dummy = Node(None)
  tail = dummy

  for item in values:
    tail.next = Node(item)
    tail = tail.next
  return dummy.next

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  dummy = Node(None)
  tail = dummy

  for item in values:
    tail.next = Node(item)
    tail = tail.next
  return dummy.next


def max_value(nums):
  #receive a list of integers
  #return biggest number seen
  #ex: [3, 5, -1, 7] => 7

  #keep track of biggest number
  #check if current num is bigger than the biggest num
  #update it if it is

  biggest_num = nums[0]

  for num in nums:
    if num > biggest_num:
      biggest_num = num
  return biggest_num

def get_ascii(ch : str) -> int:
    #receive a string
    #return an integer
    #ex: a => 26
    
    return ord(ch)
  
  import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    #receive integers
    #return the age
    #ex: 
    
    array = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    total = sum(num * num for num in array)
    squared = math.sqrt(total)
    return squared // 2
    

    def delete_nth(order,max_e):
    #receive a list of integers
    #return a list of numbers up to max_e
    #ex: [1,2,3,1,3,3], 2 => [1,2,3,1,3]
    
    #iterate through each num and keep count
    #then iterate through the num again
    #check if num > 0, reduce from object
    #return list back
    
    result = []
    track = {}
    
    for num in order:
        track[num] = track.get(num, 0) + 1
    
        if track[num] <= max_e:
            result.append(num)
        
    return result

def max_subarray_sum_size_k(nums, k):
  #receive a list of integers
  #return the max subsize of k 
  #ex: [4,2,1,5,3], 2 => [5,3]  => 8

  #iterate through the array and go through with a fixed size window

  # max_total = float("-inf")

  # for i in range(0, len(nums)  -k + 1):
  #   current_sum = sum(nums[i: i + k])
  #   if current_sum > max_total:
  #     max_total = current_sum

  # return max_total

  
  current_sum = sum(nums[:k])
  max_total = current_sum
  for i in range(0, len(nums) - k ):
    current_sum -= nums[i]
    current_sum += nums[i + k]
    if current_sum > max_total:
      max_total = current_sum
  return max_total
    
def greet(name): 
    #receive a string of characters
    #return "Hello {name}"
    #ex: 'rob' => 'Hello Rob!'
    
    #modify the name to be uppercase for first and follow by rest of name
#     return f"Hello {name[0].upper + name[:1]}"
    new_name = name[0].upper() + name[1:].lower()
    return f"Hello {new_name}!"

    import math
def max_subarray_product_size_k(nums, k):
  #receive a list of integers
  #return the max product found
  #ex: 

  #iterate through the list
  #multiply it into the product
  #divide it out of th eproduct
  #return max product seen

  # max_product = float('-inf')
  # current_product = 1
  # for i in range(0, len(nums) - k + 1):
  #   current_product = math.prod(nums[i: i + k])
  #   if current_product > max_product:
  #     max_product = current_product
  # return max_product

  current_product = math.prod(nums[0: k])
  max_product = current_product
  for i in range(0, len(nums) - k):
    current_product /= nums[i]
    current_product *= nums[i + k]
    if current_product > max_product:
      max_product = current_product
  return max_product
  
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #receive a list of integers
        #return max length of 1's next to each other
        #ex: [1,1,1,1,1] => 5
        #ex: [0] => 0

        #initialize a count
        #increment count if 1 is next to else, reset to 0
        #update max count seen

        max_count = 0
        current_count = 0

        for num in nums:
            if num == 1:
                current_count += 1
            else:
                current_count = 0
            if current_count > max_count:
                    max_count = current_count
        return max_count
            
        
        def exclusive_items(a, b):
  #receive two list of integers
  #return a list back of items 
  #ex: [4,2,1], [2, 3, 6] => [4, 1, 3, 6]


  #initialize an empty list
  #iterate through the first array
  #check if the element exists in the second list, if not add it in

  # difference = []
  # for item in a:
  #   if item not in b:
  #     difference.append(item)

  # for item in b:
  #   if item not in a:
  #     difference.append(item)
  # return difference
  #time: O(n*m)
  #space:O(n +m)

  #use a set
  #iterate through the items
  #if not in set
  #then you know that it's unique

  unique_a = set(a)
  unique_b = set(b)
  result = []

  for num in a:
    if num not in unique_b:
      result.append(num)

  for num in b: 
    if num not in unique_a:
      result.append(num)
  return result

def who_is_paying(name):
    #receive a string for first name
    #return a list with the first name in one, and a truncated version next to it of two letters
    #ex: 'Javier' => ['Javier', 'Ja']
    #ex: "Mc" => ['Mc', 'Mc']
    
    if len(name) < 3:
        return [name]
    
    modified_name = name[:2]
    
    return [name, modified_name ]

    import math

def max_subarray_product_size_k(nums, k):
  #receive a list of integers and an inte
  #return max product seen 


  #ex: 

  #iterate through nums, and check each product 
  #update max product seen

  # max_product = 0
  # for i in range(0, len(nums) - k + 1):
  #   current_product = math.prod(nums[i: i + k])
  #   if current_product > max_product:
  #     max_product = current_product
  # return max_product


  current_product = math.prod(nums[:k])
  max_product = current_product
  for i in range(0, len(nums) - k):
    current_product /= nums[i]
    current_product *= nums[i + k]
    if current_product > max_product:
      max_product = current_product
  return max_product

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  #receive the head of a linked list 
  #return the list in reversed order
  #xex: 1-> 2 -> null; 2-> 1 -> null

  #iterate through head
  #initialize an empty Node
  #point to the previous node behind me until we hit null

  prev = None
  current = head

  while current != None:
    next = current.next
    current.next = prev
    prev = current
    current = next

  return prev

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head, prev = None):
  if head is None:
    return prev

  next = head.next
  head.next = prev

  return reverse_list(next, head)



import math

def calculate_tip(amount, rating):
    #receive an amount and a rating
    #return the amount of tip needs to be paid
    #ex: (30, "excellent") => 30 * .20 => 6
    
    
    #checking what rating is, take amount multiply by tip
    
    tip = 0
    
    if rating.lower() == "excellent": 
        return math.ceil(amount * .2)
    elif rating.lower() == 'great':
        return math.ceil(amount * .15)
    elif rating.lower() == 'good':
        return math.ceil(amount * .1)
    elif rating.lower() == 'poor':
        return math.ceil(amount * .05)
    elif rating.lower() == 'terrible':
        return 0
    else:
        return "Rating not recognised"

def find_missing_letter(chars):
    #receive a list of uppercase or lowercase letters
    #return the missing letter betwen them
    #ex: ''
    
    for idx in range(0, len(chars)):
        if ord(chars[idx + 1])  - ord(chars[idx]) > 1:
          
            return chr(ord(chars[idx]) + 1) 

def leo(oscar):
    #receive an integer
    #return a specific statement with it
    #ex: 86 => 
    
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar > 88:
        return "Leo got one already!"
    else:
        return "When will you give Leo an Oscar?"
    
    def block_player(a, b):
    #receive integers as positions
    #return which number toplace to block them
    #ex: 
    
    #[0,1,2],
    #[3,4,5],
    #[6,7,8]
    
    winning_lines = [
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8}, # Rows
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, # Columns
        {0, 4, 8}, {2, 4, 6}             # Diagonals
    ]
    
    for line in winning_lines:
        if a in line and b in line:
            return (line - {a,b}).pop()


            def solution(digits):
    max_seen = float('-inf')
    strDigits = str(digits)
    
    for i in range(len(strDigits) - 4):
        total = strDigits[i:i + 5]
        
        if int(total) > max_seen:
            max_seen = int(total)
    return max_seen

def flick_switch(lst):
    #receive a list of strings
    #return true, until flick, then return the opposite
    #ex: ['flick', 'oop','hello'] => [false, false, false]
    
    #iterate through the list of words
    #check if it is flick, flip the words
    #return the list back
    
    result = []
    flip = True
    for item in lst:
        if item == 'flick':
            flip = not flip
        result.append(flip)
        
    return result 

import heapq

def k_smallest(nums, k):
  #receive a list of integers
  #return the k-smallest size asked
  #ex: [3,5,5,6,2] => 2 => [2,3]


  #sort smallest to biggest
  #return me the first k

  # sortedNums = sorted(nums)
  # return sortedNums[:k]
  #time: O(n log n)
  #space: O(n)

  #add in a min heap

  heap = []
  result = []

  for num in nums:
    item = (-num, num)
    heapq.heappush(heap, item)
    if len(heap) > k:
      heapq.heappop(heap)

  while len(heap) > 0:
    item=heapq.heappop(heap)
    result.append(item[1])
  return result[::-1]

  
  
  def cookie(x):
    #receive an input of different types
    #return a statement based on what the input type is
    #ex: 3 => "Monica"
    
    
    #check the type
    #return the name based on it

    if isinstance(x, bool):
        return "Who ate the last cookie? It was the dog!"
    elif isinstance(x, (int, float)):
        return "Who ate the last cookie? It was Monica!"
    elif isinstance(x, str):
    
        return "Who ate the last cookie? It was Zach!"
    else:
        return "Who ate the last cookie? It was the dog!"
    
    def find_missing_letter(chars):
    #receive a list of letters
    #return the missing letters
    #ex: 
    
    #iterate through
    #check if the second letter is not more than 1
    #if it is, return the missing letter there
    
    for idx in range(0, len(chars)):
        if ord(chars[idx + 1]) - ord(chars[idx]) > 1:
            print(ord(chars[idx + 1]), ord(chars[idx]))
            return chr(ord(chars[idx]) + 1)

def has_path(graph, src, dst):
  if src == dst:
    return True
  
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst) == True:
      return True
  return False

def undirected_path(edges, node_A, node_B):
  #receive an edge list, and two nodes
  #return boolean

  #build out a grpah first
  #check the logic

  graph = build_graph(edges)
  return valid(graph, node_A, node_B, set())

def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a]= []
    if b not in graph:
      graph[b] = []
  
    graph[a].append(b)
    graph[b].append(a)

  return graph

def valid(graph, src, dst, visited):

  if src == dst:
    return True
    
  if src in visited:
    return False

  visited.add(src)

  for neighbor in graph[src]:
    if valid(graph, neighbor, dst, visited) == True:
      return True
  return False

def next_id(arr):
    #receive a list of itnegers
    #return the smallest number unused from 0 - the biggest number
    
    #ex: [3,2,5] => 0 
    #[2,3,5]
    #if 0, else reutrn 0
    
    #sort nums
    #iterate through the list of nums from 0 to the biggest
    #return num missing
    
    sortNums = sorted(set(arr))
    count = 0
    
    for i in range(0, len(sortNums)):
        if sortNums[i] != count:
            return count
        else:
            count += 1
    return count

def next_id(arr):t = 0
while t in arr:
  t += 1
return t

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #receive two list of integers
        #return one list back with same amount of integers

        #ex: 

        #keep count

        # result = []
        # for num in nums1:
        #     if num in nums2:
        #         result.append(num)
        # return result

        #time:O(n^2)
        #space: O(n)

        seen = {}

        for num in nums1:
            seen[num] = seen.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if seen.get(num,0) > 0:
                result.append(num)
                seen[num] -= 1
        return result



        class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #receive two list of integers
        #return one list back with same amount of integers

        #ex: 

        #keep count

        # result = []
        # for num in nums1:
        #     if num in nums2:
        #         result.append(num)
        # return result

        #time:O(n^2)
        #space: O(n)

        seen = {}

        for num in nums1:
            seen[num] = seen.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if seen.get(num,0) > 0:
                result.append(num)
                seen[num] -= 1
        return result
    
    from collections import deque

def shortest_path(edges, node_A, node_B):
  #receive an undirected graph, two nodes
  #return shortest path between them

  graph = build_graph(edges)
  visited = set([node_A])
  queue = deque([(node_A, 0)])
  count = 0
  
  while queue:
    current, dist = queue.popleft()
    if current == node_B:
      return dist

    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, dist + 1))
  return -1

def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph

def island_count(grid):
  #receive a m x n grid
  #return count of islands on grid
  #ex: 

  #iterate through row and columns
  #check if it is a L
  #mark as seen
  #return mark

  size = 0
  visited = set()

  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if explore(grid, row, col, visited) == True:
        size += 1
  return size

def explore(grid, row, col, visited):
  row_inbounds = 0 <= row < len(grid)
  col_inbounds = 0 <= col < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return False

  if grid[row][col] == "W":
    return False
  
  if (row, col) in visited:
    return False

  visited.add((row,col))

  explore(grid, row + 1, col, visited)
  explore(grid, row-1, col, visited)
  explore(grid, row, col + 1, visited)
  explore(grid, row, col - 1, visited)

  return True
  
  from collections import deque

def closest_carrot(grid, starting_row, starting_col):
  #receive a grid 
  #return how many steps to get a 'C'

  queue = deque([(starting_row, starting_col, 0) ] )
  visited = set([(starting_row, starting_col)])

  while queue:
    row, col, dst = queue.popleft()
    if grid[row][col] == 'C':
      return dst

    deltas = [(1,0), (0, 1), (-1,0), (0,-1)]

    for delta in deltas:
      delta_row, delta_col = delta
      neighbor_row = row + delta_row
      neighbor_col = col + delta_col
      row_inbounds = 0 <= neighbor_row < len(grid)
      col_inbounds = 0 <= neighbor_col < len(grid[0])
      pos = (neighbor_row, neighbor_col)

      if row_inbounds and col_inbounds and grid[row][col] != 'X' and pos not in visited:
        queue.append((neighbor_row, neighbor_col, dst + 1))
        visited.add(pos)

      

  return -1
    
    from collections import deque

def shortest_path(edges, node_A, node_B):
  #receive an edge list

  #return shortest shortest_path
  #ex:


  #build graph
  #travel form w to z
  #increment dst
  #return dst


  graph = build_graph(edges)
  visited = set()
  queue = deque([(node_A, 0)])

  while queue:
    current, dst = queue.popleft()

    if current == node_B:
      return dst

    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append((neighbor, dst + 1))
        visited.add(neighbor)
  return -1

def build_graph(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return graph
  

from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  #receive a n x n
  #return min moves (int)

  #start from kr, kc, return mvoes of pr and pc

  moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
  visited = set([(kr, kc)])
  queue = deque([(kr, kc, 0)])

  while queue:
    row, col, dst = queue.popleft()
    if (row, col) == (pr, pc):
      return dst

    for dr, dc in moves:
      delta_row = row + dr
      delta_col = col + dc
      row_inbounds = 0 <= delta_row < n
      col_inbounds = 0 <= delta_col < n  
      pos = (delta_row, delta_col)
      if row_inbounds and col_inbounds and pos not in visited:
        visited.add(pos)
        queue.append((delta_row, delta_col, dst + 1))
        
  return None

        from collections import deque

def knight_attack(n, kr, kc, pr, pc):
  moves = [
    (-2, -1), (-2,1),
    (2, -1), (2, 1), 
    (1, -2), (-1, 2),
    (1, 2), (-1, -2)
  ]

  queue = deque([(kr, kc, 0)])
  visited = set((kr,kc))

  while queue:
    row, col, dst = queue.popleft()

    if (row,col) == (pr, pc):
      return dst

    for nr, nc in moves:
      new_row = row + nr
      new_col = col + nc
      row_inbounds = 0 <= new_row < n
      col_inbounds = 0  <= new_col < n
      pos = (new_row, new_col)
      if row_inbounds and col_inbounds and pos not in visited:
        visited.add(pos)
        queue.append((new_row, new_col, dst + 1))
  return None

def can_color(graph):
  #receive an undirected graph
  #return boolean
  coloring = {}
  for node in graph:
    if node not in coloring and validate(graph, node, coloring, False) == False:
      return False
  return True


def validate(graph, node, coloring, current_color):
  if node in coloring:
    return current_color == coloring[node]

  coloring[node] = current_color

  for neighbor in graph[node]:
    if validate(graph, neighbor, coloring, not current_color) == False:
      return False
  return True
    
  def tolerant_teams(rivalries):
  #receive a list of names
  #return boolean
  #ex:

  #build a graph
  graph = build_graph(rivalries)
  coloring ={}

  for node in graph:
    if node not in coloring:
      if validate(graph, node, coloring, False) == False:
        return False

  return True

def validate(graph, node, coloring, current_color):
  if node in coloring:
    return current_color == coloring[node]

  coloring[node] = current_color

  for neighbor in graph[node]:
    if validate(graph, neighbor, coloring, not current_color) == False:
      return False
  return True
    

def build_graph(edges):
  graph = {}

  for edge in edges:
    a,b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

  return graph

def rare_routing(n, roads):
  #receive n city, and the roads that are connected to each other
  #return boolean
  #ex: 

  #iterate through a graph
  #check if it does not equal the last city seen
  #and it does not return False, return False
  #else return True

  graph = build_graph(n, roads)
  visited = set()
  valid = validate(graph, 0, visited, None)
  return valid and len(visited) == n

def validate(graph, node, visited, last_node):
  if node in visited:
    return False

  visited.add(node)

  for neighbor in graph[node]:
    if neighbor != last_node and validate(graph, neighbor, visited, node) == False:
      return False
  return True

def build_graph(n, roads):
  graph = {}

  for city in range(n):
    graph[city]= []

  for road in roads:
    a,b = road
    graph[a].append(b)
    graph[b].append(a)
    
  return graph
  
  def safe_cracking(hints):
  #build graph
  #topological order

  graph = build_graph(hints)
  return topological_order(graph)

def build_graph(hints):
  graph = {}

  for a,b in hints:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
  return graph

def topological_order(graph):
  num_parents = {}
  for node in graph:
    num_parents[node] = 0

  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  ready = [node for node in graph if num_parents[node] == 0]

  order = ''
  while ready:
    node = ready.pop()
    order += str(node)
    for child in graph[node]:
      num_parents[child] -=1
      if num_parents[child] == 0:
        ready.append(child)

  return order

def string_search(grid, s):
  #receive a grid
  #return boolean
  #ex: 

  #iterate through row and cols
  #check if you find the first letter of it 
  #then iterate via bfs (next neighbors to see if it is the next one too)
  #if not, return False
  #else return True


  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if dfs(grid, r, c, s):
        return True
  return False


def dfs(grid, r, c,s):
  if s == "":
    return True
    
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])

  if not row_inbounds or not col_inbounds:
    return False

  if grid[r][c] != s[0]:
    return False

  suffix = s[1:]

  char = grid[r][c]
  grid[r][c]= '*'
  result = dfs(grid, r + 1, c,suffix) or dfs(grid, r - 1, c,suffix) or dfs(grid, r, c - 1,suffix) or dfs(grid, r, c + 1,suffix) 

  grid[r][c] = char

  return result

from collections import Counter

def intersection_with_dupes(a, b):
  count_a = Counter(a)
  count_b = Counter(b)

  result  =[]
  for item in count_a:
    for i in range(0, min(count_a[item], count_b[item])):
      result.append(item)
  return result
      
      def exclusive_items(a, b):
  #receive two list of integers
  #return a list back of list that do not belong in each other
  #ex: 

  result = []
  set_a = set(a)
  set_b = set(b)

  for item in set_a:
    if item not in set_b:
      result.append(item)

  for item in set_b:
    if item not in set_a:
      result.append(item)
  return result

def remove(st, n):
    #receive a string with an integer
    #return a string back with ! removed by n amount
    #ex: 'Hi!', 1 => 'Hi'
    
    return st.replace('!', '', n)

from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
    
    def quote(fighter):
    #receive a string of names
    #return specific saying associated with string
    #ex: gEorge sainT Pierre => "I am not impresed"
    
    
    if fighter.lower() == "george saint pierre":
        return "I am not impressed by your performance."
    elif fighter.lower() == 'conor mcgregor':
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    
    def even_numbers(arr,n):
    #receive a list of integers and an int
    #return a new a list up to n filled with even numbers
    #ex: 
    
    #iterate through arr check if it's % 2 == 0 and decrement from n
    
    result = []
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] % 2 == 0 and n > 0:
            result.append(arr[i])
            n -= 1
    return result[::-1]

def count_red_beads(n):
    #receive an integer
    #return the amount of red beads placed between blue beads
    #ex: brrb => 2 
    #need 2 blue beads (opening and closing)
    
    #brrbrrb => 4
    #brrbrrbrrbrrb => 8
    
    if n < 2:
        return 0
    else:
        return (n * 2) - 2
    
    def solution(number):
    #receive a number
    #return sum of all number in beween that divisible of 3 or 5
    #ex: 
    
    if number < 0:
        return 0
    
    total = 0
    for num in range(1, number):
        if num % 3 == 0:
            total += num
        elif num % 5 == 0:
            total += num
    return total
  
  class Solution:
    def romanToInt(self, s: str) -> int:
        #receive a string
        #return total output of string
        #ex: "IIII" => 4

        #iterate through string
        #check if it is in map, add to the total
        #return total

        symbol_map = { 
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0 

        for i in range(len(s)):
            current_char = symbol_map[s[i]]

            if i + 1 < len(s) and current_char < symbol_map[s[i + 1]]:
                total -= current_char
            else:
                total += current_char

        return total
    

    def find(roots, node):
  if node == roots[node]:
    return node
  return find(roots, roots[node])


def union(roots, a, b):
  root_a = find(roots, a)
  root_b = find(roots, b)

  if root_a == root_b:
    return 

  roots[root_b] = a

def count_components(n, edges):
  #receive a number of nodes, and an edge list
  #return the number of onnecte compedontes
  #ex: 

  #create a roots list
  #iterate through the rotos list
  #connecting the second node to first node
  #find the parent's node
  #return our count


  roots = [i for i in range(0, n)]

  for edge in edges:
    a,b = edge
    union(roots, a, b)

  count = 0
  for i in range(0, n):
    if roots[i] == i:
      count += 1

  return count
    

    def find(roots, node):
  if node == roots[node]:
    return node
  found = find(roots, roots[node])
  roots[node] = found
  return found


def union(roots, sizes, a, b):
  root_a = find(roots, a)
  root_b = find(roots, b)

  if root_a == root_b:
    return 

  if sizes[root_a] >= sizes[root_b]:
    roots[root_b] = root_a
    sizes[root_a] += sizes[root_b]
  else:
    roots[root_a] = root_b
    sizes[root_b] += sizes[root_a]

def province_sizes(n, roads):
  roots = [i for i in range(0, n)]
  sizes = [1 for i in range(0, n)]

  for a, b in roads:
    union(roots, sizes, a, b)

  return [ sizes[i] for i in range(0, n) if roots[i] == i ]

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  #receive a root Node
  #return the tree in depth_first_values

  if root is None:
    return []

  left = depth_first_values(root.left)
  right = depth_first_values(root.right)

  return [root.val, *left, *right]
  #O(n^2)

def uefa_euro_2016(teams, scores):
    #receive a list of string of teams (countries) and a list of integers
    #return a string
    #ex: ['Madrid', 'Barcelona'], [4, 4]
   # => # "At match Madrid - Barcelona, teams played draw."
    #ex: ['Madrid', 'Barcelona'], [2, 4]
    #=> # "At match Madrid - Barcelona, Barcelona won."
    
    
    #compare the scores of the first one and second
    #if first one > : return first team won, 
    #elif second team won
    #else it's a draw
    
#     winner = ""
    
    if scores[0] > scores[1]: #0 > 2
        return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
    elif scores[0] < scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
    else:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."
        
#     return f"At match{teams[0]} - {teams[1]}, {winner}"

def sort_my_string(s):
    #receive a string
    #return a string back where the chars at the even index comes first + space + chars at odd index
    #ex: "Hello" => Hlo el
    #.    01234
    
    #iterate throught the string
    #look at the index where the chars are located
    #then add them into the specific even or odd group they belong to
    #return even + space + odd
    
    
    evenChars = [] #Hlo
    oddChars = [] #el
    
    for i in range(len(s)): #Hello
        if i %2 == 0:
            evenChars.append(s[i])
        else:
            oddChars.append(s[i])
            
    return ''.join(evenChars) + ' ' + ''.join(oddChars)

def two_sum(numbers, target):
    #receive a list of integers, and an integer for target value
    #return the index position in a tuple that adds up to target
    #ex: [3, 4,5, 2], 7 => (0,1)
    
    #iterate through the nubmer slst
    #have another point loop through
    #add up the sum
    #check if the sum == target, return the index position
    
    
#     for i in range(0, len(numbers) -1):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 return (i, j)
    #time: O(n^2)
    #space:O(1)
    
    #find the difference between target and current number
    #check if number exists in an object, return the idx position
    
    pair = {}
    
    #{} #1: 0
     #.  2: 1
    
    for i in range(0, len(numbers)): #1, 2, 3
        difference = target - numbers[i] #4 - 3 =1
        if difference in pair: #
            return (i, pair[difference]) #(2, 0)
        else:
            pair[numbers[i]] = i
            
    #time:O(n)
    #spaceO(n)
    
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #receive a list of integers and the index position represents the days
        #return the max profit we can make by buying first and then selling
        #ex:  [7,1,5,3,6,4]
        #     1 2 3 4 5 6
        #        i
        #.              j

        #buy day 2 at $1
        #sell at the highest day at day 5 which 6
        #6 - 1 = 5

        #iterate through the list
        #have another loop check 
        #take the current $ - the second loop $
        #update our max total seen

        # maxProfit = 0
        # for i in range(0, len(prices)-1):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > maxProfit:
        #             maxProfit = profit
        # return maxProfit

        #start our buy on left side
        #sell later => sell starts on right side
        #take sell - buy 
        #update maxProfit if we've seen


        #[1,4,2]
        #b.   s.  max=2


        max_profit = 0 
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price

            max_profit = max(max_profit, profit)
        return max_profit
        
    def solution(number):
    #receive an integer
    #return an integer that is the total of the multiples
    #ex: 5 => 5 
    total = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
  
  def find_it(seq):
    #receive a list of integers
    #return the integers that occurs odd amount of times
    #ex: [1,1,1,3] =>1,3
    
    #iterate thorugh the list of integers
    #keep track of frequencies
    #iterate though the map
    #check which value is odd
    #returnt he integer
    
    freq_obj = {}
    
    for num in seq:
        freq_obj[num] = freq_obj.get(num, 0) + 1
        
    for item in freq_obj:
        if freq_obj[item] % 2 != 0:
            return item
    
    for item in seq;
       if seq.count(item) % 2 != 0:
          return item
def array_diff(a, b):
    #receive a list of integers
    #return the list of integers that don't belong in each others list
    #ex: [1,2,3,2], [2] => [1,3]
    
    #intiialize an empty list
    #iterate thorugh the numbs
    #check if b exists in a
    #don't add to the new list
    
    result = []
    
    for item in a:
        if item not in b:
            result.append(item)
    return result

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #receive a list of integers
        #return same list back where it's sorted
        #ex: 

        #iterate through the list of integers
        #check i and j next to oeach other
        #check if ==, then move i to j 

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        
  class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep track of total 

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
    
    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  #receive a root Node
  #return a list of the all the ndoes in depth_first_values
  #ex: 

  #base case: if it's empty, return an empty list
  #capture all left and capture all right

  if not root:
    return [ ]

  left = depth_first_values(root.left)
  right = depth_first_values(root.right)

  return [root.val, *left, * right]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def breadth_first_values(root):
  #receive a root node

  if not root:
    return []

  queue = deque([root])
  result = []

  while queue:
    current = queue.popleft()
    result.append(current.val)

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)
  return result

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if not root:
    return 0

  left = 0
  right = 0

  left += tree_sum(root.left)
  right += tree_sum(root.right)

  return root.val + left + right

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):

  if not root:
    return False 
    
  if root.val == target:
    return True 

  return tree_includes(root.left, target) or tree_includes(root.right, target)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #receive the root node of a tree
        #return an integer of the max depth of a tree found


        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

class Solution:
    def isValid(self, s: str) -> bool:
        #receive a string
        #return a boolean - True is where opening and closing of same kind , else it's False

        #ex: ")" => False
        #ex: "([)]" => True
        
        #iterate thorugh each character
        #check to see if it's an opening character
        #add to our stack 
        #if it is a closing character, check to see if the stack is not empty and if the previous item is an opening bracket
        #that corresponds with it
        #if it's not, return False
        #return True

        pairs = { 
           '[':  ']',
           '(':  ')',
            '{': '}',
        }


        stack = [] 

        for char in s: 
            if char in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                
                opening = stack.pop()

                if pairs[opening] != char:
                    return False
                
        return len(stack) == 0

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_min_value(root):
  #receive the root of a binary tree_min_value
  #return min value found
  #ex: 

  queue = deque([root])
  min_value = float("inf")

  while queue:
    current = queue.popleft()
    if current.val < min_value:
      min_value = current.val

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)
  return min_value
  

  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
  #return

  if not root:
    return float("-inf")

  if not root.left and not root.right:
    return root.val

  big_left = max_path_sum(root.left)
  big_right = max_path_sum(root.right)

  return root.val + max(big_left, big_right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #receive the root node
        #return an integer of count of nodes in trees
        #ex: 

        #using bfs

        if not root:
            return 0

        queue = deque([root])
        total = 0

        while queue:
            current = queue.popleft()
            total += 1
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return total


      # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #receive the root node
        #return an integer of count of nodes in trees
        #ex: 

        #using bfs

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None


def path_finder(root, target):
  result = _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]

def _path_finder(root, target):
  #receive the root Node
  #return a list back of nodes to reach target

  if not root:
    return None

  if root.val == target:
    return [ root.val ]

  left = _path_finder(root.left, target)
  if left is not None:
    left.append(root.val)
    return left
  right = _path_finder(root.right, target)
  if right is not None:
    right.append(root.val)
    return right
  return None



  # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_value_count(root, target):

  if not root:
    return 0
    
  match = 1 if root.val == target else 0

  left = tree_value_count(root.left, target)
  right = tree_value_count(root.right, target)
  

  return match + left + right

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def how_high(root):
  if not root:
    return -1

  return 1 + max(how_high(root.left), how_high(root.right))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current):
            if not node:
                return 0
            
            current = current * 10 + node.val
            if not node.left and not node.right:
                return current
            return dfs(node.left, current) + dfs(node.right, current)
        return dfs(root, 0)

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def bottom_right_value(root):
  #receive a the root node  
  #return left most

  #ex: 

  queue = deque([root])
  while queue:
    current = queue.popleft()

    if current.left:
      queue.append(current.left)

    if current.right:
      queue.append(current.right)

  return current.val
      
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths

def _all_tree_paths(root):
  #receive the rnode of th eroot
  #return all tree paths 
  #ex: 

  if not root:
    return []

  if not root.left and not root.right:
    return [ [root.val] ]

  all_paths = []
  left = _all_tree_paths(root.left)
  for path in left:
    path.append(root.val)
    all_paths.append(path)
    
  right = _all_tree_paths(root.right)
  for path in right:
    path.append(root.val)
    all_paths.append(path)
  return all_paths

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def tree_levels(root):

  if not root:
    return []
  
  result = []
  queue = deque([root])
  while queue:
    levels = []

    for current in range(len(queue)):
      current = queue.popleft()
      levels.append(current.val)

      if current.left:
        queue.append(current.left)

      if current.right:
        queue.append(current.right)

    
    result.append(levels)
  return result
    
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #receive the root of a binary tree
        #return a list stating their averages
        
        # do it via bfs using queue
        #iterate through node
        #add it into the queue
        #if they have a left and/or right children, add to queue
        #calculate their average 
        #add to the result list
        #return list

        result = [ ]
        queue = deque([root])
        while queue:
           
            total = 0
            total_nodes = 0
            for node in range(len(queue)):
                current = queue.popleft()
                total += current.val
                total_nodes += 1
                avg = total / total_nodes
                
                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
            result.append(avg)
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #receive the root node of a binary search tree
        #return min difference between values of any two different nodes in trees
        #ex: 

        #traverse through the left and right
        #find the smallest min found
        #but smallest nodes can be found on the left and left side - so no go on this

        #bfs? but you're only looking at it from level by level - so no go on this

        #since it is a bst, always look at the left side since the values are less

        #iterate through the left side

        #do via inorder traversal

        result = []
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        min_value = float("inf")

        for i in range(1, len(result)):
            diff = result[i] - result[i-1]
            if diff < min_value:
                min_value = diff
        return min_value
        

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):

  if not root:
    return [ ]

  if not root.left and not root.right:
    return [ root.val ]

  left = leaf_list(root.left)
  right = leaf_list(root.right)

  return [*left, *right]

  def max_subarray_sum_size_k(nums, k):
  #receive a list of integers
  #return the k amount max sum seen 
  #ex: 

  #iterate up to the k amount
  #check the sum
  #update max total seen
  #return max seen

  # max_total = float('-inf')

  # for i in range(0, len(nums) - k + 1):
  #   current_sum = sum(nums[i:i + k])
  #   if current_sum > max_total:
  #     max_total = current_sum

  # return max_total

  current_sum = sum(nums[0: k] )
  max_total = current_sum

  for i in range(0, len(nums)-k):
    current_sum -= nums[i]
    current_sum += nums[i + k]
    if current_sum > max_total:
      max_total = current_sum
  return max_total

import math

def max_subarray_product_size_k(nums, k):
  current_product = math.prod(nums[0: k])
  max_total = current_product
  for i in range(0, len(nums) -k ):
    current_product /= nums[i]
    current_product *= nums[i + k]
    if current_product > max_total:
      max_total = current_product
  return max_total

    # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  #receive head of a LL
  #return total sum from all values
  #ex: 

  current = head
  total = 0

  while current:
    total += current.val
    current = current.next
  return total

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        min_value = float('inf')
        i = 0

        for j in range(1, len(result)):
            diff = result[j] - result[i]
            if diff < min_value:
                min_value = diff
            i += 1
        return min_value


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  #receive the head of a list
  #return the list back with node re remove_node
  #ex: 

  if head.val == target_val:
    return head.next

  current = head
  prev = None
  
  while current:
    if current.val == target_val:
      prev.next = current.next
      break;
    prev = current
    current = current.next

  return head

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  #increment at node until we reach indexed

  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head

  current = head
  idx = 0 
  
  while current: 
    next = current.next
    if idx == index:
      current.next = Node(value)
      current.next.next = next

    current = current
    idx += 1

  return head
    
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        obj1 = {}
        obj2 = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in obj1 and obj1[c1] != c2:
                return False

            if c2 in obj2 and obj2[c2] != c1:
                return False

            obj1[c1] = c2
            obj2[c2] = c1

        return True
        
        # class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_palindrome(head):

  result = []
  current = head
  while current:
    result.append(current.val)
    current = current.next

  return result == result[::-1]

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def middle_value(head):
  # result = []
  # current = head
  # while current:
  #   result.append(current.val)
  #   current = current.next

  # mid = len(result) //2
  # return result[mid]


  # left = 0
  # right = len(result) - 1

  # while left <= right:
  #   mid = (left + right) // 2
  #   if len(result) % 2 == 0:
  #     return result[mid + 1]
  #   else:
  #     return result[mid]

  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow.val

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b,2)
        total = int_a + int_b
        return bin(total)[2:]
        
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #receive a list of sorted integers
        #return a list back starting the strings
        #ex: 

        #iterate thorugh the integers
        #see if the num is + 1 of it, if not, capture the start and the end 
        #return list

        if not nums:
            return []

        result = []

        start = 0

        for end in range(1, len(nums)):
            if nums[end] != nums[end - 1] + 1:
                if start == end - 1:
                    result.append(str(nums[start]))
                else:
                    output = f"{nums[start]}->{nums[end - 1]}"
                    result.append(output)
                start = end
            
        if start == len(nums) - 1:
            result.append(str(nums[start]))
        else:
            output = f"{nums[start]}->{nums[-1]}"
            result.append(output)
                
        return result

        #[0, 1,  2,  4,  5,7]
        #s
        #.      e1  e2

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #receive a list of sorted integers
        #return a list back starting the strings
        #ex: 

        #iterate thorugh the integers
        #see if the num is + 1 of it, if not, capture the start and the end 
        #return list

        if not nums:
            return []

        result = []

        i = 0

        while i < len(nums):
            start = nums[i]
            j = i 
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1

            if start == nums[j]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[j]}")
            i = j + 1

                
        return result

        #[0, 1,  2,  4,  5,7]
        #s
        #.      e1  e2
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #receive a list of integers
        #return the list bakc
        #ex:

        #sort by start time
        #initialize the result list with the currrent start
        #iterate and check if the next start overlaps with end
        #update the end and add it in the list

        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]

        for j in range(1, len(intervals)):
            [start, end] = intervals[j]
            [prevStart, prevEnd] = result[-1]
            if start <= prevEnd:
                result[-1][1] = max(prevEnd,end)
            else:
                result.append(intervals[j])

        return result
    
    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #receive a list of integers
        #return the list bakc
        #ex:

        #sort by start time
        #initialize the result list with the currrent start
        #iterate and check if the next start overlaps with end
        #update the end and add it in the list

        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]

        for j in range(1, len(intervals)):
            [start, end] = intervals[j]
            [prevStart, prevEnd] = result[-1]
            if start <= prevEnd:
                result[-1][1] = max(prevEnd, end)
            else:
                result.append(intervals[j])

        return result

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #sort by start time
        #iterate throught he interval
        #check if the start of newInterval <= end of the interval we are looking at

        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        results = [intervals[0]]

        for i in range(1, len(intervals)):
            [start, end] = intervals[i]
            if results[-1][1] >= start:
                results[-1][1] = max(end, results[-1][1])
            else:
                results.append(intervals[i])

        return results

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast is slow:
                return True

        return False


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        #receive a list of words (lowercase letters)
        #return a list back of common characters that are in each word
        #ex: ['hello', 'app', 'soccer'] => []

        #initalize an empty list
        #iterate through word and check the character in the other words


        #iterate through each word
        #add them into their own separate obj to keep track of the occurence of the ltter
        #ex: { 
        # 'h':1, 
        # 'e': 1,
        # 'l': 2, 
        # 'o' : 1,
        #}
        #check each obj and verify if the characters exist in the other strings
        #if it does exist in all of the other strings, add it our result list
        #tiime: O(n * m) => n characters if words
        #space: O (n)

        result = []

        for word in words:
            freq= {}
            for char in word:
                freq[char]= freq.get(char, 0) + 1 #{'h': 1}
            result.append(freq)


        frequen = []
        for char in result[0]:
            minum = result[0][char]

            for fre in result[1:]:
                minum = min(minum, fre.get(char,0))

            frequen.extend([char] * minum)

        return frequen

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #receive a list of tuples of start and end
        #return boolean, true if can attend all, else false
        #ex: [(0, 1), (3, 5), (2, 6)] => false
        #[(0,1),(2,6),(3,5)]

        #ex: 0 1 2 3 4 5 6
          #  ---
          #        ----
          #      ---------

        #sort by start time
        #check if the current start is <= end time prev
        #if it is, return false
        #else after checking everything,r eturn true

        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
           if intervals[i].start < intervals[i - 1].end:
            return False
            
        return True

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #receive a room
        #return the min rooms needed
        #for each room you need, increment
        #keep track of room needed

        #ex: [(1,5),(4,10),(8, 9)]
        #.                  i

        intervals.sort(key=lambda i:i.start)
        min_heap = []

        if len(intervals) == 1:
            return 1

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #receive a room
        #return the min rooms needed
        #for each room you need, increment
        #keep track of room needed

        #ex: [(1,5),(4,10),(8, 9)]
        #.                  i

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        result = 0
        count = 0
        s = 0
        e = 0

        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            
            result = max(count, result)
        return result


def filter_string(st):
    #receive a string of integer
    #return the integers back
    #ex: 'raw12'=> 12
    
    #iterate through the string
    #check each char if it is a an integer
    #add together as a list
    #return it as an int back
    
    result = ''
    
    for char in st:
        if char.isdigit():
            result += char
    return int(result)

        
        def longest_consec(strarr, k):
    #recevie a list of strings
    #return the string of largest length of string seen
    #ex: 
    
    #iterate thorough the list of strings
    #keep adding strings until k has been reached
    #keep track of longest length seen 
    #return longest word seen
    
    if k < 0:
        return ''
    
    longword = ''
    longlenth = 0
    
    for i in range(len(strarr) - k + 1):
        currentWord = ''.join(strarr[i:i + k])
        if len(currentWord) > len(longword):
            longword = currentWord
            longLength = len(currentWord)
    return longword
    
#     longWord = ''
#     longLength = 0
#     current = ''
#     i = 0
#     j = 0
    
#     while j <len(strarr):
#         current += strarr[j]
#         j += 1
        
#         while (j - i) == k:
#             longWord = current
#             longLength = max(longLength, len(current))
#             current -= strarr[i]
#             i += 1
#             j += 1
            
#     return longWord
  
  def valid_braces(string):
    parens = {
        '(': ')',
        '{':'}',
        '[':']'
    }
    stack = []
    
    for char in string:
        if char in parens: #opening
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if parens[stack.pop()] != char:
                return False
    return len(stack) == 0
    
def find_leftmost_index(nums, target):
  #receive a list of integers, and the target integer of nums
  #return idx of most left idx
  #ex: 

  left = 0
  right = len(nums) - 1
  leftmost = -1

  while left <= right:
    mid = (left + right) // 2

    if target < nums[mid]:
      right = mid - 1
    elif target > nums[mid]:
      left = mid + 1
    else:
      right = mid - 1
      leftmost = mid


  return leftmost

def find_leftmost(nums, target):
  left = 0
  right = len(nums)-1 
  leftmost = -1

  while left <= right:
    mid = (left + right) //2
    if target < nums[mid]:
      right = mid - 1
    elif target > nums[mid]:
      left = mid + 1
    else:
      right = mid - 1
      leftmost = mid
  return leftmost

def find_rightmost(nums, target):
  left = 0
  right = len(nums)-1 
  rightmost = -1

  while left <= right:
    mid = (left + right) //2
    if target < nums[mid]:
      right = mid - 1
    elif target > nums[mid]:
      left = mid + 1
    else:
      left = mid + 1
      rightmost = mid
  return rightmost


def count_in_sorted_array(nums, target):
  #receive a list of integers
  #return the count of occurrences
  #ex: 

  leftidx = find_leftmost(nums, target)
  rightidx = find_rightmost(nums, target)

  if rightidx == -1:
    return 0
  else:
    return rightidx - leftidx + 1
  
  def min_in_rotated_sorted_array(nums):
  #receive a list of rotated sorted integers
  #return mind element found
  #ex:[5,6,7,8,9]
  #   l    m   r
  #   

  left = 0
  right = len(nums) - 1

  while left < right:
    mid = (left + right) // 2
    if nums[mid] < nums[right]:
      right = mid
    else:
      left = mid + 1
  return nums[left]

def min_in_rotated_sorted_array(nums):
  #receive the list
  #return idx found of smallest nums value
  #ex: 

  low = 0
  right = len(nums) - 1

  while low < right:
    mid = (low + right) // 2

    if nums[mid] < nums[right]:
      right = mid
    else:
      low = mid + 1
      
  return nums[low]

def find_peak(nums):
  #receive a list of nums
  #return the idx of find_peak
  #ex: ([2,5,7,10,12])
  #     l    m     h

  low = 0
  high = len(nums) - 1 

  while low < high:
    mid = (low + high) // 2
    if nums[mid] < nums[mid + 1]:
      low = mid + 1
    else:
      high = mid

  return low

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        track1 = { }

        result = []
        for num in nums1:
            track1[num] = track1.get(num, 0) + 1

        for item in nums2:
            if item in track1 and track1.get(item) > 0:
                result.append(item)
                track1[item] -= 1
        return result
        
        def rotate_matrix(arr):
    result = []
    for col in range(len(arr[0]) - 1, -1, -1):
        new_row = []
        for row in range(len(arr)-1, -1, -1):
            new_row.append(arr[row][col])
        new_row.reverse()
        result.append(new_row)
    return result
  
  def swap(matrix, row1, row2, *columns):
    for col in columns:
        matrix[row1][col], matrix[row2][col] = matrix[row2][col], matrix[row1][col]
    
    return matrix

def get_matrix(n):
    result = [[0] * n for i in range(n)]
    
    for row in range(n):
        for col in range(n):
            if row == col:
                result[row][col] =1 
                
    return result
    
    
    import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sortNums = sorted(nums)

        # return sortNums[-k]


        heap = []
        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                    self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                    + matrix[r][c]
                )
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )

#         everything above
# +
# everything left
# -
# overlap
# +
# current value


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #receive a list of integers
        #return the a list of the top k elements
        #ex: 

        #keep track of the counter
        #iterate through until k is done
        #return the item in the list

        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1

        sorted_items = sorted(
        frequency.items(),
        key=lambda pair: pair[1],
        reverse=True)

        result = []

        for num,count in sorted_items[:k]:
            result.append(num)
        return result


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #receive a list of integers
        #return the most common elements that occurs more than n/3 times
        # 5 /3 > 1 => add to the reuslt
        #iterate through
        #keep track of occurences
        #then divide it by 3 ; if greater than 1 > add toe the reuslt array


        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        result = []
        for item in frequency:
            if frequency[item] / 3 > 1:
                result.append(item)
        return result
    
    class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #receive a list of integers,
        #return the output where ach value is the product of all elements except itself
        #ex: 

        #create a result list
        #iterate through the first time and multiply by one
        #then add to the list

        #nums=[1,2,4,6]
        #     i
        #        j
        #    


        result = []
        i = 0

        
        for i in range(len(nums)):
            multiplier = 1
            for j in range(len(nums)):
                print(nums[j],nums[i])
                if i != j:
                    multiplier *= nums[j]

            result.append(multiplier)
        
        return result

  

        
  


