//given an array of integers, rreturn
//ex: [100, 1, 4, 3, 7, 2, 5] => 5
//[1,2,3,4,5, 7, 100]

//off by one error;
//assume it's only positive numbers
//receive an array of integers of positive numbers
//return the max length of continguous numbers (an integer)
//  1 , 2,
//ex: [3, 4, 2, 6] => [2, 3, 4, 6];3; count = 3
//           i  j

//ex: [2, 3, 4, 6, 8, 10]
//     i
//       j
//ex: [2, 4, 5, 6, 7, 8]
//ex: [2, 3, 4, 8, 9, 10, 11, 12, 13, 14]

//[2, 3, 4]
//   i
//     i +1
// ! come up with more test cases than 3
//all unique numbers

//edge case: if the array is empty, return 0;  // ! what happens at the end of the loop; //edge cases are already embedded in the code
// if the array has only one element, return the array's length

//define a global currentLength variable at 1
//maxLength variable it will be 0
//sort the array by smallest to biggest
//iterate through with the first pointer pointing at the first value
//create another point to check the second value
//check the second value +1 than the first value
//increment currentLength
//else
//capture the current length
//update the maxLength - maxLength, currentLength
//return the maxlength

//there is an O(n) solution - marking the number as negative and they are unique: Use a set (this is in leetcode75) - if (!num.has(num-1))

function maxConsecutive(nums) {
  let currentLength = 0;
  let maxLength = 0;

  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] + 1 === nums[i + 1]) {
      console.log(nums[i], nums[i + 1]);
      currentLength++;
    } else {
      maxLength = Math.max(currentLength + 1, maxLength);
      currentLength = 0;
    }
  }
  return maxLength;
}

console.log(maxConsecutive([2, 3, 4, 8, 9, 10, 11, 12, 13, 14]));

//ppl care more about time complexity
