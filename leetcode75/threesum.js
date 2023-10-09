// Given an integer array nums, return all the 
// triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, 
// and j != k, and nums[i] + nums[j] + nums[k] == 0.

// Notice that the solution set must not contain duplicate triplets.

 

// Example 1:

// Input: nums = [-1,0,1,2,-1,-4]
// Output: [[-1,-1,2],[-1,0,1]]
// Explanation: 
// nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
// nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
// nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
// The distinct triplets are [-1,0,1] and [-1,-1,2].
// Notice that the order of the output and the order of the triplets
//  does not matter.


const threeSum = (nums) => {
    //an array of unsorted nums - positive and negative
    //return all triplets that sums the target of 0 and all of must be unique numbers; 
    //[0,1,2,-5, 4] => [-5, 1, 4]

    //edge case - if all numbers in array are the same, can't find solution then

}

console.log(threeSum([]))