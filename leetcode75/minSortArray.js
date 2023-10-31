// 153. Find Minimum in Rotated Sorted Array

// Suppose an array of length n sorted in 
// ascending order is rotated between 1 and n times. For example,
//  the array nums = [0,1,2,4,5,6,7] might become:

// [4,5,6,7,0,1,2] if it was rotated 4 times.
// [0,1,2,4,5,6,7] if it was rotated 7 times.
// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 
// 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

// Given the sorted rotated array nums of unique elements, 
// return the minimum element of this array.

// You must write an algorithm that runs in O(log n) time.

// Example 1:

// Input: nums = [3,4,5,1,2]
// Output: 1
// Explanation: The original array was [1,2,3,4,5] rotated 3 times.

const findMin = (nums) => {
//an array of integers, negative and positive
//return the min element value
//might have to rotate to get a sorted array
//[-3, 0, 5, 8, -5] => min = -5

//keep rotating array
//keep track of min element seen
//check to see if this is smaller than the last value we've seen
//update min
//return min

//edge cases, if array is one, then return that value
//if array only has two, check the values against each other
//and return the min value

if (nums.length === 1) return nums[0];

if (nums.length === 2) return Math.min(nums[0], nums[1]);

//O(n log n)time = binary search

let res = nums[0]

let left = 0; 
let right = nums.length - 1; 

while (left <= right) {
    let middle = Math.floor((left + right) /2)
    res = Math.min(res, nums[middle])

    if (nums[middle] >= nums[left]) {
        l = m + 1

    } else if (nums[middle] < nums[right]) {
        r = m - 1
    } else {

    }
}



}

console.log(findMin([-3, -5]))