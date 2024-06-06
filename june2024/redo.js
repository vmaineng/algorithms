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
