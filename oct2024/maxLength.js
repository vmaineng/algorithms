/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  //receive an array of integers unsorted
  //return the longest consecutive elements sequence
  //[3, 4, 5, 6, 2, 3] => 5

  //initialize maxLength at 0 to keep track of longest length
  //sort the elements
  //initialize a current length starting at 1
  //iterate going forward and checking if value is > current one
  //if value is not, then capture maxLength
  //return maxLength

  let maxLength = 0;
  let currentLength = 1;
  //edge case: if nums.length <1, return nums.length
  if (nums.length < 2) return nums.length;

  nums.sort((a, b) => a - b);
  //   console.log(nums);

  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] === nums[i]) continue;

    if (nums[i] === nums[i - 1] + 1) {
      currentLength++;
    } else {
      console.log(nums);
      maxLength = Math.max(maxLength, currentLength);
      currentLength = 1;
      //   console.log(maxLength, currentLength);
    }
  }
  //   console.log(maxLength, currentLength);
  maxLength = Math.max(maxLength, currentLength);
  return maxLength;
};

// console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  //if nums is empty, return empty array
  //create an object to track values seen
  //then get all the values in an array
  //sort by biggest to smallest
  //take the first k elements

  if (nums.length === 0) return [];

  let objSeen = {};
  for (let num of nums) {
    objSeen[num] = objSeen[num] + 1 || 1;
  }
  console.log(objSeen);
  const objSeenArray = Object.entries(objSeen);
  console.log(objSeenArray);

  objSeenArray.sort((a, b) => b[1] - a[1]);
  //   console.log(objSeenArray);
  return objSeenArray.slice(0, k).map((item) => parseInt(item[0]));
};

// console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));

function majorityElement(array) {
  let count = 0;
  let answer;

  //find majority element
  for (const value of array) {
    if (count === 0) answer = value;

    if (value === answer) {
      count++;
    } else {
      count--;
    }
  }

  //check if majority occurs more than half of the length, else return -1
  count = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] === answer) {
      count++;
    }
    if (count > array.length / 2) {
      return answer;
    }
  }
  return -1;
}

// Do not edit the line below.
exports.majorityElement = majorityElement;

function riverSizes(matrix) {
  let arr = [];
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j]) {
        arr.push(explore(i, j, 0, matrix));
        console.log(arr);
      }
    }
  }
  return arr;
}

function explore(i, j, count, matrix) {
  count++;
  matrix[i][j] = 0;

  if (matrix[i][j + 1]) size = explore(i, j + 1, count, matrix);
  if (matrix[i][j - 1]) size = explore(i, j - 1, count, matrix);
  if (matrix[i + 1] && matrix[i + 1][j])
    size = explore(i + 1, j, count, matrix);
  if (matrix[i - 1] && matrix[i - 1][j])
    size = explore(i - 1, j, count, matrix);
  return count;
}

// console.log(
//   riverSizes([
//     [1, 0, 0, 1, 0],
//     [1, 0, 1, 0, 0],
//     [0, 0, 1, 0, 1],
//   ])
// );

function window(length, offset, list) {
  const answer = [];

  for (let i = 0; i + length <= list.length; i += offset) {
    // console.log(length, offset);
    answer.push(list.slice(i, i + length)); // Push a window of exact 'length'
  }

  return answer;
}

// console.log(window(3, 1, [1, 2, 3]));

function twoNumberSum(array, targetSum) {
  //receive an array of integers, return the targetSum
  //return the two numbers that totals up the targetSum, else return an empty array
  //[3, 4, 5, 2, -2], 0 => [2, -2]

  //create an object
  //iterate through the array
  //store the value into the object
  //check if obj has the difference from targetSum - value
  //if not, add in the difference

  if (!array) return [];

  let obj = {};
  for (let i = 0; i < array.length; i++) {
    let difference = targetSum - array[i];
    if (obj.hasOwnProperty(difference)) {
      return [obj[difference], array[i]];
    } else {
      obj[array[i]] = array[i]; //setting the key to the value
      console.log(array[i], obj[array[i]]);
    }
  }
  return [];
}

// Do not edit the line below.
exports.twoNumberSum = twoNumberSum;

// console.log(twoNumberSum([3, 4, 5, 2, -2], 0));

/**
 * @param {number[]} nums
 * @return {number[]}
 */
// var productExceptSelf = function (nums) {
//receive an array of integer
//return a productSum array of integer back

//[3, 2, -1]
//answer = [-2, -3, 6]

//create an answer array
//initialize a multiplier of 1
//iterate through nums array at the first value
//iterate through the nums array with second pointer
//check if i !== j
//multiply the value by the multiplier
//then mutiply the product by the value?
//return answer array

//if nums is empty return []
//if nums array has one value, return []

// if (nums.length < 2) return [];

// let answer = [];

// for (let i = 0; i < nums.length; i++) {
//   let multiplier = 1;
//   for (let j = 0; j < nums.length; j++) {
//     if (i !== j) {
//       multiplier *= nums[j];
//       console.log(multiplier); // 2, 6, 24; then it will start on the next round
//     }
//   }
//   answer[i] = multiplier;
// }

// return answer;
// };

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  //receive an array of integers
  //return the productSum of all nums in the array except product of self
  //[3, 2, -3] => [-6, -9,-6]

  //edge case: if array is empty or has less than one value, return []

  //create an array to hold the answers
  //iterate through nums array with first pointer
  //create a multiplier of 1
  //iterate through the nums array with second pointer
  //check if the pointers do not equal each other
  //then take the mutlipier * value at second pointer
  //afterwards, update the spot of index in answers array
  //return answers array

  // let answer = [];

  // for (let i = 0; i < nums.length; i++) {
  //     let multiplier = 1;
  //     for (let j = 0; j < nums.length; j++) {
  //         if (i !== j) {
  //             multiplier *= nums[j]
  //         }
  //     }
  //     answer[i] = multiplier
  // }
  // return answer

  //O(n^2)
  //space: O(n)

  //optimized:
  //iteraete through array from left to right
  //iterate through array from right to left

  let answer = [];

  let multiplier = 1;
  for (let i = 0; i < nums.length; i++) {
    multiplier *= nums[i];
    console.log(multiplier);
    answer[i] *= multiplier;
  }

  let multiplier1 = 1;
  for (let j = nums.length - 1; j >= 0; j--) {
    // console.log(answer);
    multiplier1 *= nums[j];
    answer[j] *= multiplier1;
  }

  return answer;
};

// console.log(productExceptSelf([1, 2, 3, 4]));

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
  //receive an array of integers (pos and negative), k = integer
  //return an array where it's been shifted by right k times

  //[3, 2, 4], 2 => [2, 4, 3]

  //if array is empty, return an empty array
  //create a new array
  //iterate the array, starting at the end of the array
  //add k amount to it and add into the new array
  //keep going until array is empty

  if (nums.length === 0) return [];

  k = k % nums.length;

  for (let i = 0; i < k; i++) {
    console.log(nums.pop());
    nums.unshift(nums.pop());
  }
  return nums;
  //time: O(n x k) => n is the length of nums and k is the number of rotations
};

// console.log(rotate([3, 2, 4], 2));

/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function (chars) {
  //receive an array of characters,
  //return an array of strings back with it compressed
  //['a','a','b','b','b'] => ['2','a','3','b']

  //if array is empty, return an array of an empty string

  //keep track of an empty string
  //keep count of strings seen
  //iterate through chars
  //check if the next value is still same letter
  //increment count
  //else capture the current value
  //return array of values seen

  let answer = [];
  let i = 0;

  while (i < chars.length) {
    let char = chars[i];
    let count = 0;

    while (i < chars.length && chars[i] === char) {
      i++;
      count++;
    }
    answer.push(char);

    if (count > 1) {
      for (let digit of count.toString()) {
        answer.push(digit);
      }
    }
  }

  for (let j = 0; j < answer.length; j++) {
    chars[j] = answer[j];
  }
  console.log(answer);
  return answer.length;
};

console.log(compress(["a", "a", "b", "b", "b"]));
