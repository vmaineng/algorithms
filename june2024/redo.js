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

function mergeLL(head1, head2) {
  //receive head of two sorted linked lists
  //return one linked list with nodes sorted in order
  //1 -> 2 -> 3 -> null
  //2 -> 4 -> 6 -> null
  //return 1 -> 2 -> 2 -> 3 -> 4 -> 6 -> null

  //edge case: if one head is empty, return the other head;

  //create a dummy node
  //check which val of the first node is smaller,
  //add in that node
  //then add in the rest of the nodes
  //return the dummy node

  if (!head1) return head2;
  if (!head2) return head1;

  let dummyNode = new Node();
  let current1 = head1;
  let current2 = head2;
  let tail = dummyNode;

  while (current1 && current2) {
    if (current1.val < current2.val) {
      tail.next = current1;
      current1 = current1.next;
    } else {
      tail.next = current2;
      current2 = current2.next;
    }
    if (current1) tail.next = current1;
    if (current2) tail.next = current2;
  }
  return dummyNode.next;
}

function newArray(array) {
  array.map((ele, idx) => {
    const newIdx = idx + 1;
    return newIdx + ":" + ele;
  });
}

function checkForFactor(base, factor) {
  //receive two numbers for base and factor
  //return true if factor of base
  //else return false

  //(4, 8) 8 % 4 => 2 with no remainder = true

  //take factor % base, if remainder is 0, true, else it's false

  return base % factor === 0 ? true : false;
}

var reverseWords = function (s) {
  //receive a string of words with spaces
  //return each word reversed
  //"hi, my name is" => 'si eman ym ,ih'

  //split the string to grab each words
  //grab the words and split them, and reverse and join back together
  //join it all back

  let splitWords = s.split(" ");
  let reversedWords = splitWords.map((word) => {
    return word.split("").reverse().join("");
  });
  return reversedWords.join(" ");
  // ! new strings have to be named and have to return the words
};

var groupAnagrams = function (strs) {
  //receive an array with strings
  //return grouped strings together in an array all put in an array back

  //edge case: if empty, return empty array back

  //create an object
  //sort the strings
  //the sorted strings will be the key in the object
  //the actual strings will be the value

  //return the values back;

  if (strs.length === 0) return [strs];

  let sortedStrObj = {};

  for (let str of strs) {
    let sortedStr = str.split("").sort().join("");
    if (!sortedStrObj[sortedStr]) sortedStrObj[sortedStr] = [];
    sortedStrObj[sortedStr].push(str);
  }

  return Object.values(sortedStrObj);
};
function gimme(triplet) {
  //receive an array of inters
  //return an integer of where the middle value lives
  //[3, 4,5] => 1

  //create a copy of the triplet and sort it
  //find the index of the middle value

  let sortedTriplet = [...triplet].sort((a, b) => a - b); //[1,2, 3]
  let middleValue = sortedTriplet[1]; //1
  console.log(sortedTriplet, middleValue);

  return triplet.indexOf(middleValue);
}

function flickSwitch(arr) {
  //receive an array of strings
  //return an array with booleans, if 'flick', convert it to opposite
  //['mad', 'happy', 'flick', 'joe', 'flick'] => [True, True, False, True, False]

  //iterate through the array
  //if the word equals false, switch it to the opposite
  //else keep as is
  //return the array

  let switchBooealn = true;

  return arr.map((word) => {
    if (word === "flick") {
      switchBooealn = !switchBooealn;
    }
    return switchBooealn;
  });
}

function longestConsec(strarr, k) {
  //receive an array of strings, and integer to tell you how many strings you can add
  //return the string length of two strings connected
  //['hi', 'yellow', 'four'], => 'yellow'

  //create a maxString
  //iterate through the string
  //keep track of the maxString seen
  //if i + j surpasses k, move i and j up

  if (strarr.length === 0 || k > strarr.length || k <= 0) {
    return "";
  }

  let maxString = "";
  let currString = "";

  for (let i = 0; i < strarr.length; i++) {
    currString = strarr.slice(i, i + k).join("");
    if (currString.length > maxString.length) {
      maxString = currString;
    }
  }
  return maxString;
}

/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function (flowerbed, n) {
  //receive an array of 1 (flower), 0 (empty), n = how many more flowers to plant
  //return true if n amount can be planted, else return false
  //[0, 1, 0, 1], 2 => false

  //adjacent = right next to each other

  //checkhow many 0 next to 1,
  //if this exceeds n, return false

  //iterate through flowerbed array
  //check if value is a 0, then check if the one before it is a 0, and the one after it is a 0
  //keep track of total

  //if total < n, return false, else return true

  let count = 0;

  for (let i = 1; i < flowerbed.length; i++) {
    if (flowerbed[i - 1] === 0 && flowerbed[i + 1] === 0) {
      flowerbed[i] = 1;
      count++;
    }

    if (count >= n) {
      return true;
    }
  }

  return false;
};

//time: O(n)
//space: O(n) - to keep track of count

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  //receive a string of words
  //return the words in reversed order
  //'hi joe jilly' => 'jilly joe hi'

  //split the string to capture each word
  //create a new string
  //add in the last word in first
  //return the string back

  let revWord = "";
  let splitString = s.split(" ");

  for (let i = splitString.length - 1; i >= 0; i--) {
    if (splitString[i] !== "") {
      revWord += splitString[i] + " ";
    }
  }
  return revWord.trim();
};
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function (nums) {
  //receive an array of integers
  //return true if the index are in chronological order and so are the values (increasing)
  //[3, 5, 6, 2, 1] => true => [3, 5, 6] && index are 0, 1, 2

  //create an array to store index
  //create an array to store values

  //iterate through the nums array (i)
  //iterate again for j and k
  //check if the value is increasing && check if the index position are increasing, return true;
  //else after checking everything return false

  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (nums[i] < nums[j] && nums[j] < nums[k] && i < j < k) {
          console.log(nums[i], nums[j], nums[k]);
          console.log(i, j, k);
          return true;
        }
      }
    }
  }
  return false;
};

//time: O(n^3)
//space: O(1)
