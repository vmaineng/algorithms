# track population growth of small towns
#write function that is take in initial population
#percent by what it grows each year
#the augmentation (number of inhabitant comes each year on top of growth)
#population you're trying to get to
#return n -> years from initial to expected goal

#receive an integer for initial population (whole) and goal number (whole)
#receive percent of growth (whole or float ex: 2 or 2.5,13.25/100), the augementation (whole/year)
#4 inputs - growth (positive numbers only)
#return an integer for the years to get from initial to expected

#ex: (initial, percent, augmentation, target)
#ex:  (100,      10  , 50      ,     200)   

#while our target has not been reached
#calculate first year's goal => (100 * .10) + 50 => 110 + 50 => 160.2 (round down)
#increment a count for the year
#second: (160 *.10 ) + 50 => (160 + 16) + 50 => 176 + 50 =. 226
#return 2

#calculate first year's goal => (100 * .025) + 50 => 175

import math

def trackPopulation(initial, percent, augmentation, target):
    year = 0
    while initial < target: #100 < 200, 160 < 200, 226 
        initial = math.floor((initial * percent) + augmentation) #(100 * .10) + 50 => 160, #226
        year += 1 # year = 2
    return year

# print(trackPopulation(100, 1.1, 50, 200))


# def subK(nums,k):
#     #receive a list of integer nums
#     #return max_sum found that are continguous
#     #ex: [3,4,5], 2 => [4,5] => 9

#     #iterate through nums up to k size
#     #check if sum of them is > max, update max

#     current_sum = sum(nums[0:k])
#     max_sum = current_sum

#     for i in range(len(nums) - k):
#         current_sum += nums[i + k]
#         current_sum -= nums[i]
#         max_sum = max(current_sum, max_sum)
            
#     return max_sum

# # print(subK([2, 1, 5, 1, 3, 2], 3))



# def findMax3(cards, k):
#     #receie a list of cards
#     #return maxSum found
#     #ex:

#     #look at first 3, look at last 3, look at firs tand last 2, look at first 2 and last
#     #compare who has highest score

#     first_three = sum(cards[0:k])
#     last_three = sum(cards[-k:])
#     first_max = max(first_three, last_three)  

#     first_mix = cards[0]+ sum(cards[-2:])
#     second_mix = sum(cards[:2]) + cards[-1]
#     second_max= max(first_mix, second_mix)

#     return max(first_max, second_max)

# print(findMax3([2,11,4,5,3,9,2], 3))

# class Solution:
#     def trappingWater(self, height: List[int]) -> int:
#         left, right = 0, len(height) - 1
#         leftMax = height[left]
#         rightMax= height[right]
#         total = 0

#         while left < right: 
#             if leftMax < rightMax:
#                 left += 1
#                 if height[left] >= leftMax:
#                     leftMax = height[left]
#                 else:
#                     total += leftMax - height[left]
            
#         else:
#             right -=1
#             if height[right] >= rightMax:
#                 rightMax = height[right]
#             else:
#                 total += rightMax - height[right]
#         return total

#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         max_score = score = sum(cardPoints[-k:])
#         n = len(cardPoints)

#         if k == n:
#             return max_score

#         left = 0
#         for right in range(n - k, n):
#             score += cardPoints[left] - cardPoints[right]
#             max_score = max(max_score, score)
#             left += 1
        
#         return max_score


def maxSum(nums, k) -> int:
        #receive a list of integers
        #return the max sum seen for unique vals
        #ex: 

        #iterate up by one to the right
        #if the val is in set already, seen this val before
        #if window size == k, get sum

    unique = set()
    left = 0
    max_sum = 0
    cur_sum = 0

    for right in range(len(nums)):
        while nums[right] in unique:
            unique.remove(nums[left])
            cur_sum -= nums[left]
            left += 1

        unique.add(nums[right])
        cur_sum += nums[right]
        print(unique)


        if len(unique) == k:
            max_sum = max(max_sum, cur_sum)
            unique.remove(nums[left])
            cur_sum -= nums[left]
            left += 1
    return max_sum

#nums: [4,2,4,5,6],    k: 4
#        [.     ]
#
#set: [2, 4, 5, 6 ]

print(maxSum( [1,2,3,4,5], 4))

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        left = 0
        max_sum = float('-inf')
        total = 0

        for right in range(len(nums)): 
            total += nums[right]
            print(total )
            if (right - left) + 1 == k:
                max_sum =max(max_sum, total)
                total -= nums[left]
                left += 1
            

        return max_sum 