// Given an integer array nums, return true if any value appears at least twice in the array, 
// and return false if every element is distinct.

 

// Example 1:

// Input: nums = [1,2,3,1]
// Output: true
// Example 2:

// Input: nums = [1,2,3,4]
// Output: false
// Example 3:

// Input: nums = [1,1,1,3,3,4,3,2,4,2]
// Output: true

//p = receive an array of integers - could be positive and negative
//return true if duplicates
//return false if all unique
//[-1, 5, 3, 2, -1] => true

//BF: double nested loops
//iterate through array
//keep a pointer on first element, second pointer on second element
//if they do equal each other, return true
//else after checking entire array, return false
//time: O(n^2)
//space: O(1)

function containDup(array) {
    for (let i = 0 ; i < array.length; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] === array[j]) {
                return true;
            }
        }
    }
    return false;
}

// console.log(containDup([1,2,-1, -1]))
console.log(containDup([1,2,-1, 3]))