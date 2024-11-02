function twoNumberSum(array, targetSum) {
  //receive an array of integers
  //return the two values in an array that totals up to targetSum
  //ex: [1, 3, -2, 4], -1 => [1, -2]

  //iterate through the array with one pointer
  //iterate through the rest of the array with a second pointer
  //if the total matches up to targetSum
  //return the two values in an array

  // for (let i =0; i < array.length; i++) {
  //   for (let j = i + 1; j < array.length; j++) {
  //     if (array[i] + array[j] === targetSum) {
  //       return [array[i], array[j]]
  //     }
  //   }
  // }
  // return []

  //time: O(n^2);
  //space: O(1)

  //optimized: use an object to store the values
  //iterate through the array of integers
  //look at the difference between target and the current integer value
  //if the obj, has the difference
  //return the difference and the current value of pointer
  //else set the value in the object

  let valueObj = {};

  for (let i = 0; i < array.length; i++) {
    let difference = targetSum - array[i];
    if (valueObj.hasOwnProperty(difference)) {
      return [array[i], valueObj[difference]];
    } else {
      valueObj[array[i]] = array[i];
    }
  }
  return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;
