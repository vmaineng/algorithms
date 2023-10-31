// 33. Search in Rotated Sorted Array

// There is an integer array nums sorted in 
// ascending order (with distinct values).

// Prior to being passed to your function, 
// nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
// such that the resulting array is [nums[k], nums[k+1], ..., 
// nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, 
// [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

// Given the array nums after the possible rotation and an integer target, r
// eturn the index of target if it is in nums, or -1 if it is not in nums.

// You must write an algorithm with O(log n) runtime complexity.


// Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4

//brute force - check if each position is our target = O(n) time


//O (log n) time - binary search

const searchSorted = (nums, target) => {
//get an array of integers in ascending order & unique (which could be rotated), target = integer
//return the index or -1 if can't find it
//[-4, -3, 0, 4, 5, -5], 4 => 3 = index of 4

//initialize a left pointer at beginning
//initialize a right pointer at end
//iterate through to make sure left and right pointer do not cross
//check to see if middle is the target,
//if so, return the index
//if not middle index, if the target is smaller than middle index,
//move right pointer
//else move left pointer
//return -1 if can't find index

let left = 0;
let right = nums.length - 1; 

while (left < right) {
    let middle = Math.floor ((left + right) / 2)

    if (nums[middle] === target){
        return middle
    } else if (nums[middle] > target) {
        left = middle + 1
    } else {
        right =middle - 1
    }
}
return - 1;

}

console.log(searchSorted([-4, -3, 0, 4, 5, -5]))