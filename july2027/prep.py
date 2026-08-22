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

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        postorder(root)
        return result

    class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, second-first)
        return stones[0]

    class Solution:
    def isPalindrome(self, s: str) -> bool:
        #receive a string of letters spaces and chars
        #return boolean if palindrome, else False
        #ex: 

        # result = []
        # for char in s:
        #     if char.isalpha():
        #         result.append(char.lower())
        # modifiedWord = ''.join(result)
        # return modifiedWord == modifiedWord[::-1]

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -=1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1
        return True


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit = 0
        # for buy in range(len(prices)):
        #     for sell in range(buy +1, len(prices)):
        #         profit = prices[sell] - prices[buy]
        #         maxProfit = max(maxProfit, profit)
        # return maxProfit

        maxProfit = 0
        buy = 0 
        for sell in range(len(prices)):
            profit = prices[sell]-prices[buy]
            maxProfit = max(maxProfit, profit)
            if prices[sell] < prices[buy]:
                buy = sell
        return maxProfit

    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxProfit = 0
        # for buy in range(len(prices)):
        #     for sell in range(buy +1, len(prices)):
        #         profit = prices[sell] - prices[buy]
        #         maxProfit = max(maxProfit, profit)
        # return maxProfit

        maxProfit = 0
        buy = 0 
        sell = 1

        while sell < len(prices):
            diff = prices[sell]- prices[buy]
            if diff > 0:
                maxProfit = max(maxProfit, diff)
            
            if prices[buy] > prices[sell]:
                buy +=1
                sell +=1
            else:
                sell +=1
        return maxProfit

    class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #receive a m x n grid
        #return the count of perimeter
        #ex: 

        count = 0 
        visited = set() 

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                        return 1
            if (row,col) in visited:
                return 0
                    
            visited.add((row, col))

            perim = dfs(row + 1, col) + dfs(row-1, col) + dfs(row, col + 1) + dfs(row, col -1)
            return perim

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return dfs(row, col)
       
        return 0

            class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #receive a list of integers
        #return boolean if can pay all customers, else false

        #iterate through the list of bills
        #check if the amount is 5
        #if not, check then check if any money is left on stack
        #, can we use that for chagne, if so, then give to them
        #iterate through back

        if bills[0] != 5:
            return False

        stack = []

        for num in bills:
            if num == 5:
                stack.append(5)
            else:
                if stack and num - stack[-1] > 0:
                    stack.pop()
                    stack.append(num)
                else:
                    return False
        return len(stack) == 0

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -=1
                ten +=1
            else:
                if five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

    class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #receive a list of integers
        #return the weight of stone left after crushing them all else return 0

        #find top two max stones
        #and remove from list
        #then add back their difference

        

        while len(stones) > 1:
            stones.sort()
            first = stones.pop()
            second = stones.pop()
            diff = first - second
            if diff > 0:
                stones.append(diff)
        return stones[0] if stones else 0

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #receive a list of integers
        #return the index position of where two values are equal to each other
        #ex: 

        # for i in range(len(nums)-1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return -1

        seen = { }

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
    

        class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return word[:i]
        return strs[0]
        
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())
        
        while len(tmp):
            self.stack.append(tmp.pop())
        return mini


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[len(self.nums)-self.k]

    class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #receive a list of changes
        #return true if can make change for all of them, else False
        #ex: [10, 5 , 20] => False, b/c no change for a drink

        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else: #20
                if five >= 3:
                    five -= 3
                elif five > 0 and ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    return False
        return True

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0
        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, profit)
            if prices[sell] <prices[buy]:
                buy = sell
        return maxProfit

    class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #receive a list of integers
        #return a boolean if two same values are == to each other and close to each other, else false
        seen = set()
        left = 0
        for right in range(len(nums)):
            if nums[right] in seen:
                return True
            seen.add(nums[right])

            if right - left >= k:
                seen.remove(nums[left])
                left += 1
        return False

    class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0

            visited.add((row, col))
            
            size = dfs(row + 1, col) + dfs(row -1, col) + dfs(row, col + 1) + dfs(row, col -1)
            return size

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    return dfs(row, col)

        return 0

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perim += 4

                    if row > 0 and grid[row-1][col] == 1:
                        perim -= 2
                    
                    if col > 0 and grid[row][col-1] == 1:
                        perim -=2 

        return perim

def neutralise(s1, s2):
    #receive a string of + and -
    #return a new string of the output
    #ex: '--', '--' = '--'
    
    #initialize an empty string
    #keep a pointer on both
    #check what the signs are
    
    result = ''
    
    for i in range(len(s1)):
        if s1[i] == '-' and s2[i] == '-':
            result += '-'
        elif s1[i] == '+' and s2[i] == '+':
            result += '+'
        else:
            result += '0'
    return result


    def eval_object(v):
    match v["operation"]:
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 1

        class Hero(object):
    def __init__(self, name = "Hero"):
        self.name = name
        self.experience = 0
        self.health = 100
        self.position = '00'
        self.damage = 5

        class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        if self.lives < 1:
            raise ValueError("OOM")
            
        if n == self.number:
            return True
        
        if n != self.number:
            self.lives -= 1
            return False


            def two_highest(arg1):
#     arg1.sort()
#     max1 = arg1[-1]
#     max2 = arg1[-2]
# #     for i in range(len(arg1)-1, -1, -1):
# #         print(arg1[i])
# #         max2 = arg1[i]

#     if max2 == max1:
#         return max2 = arg1[-3]
        
#     return [max1, max2]

    #receive a list of integers
    #return the biggest and second biggest
    #ex: [15, 20, 20, 17] => 20 , 17
    
    #sort them, grab the inters
    #if they are the same
    
    if not arg1:
        return []
    
    if len(arg1) == 1:
        return [arg1[0]]
    
    arg1.sort()
    max1 = arg1[-1]
    max2 = arg1[-2]
    if max1 == max2:
        max2 = arg1[-3]
    return [max1, max2]

def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]

def merge_arrays(first, second): 
    #receive two lists of integers
    #return one list sorted integers
    #ex: 
    
    #intialize an empty result
    #iterate through the lists at same time
    #check if the numbers is less, add it from the first one, else add from second
    #then if same number, continue
    
    result = []
    for idx in range(len(first)):
        if first[idx] == second[idx]:
            result.append(first[idx])
        elif first[idx] < second[idx]:
            result.append(first[idx])
            result.append(second[idx])
        else:
            result.append(second[idx])
            result.append(first[idx])
    return result


        def merge_arrays(first, second): 
    #receive two lists of integers
    #return one list sorted integers
    #ex: 
    
    #intialize an empty result
    #iterate through the lists at same time
    #check if the numbers is less, add it from the first one, else add from second
    #then if same number, continue
    
#     result = []
#     for idx in range(len(first)):
#         if first[idx] == second[idx]:
#             result.append(first[idx])
#         elif first[idx] < second[idx]:
#             result.append(first[idx])
#             result.append(second[idx])
#         else:
#             result.append(second[idx])
#             result.append(first[idx])
#     return result

    result = first + second
    return sorted(set(result))

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #receive a string with chars
        #return boolean if valid palindrome

        #ex: 

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1
        return True


            class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        left = 0

        for right in range(len(nums)):
            if nums[right] in seen:
                return True
            seen.add(nums[right])

            if right - left >= k:
                seen.remove(nums[left])
                left += 1
        return False

    class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #receive a list of two integers
        #return the last weight of remaining stone

        #iterate and pop off the last two biggest
        #add their weight back on 
        #resort
        
        while len(stones) > 0:
            stones.sort()
            first = stones[-1]
            second = stones[-2]
            diff = first - second
            if diff:
                stones.append(diff)
        return stones[0] if stones else 0

    """
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #receive a list of tuples
        #return True if can attend all meetings, else False
        #ex: 

        #sort by start time for all of them
        #iterate through the second interval
        #compared start time of second interval with last's end time
        #if they conflict, return False
        #else return True


        intervals.sort(lambda=key x:x[0])

        for interval in range(len(intervals)):
            if interval[i][1] >= interval[i + 1][0]:
                return False
        return True

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        seen = set()
        for right in range(len(nums)):
            if nums[right] in seen:
                return True
            seen.add(nums[right])

            if right - left >= k:
                seen.remove(nums[left])
                left +=1
        return False

    class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right: 
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -=1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1 
        return True

    class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        def explore(graph, node, visited):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                explore(graph, neighbor, visited)
            return True

        graph = build_graph(edges)
        visited = set()

        count = 0

        for node in graph:
            if explore(graph, node, visited) == True:
                count += 1
        return count
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        
        def explore(graph, node, visited):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in graph[node]:
                explore(graph, neighbor, visited)
            return True

        count = 0
        visited = set()
        graph = build_graph(edges)

        for node in graph:
            if explore(graph, node, visited) == True:
                count += 1
        return count
        

       class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n -1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -=1
            else:
                nums1[last] = nums2[n-1]
                n -=1

            last -=1
        while n > 0:
            nums1[last] = nums2[n-1]
            n -=1
            last -=1
            

def find(roots, node):
  if roots[node] == node:
    return node
  return find(roots, roots[node])


def union(roots, node_a, node_b):
  root_a = find(roots, node_a)
  root_b = find(roots, node_b)

  if root_a == root_b:
    return 
  roots[root_b] = root_a

def count_components(n, edges):
  roots = [i for i in range(0, n)]

  for edge in edges:
    node_a, node_b = edge
    union(roots, node_a, node_b)
  count = 0
  for i in range(0, n):
    if roots[i] == i:
      count += 1
  return count

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
        return stack


        def find(roots, node):
  if roots[node] == node:
    return node
  return find(roots, roots[node])

def union(roots, a, b):
  root_a = find(roots, a)
  root_b = find(roots, b)
  if root_a == root_b:
    return node

  roots[root_b] = root_a

def count_components(n, edges):
  #receive nodes, and list of edges
  #return count of components 
  #ex: 

  #create a roots list
  #iterate through the list
  #find their parent nodes
  #update it accordingly in the roots list

  roots = [i for i in range(0, n)]

  for a,b in edges:
    union(roots, a, b)

  count = 0
  for i in range(len(roots)):
    if roots[i] == i:
      count += 1
  return count


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i in range(len(strs[0])):
            for word in strs:
                if i > len(word) or word[i] != strs[0][i]:
                    return word[:i]
        return strs[0]
                
def is_opposite(s1,s2):
    #receive two strings
    #return a boolean if they are the opposite of each other, else, return False
    #ex: 'HI', 'hi' => True; 'hi', 'HI' => True
    
    if len(s1) == 0 and len(s2) == 0:
        return False
    
    if len(s1) != len(s2):
        return False
    
    for a,b in zip(s1,s2):
        if a.isupper() == b.isupper():
            return False
        
    return True

from preloaded import FIRST_NAME, SURNAME

def alias_gen(f_name: str, l_name: str) -> str:
    #receive a string for first name and last name where first character is capitalized
    #return a first name and last name nicknamed
    #ex: 'Mary', 'Berry' => 'Malware', 'Beta'
    
    #if the first character if each name is not a letter, then return 'Your name must start with a letter from A - Z.'
    #if the first name is not capitalize, uppercase the first character
    #match the charcter from first name first char, return that as first nick name
    #do the same for surname as well
    #joined the two names together 
    
    if not f_name[0].isalpha() or not l_name[0].isalpha():
        return 'Your name must start with a letter from A - Z.'
    
    first_name = FIRST_NAME[f_name[0].upper()]
    last_name = SURNAME[l_name[0].upper()]
    return first_name +' ' + last_name

class Solution:
    def integerBreak(self, n: int) -> int:
        #receive an integer
        #return the max product you get (multiply)
        #ex: 4
        #output divided by something to get an equal amount of numbers
        #12 / 4 => 3  ( 3 * 3 * 3 * 3) => 81
        # 12/. 2 => 6  (6 +6) => 36
        # 12/ 6 => 2 (2 + 2 + 2 + 2+ 2 + 2 ) => 48 
        #12 /12 => (1 + 1 + 1)

        #output % each individual even numbers, 
        #we are going to check to see the output * divisior >= max
        #if so, update our max
        
        max_value= float("-inf")

        for num in range(2, n + 1): # 2, 12, ; skip by 2; 3, 
            if n % num == 0: #12 / 2 == 0; 12 /3 == 0; 
                divisor = n / num # 12 / 2=> 6 ; 12 / 3 => 4
                # value = divisor * num # 6 * 2 => 12;  4 * 3
                total = 1
                while divisor > 0: # 3
                    print(total)
                    total *= num # 3 * 1 => 3, 3 * 3 
                    divisor -= 1 # 3
                max_value = max(total, max_value)
            else:
                continue

        return max_value

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #receive a list of stones
        #return the last remaining stone
        #else 0

        #iterate through and knock off the two highest ones
        #resort it

        while len(stones) > 1:
            stones.sort()
            diff = stones.pop() - stones.pop()
            # first = stones.pop()
            # second = stones.pop()
            if diff:
                stones.append(diff)
        return stones[0] if stones else 0

def cannons_ready(gunners):

    nay_count =0
    for name in gunners:
        if gunners[name] == 'nay':
            nay_count += 1
  
            
    return 'Shiver me timbers!' if nay_count >= 1 else 'Fire!'

return 'Shiver me timbers' if 'nay' in gunners.values() else 'Fire!'

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time: O (Nlogn) nums.sort()

        #start with two pointers
        #left and right
        #compare the value

        #or insertion sort
        #start with first value
        #check with next value
        #iterate through entire list until it's sorted


        count = [0] * 3
        for num in nums:
            count[num] += 1

        idx = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[idx] = i
                idx += 1
            

        from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #receive a list of integers
        #return top k elements

        #keep track of count
        #sort by values 
        #return top k

        count = Counter(nums)

        return [num for num, freq in count.most_common(k)]


from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #receive a list of integers
        #return top k elements

        #keep track of count
        #sort by values 
        #return top k

        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #receive a list of integers
        #return the max profit gained by buying and selling multiple times
        #ex: [7,1,5,3,6,4]
        #.    b s
        #.      b s

        #start off of with first item
        #iterate through and check if the next day's price is than current price
        #buy on low price, sell on high, check the profit
        #add to maxprofit seen

        maxprofit = 0

        buy = 0

        for sell in range(len(prices)):
            if prices[buy] < prices[sell]:
                print(prices[sell], prices[buy])
                profit = prices[sell] - prices[buy]
                maxprofit += profit
                buy += 1
            else:
                buy = sell
        return maxprofit

        from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #receive a list of nums
        #return the nums that exceeds more than len(n) / 3

        #iterate through the list of integers
        #keep count of it
        #check if the amount they have >= len(n) / 3
        #if so add in a the result list


        result = []

        count = Counter(nums)
        check = len(nums)/ 3

        for key, val in count.items():
            if val > check:
                result.append(key)
        return result

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #receive a list of integers
        #return the max amount of water a container can store
        #ex: 

        #iterate through starting with o(n^2) operation to test all operations out to find max
        #else do it with sliding window
        #start from left and right


        left = 0
        right = len(heights) - 1
        maxHeight = 0

        while left <= right:
            minHeight = min(heights[left], heights[right])
            height = minHeight * (right -left)
            maxHeight = max(maxHeight, height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return maxHeight

    def has_path(graph, src, dst):
  if src == dst:
    return True

  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst):
      return True
  return False



from collections import deque

def has_path(graph, src, dst):
  queue = deque([src])

  while queue:
    current = queue.popleft()
    if current == dst:
      return True

    for neighbor in graph[current]:
      queue.append(neighbor)
  return False
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #receive a list of integers
        #return max profit seen from selling and buying continuously
        #ex:

        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] -prices[i - 1]
        return maxProfit
        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square //3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
                


        from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time: O (Nlogn) nums.sort()
        #iterate through the array
        #keep count
        #start placing the values at the specific spots at 

        count = Counter(nums)

        idx = 0

        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[idx] = i
                idx += 1


def undirected_path(edges, node_A, node_B):
  graph = build_edges(edges)
  visited = set()

  return has_path(graph, node_A, node_B,visited)



def build_edges(edges):
  graph = {}

  for a,b in edges:
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    graph[a].append(b)
    graph[b].append(a)
  return graph

def has_path(graph, node_A, node_B, visited):

  if node_A == node_B:
    return True
    
  if node_A in visited:
    return False

  visited.add(node_A)


  for neighbor in graph[node_A]:
    if has_path(graph, neighbor, node_B, visited):
      return True
  return False
        

        def connected_components_count(graph):
  #receive a graph
  #return connected connected_components_count
  #ex: 

  #iterate through the edges
  #track visited
  #if node in visitied, return False

  count = 0
  visited = set()

  for node in graph:
    if has_path(graph, node, visited) == True:
      count += 1
  
  return count

def has_path(graph, node, visited):
  if node in visited:
    return False

  visited.add(node)

  for neighbor in graph[node]:
    has_path(graph, neighbor, visited)
      
  return True

def largest_component(graph):
  visited = set()
  count = 0
  largestCount = 0

  for node in graph:
    count = explore(graph, node, visited)

    if count > largestCount:
      largestCount = count

  return largestCount


def explore(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)

  size = 1

  for neighbor in graph[node]:
    size += explore(graph, neighbor, visited)

  return size  
    

        