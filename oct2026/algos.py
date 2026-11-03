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

                    


