class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #receive a list of numbers
        #return the index position of target
        #ex: [3,4,5] => 2 => 0

        #iterate through each nums
        #look to see if target is <= next num,
        #return the index value

        # for idx,num in enumerate(nums):
        #     print("num:", num, "idx:", idx)
        #     if target <= num:
        #         return idx
        #  return len(nums)

    #left and right
    #while left and right <= to each other
    #find middle
    #check if target >= middle:
    #go to the right, move left pointer up
    #else, move right pointer down
    #return left

    left, right = 0, len(nums) -1
    
    while left <= right:
        middle = (right - left) // 2
        if nums[middle] == target:
            return middle
        else if nums[middle] <= target:
            right = middle - 1
        else:
            left = middle + 1
    return left



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #receive an array of distinct integers
        #return the index position of where our target should be placed
        #ex: [3,4,5,10], target = 1 => return index of 0

        #brute force:
        #iterate through every number in the list
        #check if target <= number
        #return the index
        #else return the end index

        # for idx, num in enumerate(nums):
        #     if target <= num:
        #         return idx
        # return idx + 1

        #time: O(N)
        #space: O(1)

        #optimized solution: binary search
        #left starts at 0, right starts at the end index
        #calcl the middle
        #check if our middle is our target,
        #return the middle index
        #check if the target <= middle idx,
        #check right pointer will move down
        #else move left pointer up

        left, right = 0, len(nums) - 1
        while left <= right: 
            middle = (right - left) + 1 // 2
            if nums[middle] == target:
                return middle
            elif target <= nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return left
        
            
    def string_to_array(s):
    # receive a string of upper and lowecases and spaces
    #return a list of strings splut
    
    #ex: 'Hello world' => ['Hello', 'world']
    
    return list(s.split()) if len(s) > 0 else ['']
    return s.spit(" ")def to_jaden_case(string):
    #receive a string of words with no punctuations
    #return the string back with the first letter of every word uppercase
    
    #ex: 'hello world' => 'Hello World'
    
    #brute force: 
    #initialize a new string
    #iterate through each word
    #captilize the first letter + all of the remaining chars
    #add it to the new string
    #return the string

    outputArr = []
    for word in string.split(" "):
        word = word[0].upper() + word[1:]
        outputArr.append(word)
    return ' '.join(outputArr)

#time: O(N) for words in string
#space: O(n) for creating space for output arr



#     arrayString = string.split(" ")
#     return ''.join(word.captialize() for word in arrayString)

def solution(text, ending):
    # receive a string of lowercase letters, and a string for end
    #return true if ending is the true ending for text
    #else, return false
    
    #ex: 'jump','p' => true
    
    return text.endswith(ending)

    class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #receive a list of integers, and an integer for target
        #return the index position of target if found, else -1

        #brute force:
        #iterate through each num
        #check if num is target
        #return index
        #time;O(n) n for num in nums
        #space: O(1) returning idx only

        #optimized: binary search
        #set up left and right pointers
        #while they do not cross
        #find the middle
        #if middle idx == target, return middle idx
        #else check if the target is <= middle value, 
        #look on left
        #else look on right

        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right-left) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            if nums[middle] <= nums[right]:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle -1
        return -1

        
    class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #receive a list of weights, days = integer
        #return smallest weight capacity

        minCap = max(weights)
        maxCap = sum(weights)

        for cap in range(minCap, maxCap + 1):
            current_days = 1
            current_wgt = 0

            for weight in weights:
                current_wgt += weight
                if current_wgt > cap:
                    current_days += 1
                    current_wgt = weight
            if current_days <= days:
                return cap
        return -1

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #receive a list of weights, days = integer
        #return smallest weight capacity

        # minCap = max(weights)
        # maxCap = sum(weights)

        # for cap in range(minCap, maxCap + 1):
        #     current_days = 1
        #     current_wgt = 0

        #     for weight in weights:
        #         current_wgt += weight
        #         if current_wgt > cap:
        #             current_days += 1
        #             current_wgt = weight
        #     if current_days <= days:
        #         return cap
        # return -1

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) //2
            current_days = 1
            current_weight = 0

            for weight in weights:
                current_weight += weight
                if current_weight > mid:
                    current_days += 1
                    current_weight = weight
            if current_days <= days:
                right = mid
            else:
                left = mid + 1
        return left
                

    def searchInSortedMatrix(matrix, target):
    #receive a 2D matrix, and an integer number
    #return the 2D location if target found
    #ex:

    #iterate thorugh rows and cols
    #find the middle
    #chceck if target is <= middle value
    #, then checkother half, else check right half

    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col]> target:
            col -=1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row, col]
    return [-1,-1]

    def compress(s):
  #receive a string of lower and upper letters
  #return the compressed vversion of a string
  #ex: 'aaabba' => '4a2b'


  #create a list
  #push in count of letters seen
  #else start new and refresh count

  result = []
  count = 1
  
  for i in range(len(s)):

    if s[i] == s[i+1]:
      count += 1
    else:
      result.append({count}s[i])
  return ''.join(result)
    def is_divisible(n,x,y):
    #receive all 3 integers
    #return a boolean - True if x and y // n
    
    #ex: 12, 6, 2; 2 * x = 12, 6 * y. = 12
    #return True
    
    #12/6 => 2 => True => 0
    # 6 in to 12 with how many remainders left over which is 0 => True
    #12/5 => 10 => 2 => False
    #5 * 2 = 10
    #12 - 10 = 2
    
    #brute force:
    #check if x % n == 0 and if y % n == 0: return True
    #else return False
    
#     if n % x == 0 and n % y == 0:
#         return True
#     else:
#         return False

    return n % x == 0 and n% y == 0

#time: O(1)
#space: O(1)


