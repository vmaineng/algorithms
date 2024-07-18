function kadanesAlgorithm(array) {
  // Write your code here.

  //receive an array of integers
  //return the max total
  //[1, -4, 3, 2] => 5 (3 + 2)

  //keep track of maxSum;
  //keep track of maxNumber
  //iterate through and grab each max total
  //if the maxsum < the next number, start a new total with the next number
  //return maxsum

  let maxSum = array[0];
  let maxNumber = array[0];

  for (let i = 1; i < array.length; i++) {
    maxSum = Math.max(array[i], maxSum + array[i]);
    maxNumber = Math.max(maxNumber, maxSum);
  }
  return maxNumber;
}

// Do not edit the line below.
exports.kadanesAlgorithm = kadanesAlgorithm;

function twoNumberSum(array, targetSum) {
  //receive an array of integers (pos and neg), and a target sum (integer) to reach
  //return the two values that adds up to targetSum in an array

  //[3, -3, -2, -4, 6], -6 => [-2, -4]

  //edge case if array is empty
  //need to make sure sum is two differente integers

  //iterate through the array
  //create another pointer to point to the next value
  //if you find the first instance and they are not of the same value
  //return the values

  if (!array) return [];

  for (let i = 0; i < array.length; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[i] + array[j] === targetSum) {
        return [array[i], array[j]];
      }
    }
  }
  return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;

function moveElementToEnd(array, toMove) {
  //receive an array of integers, and an integer to identify which number to move
  //return an array of integers back with all the elements === toMove towards the end
  //[1,2,3,1,4],1 => [2, 3, 4 1, 1]

  //edge cases: if array is empty

  //initialize a pointer at starting index
  //initialize a pointer at end of array
  //check if the value at beginning of array is equal toMove
  //swap the value
  //then increment left point, decrement right pointer
  //return array

  //time: O(n) - iterating through array once
  //space: O(1) - doing it in place

  if (array.length === 0) return [];

  let left = 0;
  let right = array.length - 1;

  while (left < right) {
    while (left < right && array[right] === toMove) {
      right--;
    }
    if (array[left] === toMove) {
      let temp = array[left];
      array[left] = array[right];
      array[right] = temp;
    }
    left++;
  }
  return array;
}

// Do not edit the line below.
exports.moveElementToEnd = moveElementToEnd;
