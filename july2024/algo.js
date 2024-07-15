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
