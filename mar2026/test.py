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

