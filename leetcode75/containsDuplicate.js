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
    // for (let i = 0 ; i < array.length; i++) {
    //     for (let j = i + 1; j < array.length; j++) {
    //         if (array[i] === array[j]) {
    //             return true;
    //         }
    //     }
    // }
    // return false;

//optimized: 
//could use a Set
//iterate and check if Set already has element, if so, return true;
//else return false after checking Set
//time: O(n)
//space: O(n) //creating new Set for every element in the Set

// let setArray = new Set(array); //would not use this b/c we want to store the element into Set

// let setArray = new Set(); 

// for (const element of array) {
//     if (setArray.has(element)) {
//         return true
//     } else {
//         setArray.add(element)
//     }
// }
// return false;

//object

let newObject = {};

for (const element of array) {
    if (!newObject[element]) {
        newObject[element] = (1 || 0) + 1
    }
    
    if(newObject[element] < 2) {
        return true
    }
    console.log(newObject, newObject[element])
    return false
}

// let results = {};

// for (let num of array) {
//     //if object has it already, return true;
//     if (results[num]) {
//         console.log(results[num])
//         return true
//     } else {
//         //else set it to true
//         results[num] = true; //set the value to true
//     }
//     console.log(results)
// }
// return false;

}

// console.log(containDup([1,2,-1, -1]))
console.log(containDup([1,2,-1, 3]))