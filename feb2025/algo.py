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
        
            