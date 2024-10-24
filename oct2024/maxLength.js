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

console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));
