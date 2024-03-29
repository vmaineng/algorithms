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

    //brute force; 
    //use triple nested loops
    //make sure the numbers do not equal each other
    //push them into an array to be pushed into the final result

    // let result = [];
    
    // for (let i = 0; i < nums.length; i++) {
    //     for (let j = i + 1; j < nums.length - 1; j++) {
    //         for (let k = j + 1; k < nums.length - 2; k++) {
    //             if (nums[i] !== nums[j] !== nums[k])
    //         }
    //     }
    // }

    //edge case - if all numbers in array are the same, can't find solution then

//optimized approach: 
//initialize an [] to capture the results;
//sort the elements
//have a pointer on the first index;
//have a poitner next to it and pointer at the end; 

//time: O(n^2)
//space: O(n) b/c of creating new array

let result = [];
nums = nums.sort((a,b) => a - b)

let target = 0;

for (let i = 0; i < nums.length - 2; i++) {
    // if (nums[i] > target) break;
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1
    while ( left < right) {
        let sum = nums[i] + nums[left] + nums[right]
        // console.log([nums[i], nums[left], nums[right]])
        if (sum === target) {
            result.push([nums[i], nums[left], nums[right]])
           // console.log([nums[i], nums[left], nums[right]])
            while (nums[left] === nums[left+1]) left++;
            while (nums[right] === nums[right - 1]) right--;
            left++;
            right--;
        } else if (sum < target){
            left++
        } else {
            right--;
        }
    }
}
return result;

}

console.log(threeSum([-1,0,1,2,-1,-4]))


// * start with the first element and use two pointers with left and right 