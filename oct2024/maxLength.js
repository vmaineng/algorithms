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
  console.log(nums);

  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] === nums[i]) continue;

    if (nums[i] === nums[i - 1] + 1) {
      currentLength++;
    } else {
      console.log(nums);
      maxLength = Math.max(maxLength, currentLength);
      currentLength = 1;
      console.log(maxLength, currentLength);
    }
  }
  console.log(maxLength, currentLength);
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
  console.log(objSeenArray);
  return objSeenArray.slice(0, k).map((item) => parseInt(item[0]));
};

console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));

function majorityElement(array) {
  //receive an array of integers unsorted
  //return the majority element; appears more than half of its indices
  //[3, 2, 5, 6, 6, 6,3] => -1

  //initialize a frequencyCounter pattern
  //then check which element appeared more than half of the length
  //return the element

  if (array.length === 0) return -1;

  let obj = {};
  let maxVal = 0;
  let maxEle = 0;

  for (let num of array) {
    if (!obj[num]) {
      obj[num] = 0;
    }
    obj[num]++;
  }

  for (let key in obj) {
    if (obj[key] > maxVal) {
      maxVal = obj[key];
      maxEle = parseInt(key);
    }
  }

  if (maxVal > Math.floor(array.length / 2)) {
    return maxEle;
  }
  return -1;
}

// Do not edit the line below.
exports.majorityElement = majorityElement;
