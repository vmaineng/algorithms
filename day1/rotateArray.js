// Given an input Array, rotate k units clockwise, i.e. 
// shift the values rightward k units.

// k is an Integer >= 0.

function rotateArray(array, k) {
//receives an array of integers > 0, an integer stating how many rotations are made
//return the new rotated array
//[1,2,3,4], 7 => [4,1,2,3], [3,4,1,2], [2,3,4,1], [1,2,3,4], [4,3,2,1],[3,4,1,2], [2,3,4,1] => [2,3,4,1] 

//identify the rotations
//splice out the certain part of it, and add it back together

const rotations = k % array.length;
const removed = array.splice(array.length - rotations, rotations)
// console.log(removed, array.length - rotations, rotations) //[4], 2, 1

return removed.concat(array)

}

console.log(rotateArray([1,2,3,4], 1))