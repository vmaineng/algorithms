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
