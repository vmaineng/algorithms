// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

// Example 1:

// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

const longestConsecutive = (nums) => {
//parameter of nums, an unsorted array of integers
//return longest length of consecutive numbers
//[3,5,435,6,6,2,2,32,121] => 2 b/c of 2,3

//brute force
//sort the array 
//initialize a count to keep track of max length;
//initialize a temp count to keep track of the highest amount temporarily

//iterate through the array to check if the value at the index is equal to the 
//check to see if the number before value exists,
//if so, add to count
//check to see if number after exists,
//add to count
//otherwise reset count to 1;

//time: O(n log n) b/c using sort
//space: O(1) b/c using the same space and not creating new one

// nums.sort((a,b) => a - b); 

// let count = 0;
// let temp = 1; //set it to 1 b/c it captures at least the first beginning element

// for (let i = 0; i < nums.length; i++) {
//     if (nums[i] === nums[i + 1] - 1) { //if the number in front of the current index is before the value, count it
//        console.log(nums[i], nums[i+1], nums[i + 1] -1)
//         temp++;
//         count = Math.max(temp, count);
//     } else if (nums[i] === nums[i + 1]) {
//         count = Math.max(temp, count);
//     } else {
//         temp = 1; 
//         count = Math.max(temp, count);
//     }
// }

// return count; 


//optimized method: 
//use a Set to iterate through the array to remove duplicates
//iterate and check to see if Set has previous and the after number
//increase count if found
//time: O(n)
//space: O(n) b/c using a set for as long as the input is




}

console.log(longestConsecutive([1,2,2,2,3]))