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

def stairs_in_20(stairs):
    #receive an array for each day in the week in an array (2D array)
    #return total sum amount of stairs climbed in 20
    
    #ex: [[12,35], [35,42], [34], [23,12], [23,65], [343,52], [23,52], [3]]
    
    #edge cases: will there be any days where the array are empty? => 0
    
    #initialize a sum
    #iterate through the stairs
    #take the sum of each inner arrays
    #add the total to the top sum
    #return sum

    
    total = 0
    for weekday in stairs:
        total += sum(weekday)
    return total * 20

return sum(sum(day)for day in stairs) * 20

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #receive a list of integers - positive numbers and all numbers are unique
        #return the integer that's missing

        #ex: [5,3,4]
        #[3,4,5] => 6 that's missing
        #length = n = 3
        #invalid because it is not [0, n]

        #[0,1] => 2
        #length = [0,2]

        #ex: [0,3,2]
        #length = 3
        #return 1
        
        #brute force:
        #sort the array
        #check the number starting at idx 1
        #check the number before to see if it is num - 1
        #if it isn't, return the specific num


        #[3,0,1]
        # nums.sort() #[0,1,3]

        # for i in range(1, len(nums)): #3
        #     if nums[i] -1 != nums[i - 1]: #3 -1 = 2 != 1
        #         return nums[i] -1
            
        # return nums[i] + 1

        #time: O(n log n ) due to sorting all the nums
        #space: O(1)

        #optimized: on time: use a Set
        #create a new set
        #iterate through nums list
        #check if set has previous number
        #if it does, then return the num - 1
        #else add it to the set

        # numSet = set() # { }
        # for i in range(len(nums)): #0
        #     if not nums[i] - 1 in numSet and nums[i] != 0: #0 - 1 = -1
        #         return nums[i] - 1 # -1
        #     else:
        #         numSet.add(nums[i])
        # return nums[i] + 1

        numSet = set(nums) # { 0,3,2}
        for i in range(len(nums)):
            if not nums[i] - 1 in numSet and nums[i] != 0:
                return nums[i] -1
            
        return nums[i] + 1

#time: O(n) => for each num in nums
#space: O(1) => returning a number back
        
        numSet = set(nums)
        missingNum = 0

        while missingNum in numSet:
            missingNum += 1
        return missingNum
    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #receive an array of integers
        #return the top k elements

        #create an object
        #keep count of values
        #create buckets for the counts

        #iterate through the buckets
        #add in the key into the value buckets

        #iterate through buckets starting from right to left
        #pull out K size

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for num in range(len(nums) + 1)]
        
        for key,value in count.items():
            buckets[value].append(key)

        result = []

        for i in range(len(buckets) - 1, -1, -1):
            for i in buckets[i]:
                result.append(i)
                if len(result) ==k:
                    return result

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k-1]
    
#time: O(n logn)
#space:O(n)        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap) # convert to min-heap
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.lower = []
        self.upper = []
        heapq.heapify(self.lower)
        heapq.heapify(self.upper)

    def insert(self, number):
        # if the length of one is greater than the other, I'd insert from lower to upper
        #or have upper go to lower
        #then rebalance
        #get updated Median
        if not self.lower or number < -self.lower[0]:
            heapq.heappush(self.lower, -number)
        else:
            heapq.heappush(self.upper,number)
        self.rebalance()
        self.updateMedian()

    def rebalance(self):
        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def updateMedian(self):
        if len(self.lower) == len(self.upper):
            self.median = (-self.lower[0] + self.upper[0]) /2
        else:
            self.median = -self.lower[0]

    def getMedian(self):
        return self.median
    
    class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        #receive a list of integers
        #return a list of strings with outputs based on their ranks

        #ex: [3,4,1,2] => ['Bronze Medal', '4', 'Gold Medal', 'Silver Medal']

        #brute force:
        #sort the score from highest to smallest
        #if the ranking is placed first in the sorted arrays, we are going to find the original idx
        #from original array and update it accordingly
        #else update the value after 4th place

        result = [''] * len(score)

        sortedScores = sorted(score, reverse = True)

        for idx, val in enumerate(sortedScores):
            orgIdx = score.index(val)
            if idx == 0:
                result[orgIdx] = 'Gold Medal'
            elif idx == 1:
                result[orgIdx] = 'Silver Medal'
            elif idx == 2:
                result[orgIdx] = 'Bronze Medal'
            else:
                result[orgIdx] = str(idx + 1)
        return result

        import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)
        
        result = [""] * len(score)
        rank_names = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

        rank = 1
        while heap:
            val, idx = heapq.heappop(heap)
            if rank <= 3:
                result[idx] = rank_names[rank - 1]
            else:
                result[idx] = str(rank)
            rank += 1
        return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #receive a list of integers
        #return top k elements

        #brute force: create a frequency counter
        #sort by values
        #return top k keys

        numsCount = {}
        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1
        
        sorted_counts = sorted(numsCount.items(), key=lambda x:x[1])

        return sorted_counts[0][:k]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res
  
  
  class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #intiialize counter
        #keep track of count
        #create buckets
        #add in the key into the buckets of their values
        #iterate through buckets from right to left
        #add in value into results array
        #return result if length == k

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        buckets = [[] for num in range(len(nums) + 1)]

        for key, value in counter.items():
            buckets[value].append(key)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for i in buckets[i]:
                res.append(i)
                if len(res) == k:
                    return res

  
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        #add in value to the end
        #sort the value
        #return the largest k

        self.nums.append(val)
        self.nums.sort(reverse = True)
        return self.nums[self.k -1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

def count_sheep(n):
    #receive an for integers
    #return a string of up to n sheep
    #ex: 0 => ''
    
    #ex: 5 => '1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...'
    
    #edge case:
    #if n == 0, return ''
    
    #initialize an empty string
    #iterate up to n:
    #for every number, return the number + sheep...
    #return the string back
    
    if n == 0:
        return ''
    
#     output = ''
#     for num in range(1, n+ 1):
#         output += f"{num} sheep..." #'1 sheep...2 sheep...'
#     return output

#time: O(n^2) for each num in n
#space: O(n) create output string

    output = [f"{num} sheep..." for num in range(1, n+1)]
    return ''.join(output)

#time: O(n)
#space: O(n)

    
    