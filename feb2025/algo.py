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

            