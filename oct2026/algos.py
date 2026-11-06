def longest_subarray_sum(nums, target_sum):
  #receive a list of integers, and a target target_sum
  #return the length of longest subarry that returns the target
  #ex: 

  #iterate through nums, with left and right at 0
  #keep expanding window while total of window < = target_sum
  #if it == target_sum, capture the window size
  #update it for max variable


  max_window = 0
  left = 0
  right = 0
  total = 0
  
  for right in range(0, len(nums)):
    total += nums[right]

    while total  > target_sum:
      total -= nums[left]
      left += 1
    if total == target_sum:
      max_window = max(max_window, (right - left + 1) )

  return max_window if max_window != 0 else -1
      
    def longest_unique_substring(s):
  #receive a string of chars lowercase
  #return the longest unique strings
  #ex: 

  #put chars in sets
  #if char not in set
  #add, extend right
  #if char in set, move left

  unique = set()
  left = 0
  longest = 0

  for right in range(len(s)):
    if s[right] not in unique:
      unique.add(s[right])
    elif s[right] in unique:
      longest = max(longest, (right - left + 1))
      left += 1
      unique.remove(s[left])
      print(unique)
  return longest

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #receive a list of strings
        #return the integer representation of it
        #ex:

        #if reach integer, add to stack
        #if reach a '+', '-', '*', and '/'.
        #then pop the previous number to calculate

        stack = []
        symbols = ['+', '-', '*', '/']

        result = 0

        for char in tokens:
            if char not in symbols:
                stack.append(int(char))
            else:
                first = stack.pop()
                second = stack.pop()

                if char == "+":
                    result = first + second
                elif char == '-':
                    result = second - first
                elif char == "*":
                    result = first * second
                elif char == '/':
                    result = int(second /first)
                stack.append(result)
        return stack[0]

                    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #receive a head of a ll 
        #return the ll intertwined
        #ex: 

        if not head:
            return []

        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        i = 0
        j = len(nodes)- 1

        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j-=1
        nodes[i].next = None

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #receive a list of integers
        #return the max profit received
        #ex: [2,3,4]
        #.   buy. sell => 2

       # [10,1,5,6,7,1]
       #. b
       #. s
        # 0

        #iterate through the list of integers with sell adn buy
        #calculate the price made and keep track of max price
        
        maxProfit = 0
        buy = 0

        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            profit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, profit)

        return maxProfit
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #receive a list of integers
        #return the max heigt you can get 

        #[1,7,2,5,4,7,3,6]
        #   l             r
        #. 
        #ex: iterate through with two pointers
        #cal the width  * highest height seen
        #store as max height seen

        left = 0
        right = len(heights) - 1
        maxHeight = 0

        while left < right:
            width = right - left
            height = min(heights[right], heights[left])
            curr = height * width
            maxHeight = max(maxHeight, curr)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -=1
            else:
                left += 1
                

        return maxHeight

            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> bool:
        #receive a list of integers, and a target int
        #return true if pair is found, else False
        #ex:

        #left and right since it is sorted

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                return True
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -=1
        return False
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #receive a list of integers
        #return a list of lists of triplets back together
        #ex:

        #iterate through the list of nums
        #then do left and right with the vals next to it
        #if they add to 0, add as triplets into list

        nums.sort()

        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i +1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -=1 
        return result

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Your code goes here
        count = 0

        nums.sort()

        for i in range(len(nums)- 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = 1
            right = len(nums) -1 

            while left < right:
                if nums[i] + nums[left] > nums[right] and nums[i] + nums[right] > nums[left] and nums[left] + nums[right] > nums[i]:
                    count += 1
                    left += 1
                    right -=1
                elif nums[i] + nums[left] > nums[right] and nums[i] + nums[right] > nums[left] and nums[left] + nums[right] > nums[i]:
                




        return count


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        count = 0

        for i in range(len(nums) - 1, -1, -1): 
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -=1
                else:
                    left += 1
        return count

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #receive a list of integers
        #return a list where all 0's are pushed to the end
        #ex: 

        #use i and j (right)
        
        #check if j is 0, then move it down
        #else check if i is 0, swap it with j's position
        
        i = 0
        j = len(nums) - 1

        while i < j:
            if nums[j] == 0:
                j -=1
            elif nums[i] == 0 and nums[j] != 0:
               nums[i], nums[j] = nums[j], nums[i]
               j-=1
               i += 1
            elif nums[i] != 0:
                i += 1
        return nums

print(Solution().moveZeroes([0,1,0,3,12]))

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j],nums[i]
                i += 1