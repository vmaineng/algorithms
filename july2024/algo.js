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

function twoNumberSum(array, targetSum) {
  //receive an array of integers (pos and neg), targetSum (an integer)
  //return an array back of the two values
  //[2, 3, 5, 1], 4 => [3, 1]

  //if array is empty, return empty array

  //create an object
  //iterate through array, put the value seen as value in obj
  //check if the difference exists in obj,
  //return it
  //else store it

  if (array.length === 0) return [];

  let seenVals = {};

  for (let i = 0; i < array.length; i++) {
    let difference = targetSum - array[i];
    if (seenVals.hasOwnProperty(difference)) {
      return [seenVals[difference], array[i]];
    } else {
      seenVals[array[i]] = array[i];
    }
  }
  return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;

function binarySearch(array, target) {
  //receive an array of sorted integers and a target number
  //return the index if the target value is found in the array, else return -1;

  //[3, 5, 6, 8, 11, 15, 23], 3 => return index 0

  //edge case: if array is empty

  //binary search algo
  //capture left(start of index) and right(end of the array) pointer
  //calc middle index, check the value
  //if the value does not equal target, check if the target is less than the middle value
  //move right pointer down
  //else if the value is greater than middle value, move left pointer up
  //else return -1;

  if (array.length === 0) return -1;

  let left = 0;
  let right = array.length - 1;

  while (left <= right) {
    let middle = Math.floor((left + right) / 2);
    if (array[middle] === target) {
      return middle;
    } else if (array[middle] > target) {
      right--;
    } else {
      left++;
    }
  }
  return -1;
}

// Do not edit the line below.
exports.binarySearch = binarySearch;

function shiftedBinarySearch(array, target) {
  //receive an array that has been shifted and a number integer target
  //return index of the target if found in the array, else return -1;
  //[1, 2, 3, 4, 5] => shifted [3, 4, 5, 1, 2], 2 => index 4

  //edge case: if array is empty, return -1

  //set up the binary algo
  //difference is add another if stmt to check if the left value is < middle idx
  //if not, return -1;

  //same set up for the right value too

  if (array.length === 0) return -1;

  let left = 0;
  let right = array.length - 1;

  while (left <= right) {
    let middleIdx = Math.floor((left + right) / 2);
    if (array[middleIdx] === target) {
      return middleIdx;
    } else if (array[left] <= array[middleIdx]) {
      // know the array is still sorted
      if (target < array[middleIdx] && target >= array[left]) {
        //check if the value is less than middleIdx value and greater than the left value
        right = middleIdx - 1;
      } else {
        left = middleIdx + 1;
      }
    } else {
      if (target > array[middleIdx] && target <= array[right]) {
        left = middleIdx + 1;
      } else {
        right = middleIdx - 1;
      }
    }
  }
  return -1;
}

// Do not edit the line below.
exports.shiftedBinarySearch = shiftedBinarySearch;