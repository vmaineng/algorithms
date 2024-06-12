/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  //receive a string of lowercase letters
  //return longest substring with unique chars
  //'rhinocareus' => 'rhinoca' => 7

  //edge case: if string is empty

  //create a new set
  //keep track of each letter
  //keep extending right side of window until it's no longer unique
  //then push in the left side window
  //keep track of the max Count you've seen
  //return the count

  let uniqueChars = new Set();
  let left = 0;
  let right = 0;
  let count = 0;

  while (right < s.length) {
    if (!uniqueChars.has(s[right])) {
      uniqueChars.add(s[right]);
      right++;
    } else {
      uniqueChars.delete(s[left]);
      left++;
    }
    count = Math.max(count, uniqueChars.size);
  }
  return count;
};

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  //receive a string of opening and closing parens
  //return true if all pairs up together, else false
  //')[]' = false
  //'[(])' => true

  //edge case: if string is empty, return false
  //if string does not start with opening, return false

  //create a stack
  //iterate through the string
  //if it is an opening char, add it to the stack
  //else if it is a closing char, check the stack to make sure it's not empty
  //then pop it off
  //if not, return false

  //else return true

  if (s.length === 0) return false;
  if (s[0] === ")" || s[0] === "]" || s[0] === "}") return false;

  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(" || s[i] === "[" || s[i] === "{") {
      stack.push(s[i]);
    } else {
      if (stack.length > 0) {
        if (
          (s[i] === ")" && stack[stack.length - 1] === "(") ||
          s[i] === "]" ||
          s[i] === "}"
        ) {
          stack.pop();
        }
      }
      return false;
    }
  }
  return true;
};

function makeNew(array) {
  //receive an array
  //return a new array with pairs wrapped around an array
  //[0, 1]

  let newArray = [];
  for (let i = 0; i < array.length; i++) {
    newArray.push([array[i], array[i + 1]]);
  }
  return newArray;
}

function twoSum(numbers, target) {
  //receive an array of numbers, target
  //return the index position
  //[3, 4, 5, 8], 9 => [1, 2]

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] + numbers[j] === target) {
        return [i, j];
      }
    }
  }
}
