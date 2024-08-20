function caesarCipherEncryptor(string, key) {
  //receive a string of chars with no spaces and lowercase alphabet letters, and a key of integers
  //return a new string with key added

  //'abc', 3 => 'def'

  //create an alphabet to hold all letters of alphabet
  //create a new key % 26 to get the remainders
  //look for the index of each char in string
  // add new index to it with key
  //if new index is greater than 25, then subtract from 26
  //return new letters

  let newWord = [];
  const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
  let newKey = key % 26;

  for (let char of string) {
    let oldIdx = alphabet.indexOf(char);
    let newIdx = oldIdx + newKey;
    if (newIdx > 25) newIdx -= 26;
    newWord.push(alphabet[newIdx]);
    // console.log(newWord);
  }
  return newWord.join("");
}

// Do not edit the line below.
exports.caesarCipherEncryptor = caesarCipherEncryptor;

// console.log(caesarCipherEncryptor("abc", 3));

function commonChar(strings) {
  //receive an array of strings
  //return an array of common chars
  //['hi', 'hello', 'hey'] => ['h']

  //create a set of the first word
  //iterate through the rest of the array
  //create a new set of second word
  //check if the letters in the first set is found in second set
  //if not, delete from first
  //return first set

  let firstSet = new Set(strings[0]);

  for (let i = 1; i < strings.length; i++) {
    let resetSet = new Set(strings[i]);
    for (let char of firstSet) {
      if (!resetSet.has(char)) {
        firstSet.delete(char);
      }
    }
  }
  return Array.from(firstSet);
}

//console.log(commonChar(["hi", "hello", "hey"]));

function firstNonRepeatingCharacter(string) {
  //receive a string of chars with no spaces
  //return the index position of non-repeating char
  //'abcdebc' => a

  //brute force: create nested for loops?

  //optimized: freq counter

  //create an object
  //iterate through the string
  //keep track of how many times you've seen it
  //return the index position of values seen 1 time

  let seenVals = {};

  for (let char of string) {
    if (!seenVals[char]) {
      seenVals[char] = 0;
    }
    seenVals[char] += 1;
  }

  //   for (let key in seenVals) {
  //     if (seenVals[key] === 1) {
  //       return key;
  //     }
  //   } //grabs the value

  //grab idex position =
  for (let i = 0; i < string.length; i++) {
    if (seenVals[string[i]] === 1) return i;
  }

  return -1;
}

// Do not edit the line below.
exports.firstNonRepeatingCharacter = firstNonRepeatingCharacter;

//console.log(firstNonRepeatingCharacter("abcdebc"));

function runLengthEncoding(string) {
  //receive a string of chars uppercase
  //return back the count of strings in a string back
  //ex: 'AARRRRRRRRRRRRRRS' => '2A9R4R1S'

  //if string has one, return the string with one

  //create an object to store the value we have seen
  //iterate through the string

  //keep track of the count;
  //if the count surpasses 9, reset the count to 1

  //check the previous letter before it
  //if it's the same, add by 1
  //else start a new one

  //return the item

  // if (string.length === 1) return `1${string}`

  let objSeen = {};

  for (let char of string) {
    if (!objSeen[char]) {
      objSeen[char] = 0;
    }
    objSeen[char]++;
  }

  for (let key in objSeen) {
    if (objSeen[key] > 9) {
    }
  }
}

// Do not edit the line below.
exports.runLengthEncoding = runLengthEncoding;

// console.log(runLengthEncoding("AARRRRRRRRRRRRRRS"));

function generateDocument(characters, document) {
  //receive two strings of chars with spaces
  //return boolean; true if you can agenerate document from characters, else false
  //'hi', 'hello' => false

  //edge case ; if both strings are empty, can generate empty string

  //brute force: sort characters and document strings?
  //similar to is valid subsequence?

  //method: freq counter:

  //create an object to track frequencies
  //if chars exist for documents,
  //keep looking through the rest
  //else return false
  //else return true

  let charCount = {};

  for (let char of characters) {
    if (!charCount[char]) return (charCount[char] = 0);
  }
  charCount[char] += 1;

  for (let char in charCount) {
    if (!document[char] === 0) return false;
  }
  return true;
}

// Do not edit the line below.
exports.generateDocument = generateDocument;

function groupAnagrams(words) {
  //receive an array of words
  //return an array of arrays of anagrams together
  //anagram = using same amount of letter
  //['apple', 'pplea', 'yo'] = [['apple', 'pplea',], 'yo']

  //edge case: if array has one, or empty

  //create an object
  //sort the letters
  //create an array
  //push the word together into the array
  //return the object entries as arrays

  let anagramObj = {};

  for (let word of words) {
    let sortedWord = word.split("").sort().join("");
    if (!anagramObj[sortedWord]) anagramObj[sortedWord] = [];
    anagramObj[sortedWord].push(word);
  }
  return Object.values(anagramObj);
}

// Do not edit the line below.
exports.groupAnagrams = groupAnagrams;

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  //receive a string of lowercase letters
  //palindrome = word written the same forward as it is backwards
  //'abacdcdef' => 'aba'

  //output: longest palindromic substrings; string of characters

  //example: 'racecar' => 'racecar'; //odd lengths
  //'abbacdef' => 'abba' //even lengths

  //edge case: any spaces to take consideration? all lowercase letters?
  //if the string has only letter, return string
  //'a' => 'a'

  //create a string to hold the longest palindromic substring
  //iterate through the strings
  //one pointer starts at the beginning
  //second pointer starts right next to it;

  //take out a portion of the string
  //check if the it is a palindrome, if it is, then check if it is longer than the current palindrome string
  //right now

  //return palindrome string

  if (s.length === 1) return s;

  let longestPalindromic = "";

  for (let i = 0; i < s.length; i++) {
    for (let j = i; j < s.length; j++) {
      let palindrome = true;
      let substring = s.slice(i, j + 1);

      let left = 0;
      let right = substring.length - 1;

      while (left < right) {
        if (substring[left] !== substring[right]) {
          palindrome = false;
          break;
        }
        left++;
        right--;
      }

      if (palindrome && substring.length > longestPalindromic.length) {
        longestPalindromic = substring;
      }
    }
  }

  return longestPalindromic;
};

//time: O(n^2) -
//space: O(n)

function whatday(num) {
  //receive an integer
  //return a string back for the designated weekday
  //'8' => "Wrong, please enter a number between 1 and 7"
  //3 => "Tuesday"

  //edgecase: number > 7 or < 1

  //create an object to hold the number as key, and values are weekdays
  //if the num matches the key in the obj, return the value

  //time: O(1)
  //space: O(1)

  if (num < 1 || num > 7) return "Wrong, please enter a number between 1 and 7";

  const weekDayObj = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday",
  };

  if (num in weekDayObj) {
    return weekDayObj[num];
  }
}

function mergeOverlappingIntervals(array) {
  //receive an array of arrays of start and end time
  //return back an array of arrays where the end time of the first interval is less than start time end time
  //[[1,2], [2 , 4]] => [[1, 4]]

  //sort the star time of the array

  //capture the first array
  //iterate trhough the array
  //destructure end time of the first array, start of the second array
  //check if the start time <= end time, let's merge
  //end time = update it the max end time
  //else - there's no conflict, push the array

  //return the array

  array.sort((a, b) => a[0] - b[0]);

  let result = [array[0]];

  for (let i = 1; i < array.length; i++) {
    let start = array[i]; //capture the current arrays
    let end = result[result.length - 1]; //capture the previous array
    if (start[0] <= end[1]) {
      end[1] = Math.max(end[1], start[1]);
    } else {
      result.push(array[i]);
    }
  }
  return result;
}

// Do not edit the line below.
exports.mergeOverlappingIntervals = mergeOverlappingIntervals;

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  //receive an array of prices
  //return maxProfit (integer)
  //[3, 6,7 3, 2] => buy on 3, sell, on 7 => 4

  //edge case: if array is empty, return 0;

  //initialize a maxProfit at 0, start the buy on first day
  //iterate through prices array
  //look at second value in array
  //check if the sell price is higher,
  //if so, calc sell - buy = maxprofit
  //if it's greater than maxProfit currently, update maxProfit
  //return the max profit

  if (prices.length === 0) return 0;

  let maxProfit = 0;
  let buy = 0;

  for (let sell = 1; sell < prices.length; sell++) {
    if (prices[buy] < prices[sell]) {
      let profit = prices[sell] - prices[buy];
      maxProfit = Math.max(maxProfit, profit);
    } else {
      buy = sell;
    }
  }
  return maxProfit;
};

function balancedBrackets(string) {
  //receive a string of opening and closing brackets
  //return true if they pair up together, else false;
  //'()' => true
  //'({(}{' => false

  //create a stack
  //create an object to show opening and closing brackets
  //iterate through string
  //check if it's an opening bracket, add to the stack
  //else if it is a closing bracket,
  //check if the stack is not empty
  //pop up the previous one in the stack to see if it is an opening
  //if not, return false;

  //return true if stack is empty

  let stack = [];
  const bracket = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  for (const char of string) {
    if (bracket[char]) {
      stack.push(bracket[char]);
    } else if (char === ")" || char === "}" || char === "]") {
      if (!stack.length) {
        return false;
      }
      if (stack.pop() !== char) {
        return false;
      }
    }
  }
  return stack.length === 0;
}

// Do not edit the line below.
exports.balancedBrackets = balancedBrackets;

function majorityElement(array) {
  //receive an array of positive integers
  //return the element that appears more than half of the array
  //[2,3,2,1] => 0 since 2 only appears 2/4
  //[3,2 ,5 ,2, 2, 5, 1,2, 2, 2] => 2 b/c 6/10

  //if array is empty return 0;

  //iterate through the array
  //keep track of the character most seen
  //take the character divde by the length to see if majority element
  //return the value

  if (!array) return 0;

  let freqElement = {};
  let maxVal = 0;
  let ele = null;

  for (const num of array) {
    if (!freqElement[num]) {
      freqElement[num] = 0;
    }
    freqElement[num]++;
  }

  for (const key in freqElement) {
    if (freqElement[key] > maxVal) {
      maxVal = freqElement[key];
      ele = key;
      console.log(ele);
    }
  }
  return parseInt(ele);
}

// Do not edit the line below.
exports.majorityElement = majorityElement;

//console.log(majorityElement([2, 3, 2, 1]));

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

exports.LinkedList = LinkedList;

function middleNode(linkedList) {
  //slow and fast pointer

  let slow = linkedList;
  let fast = linkedList;

  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}
//o(n time); o(1 space)

// Do not edit the line below.
exports.middleNode = middleNode;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

exports.LinkedList = LinkedList;

function middleNode(linkedList) {
  //receive a head of linkedlist
  //return the middle node
  //2 -> 4 -> 8 -> 9 -> null => 8_. 9

  //keep count
  //iterate through entire linkedlist
  //then iterate through again
  //find the middle node
  //return

  let count = 0;
  let current = linkedList;

  while (current !== null) {
    count++;
    current = current.next;
  }

  let middleNode = linkedList;
  for (let i = 0; i < Math.floor(count / 2); i++) {
    middleNode = middleNode.next;
  }

  return middleNode;
}

// Do not edit the line below.
exports.middleNode = middleNode;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function sumOfLinkedLists(linkedListOne, linkedListTwo) {
  //receive head of two LL
  //return a new LL that represents sum of the nodes
  // 2 -> 3 -> 9 -> null  --> 932
  //9 -> 2 ->  null --> 29
  //return => 1 -> 6 -> 9 -> null --> 961

  //create a dummy node
  //initialize carry

  //traverse trhough both LL
  //add them together
  //if carry, add to next sum;

  if (!linkedListOne) return linkedListTwo;
  if (!linkedListTwo) return linkedListOne;

  let dummy = new LinkedList(0);
  let current = dummy;

  let current1 = linkedListOne;
  let current2 = linkedListTwo;
  let carry = 0;

  while (current1 !== null || current2 !== null || carry !== 0) {
    let value1 = current1 !== null ? current1.value : 0;
    let value2 = current2 !== null ? current2.value : 0;

    let sum = value1 + value2 + carry;
    carry = Math.floor(sum / 10); //13 /10 = 1.3 and Math.floor gives you 1
    let newValue = sum % 10; //looks at carry

    current.next = new LinkedList(newValue);
    current = current.next;

    if (current1) current1 = current1.next;
    if (current2) current2 = current2.next;
  }
  return dummy.next;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.sumOfLinkedLists = sumOfLinkedLists;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeDuplicatesFromLinkedList(linkedList) {
  //receive a head of linkedlist
  //return the same linkedlist back w/ no duplicate values
  // 1 -> 2 -> 2 -> 3 -> null => 1 -> 2 -> 3 -> null
  //edge case: if LL is null, return null

  //capture the first head of the ll
  //traverse until null
  //check if the next node's value === as current node
  //if so, skip it and point to the node afterwards;
  //else move the pointer up
  //return the linked list

  if (!linkedList) return null;

  let current = linkedList;

  while (current !== null && current.next !== null) {
    if (current.value === current.next.value) {
      current.next = current.next.next;
    } else {
      current = current.next;
    }
  }
  return linkedList;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.removeDuplicatesFromLinkedList = removeDuplicatesFromLinkedList;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function reverseLinkedList(head) {
  //receive the head of a LL
  //return the LL reversed in place
  // 1 -> 2 -> 3 -> null => 3 -> 2 -> 1 -> null;

  //edge case: if the head is empty, return null;
  //capture the current as the head
  if (!head) return null;

  let prev = null;
  let current = head;

  while (current !== null) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.reverseLinkedList = reverseLinkedList;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function reverseLinkedList(head) {
  //receive a head of LL;
  //return the LL reverse;
  // 1 -> 2 -> 3 -> null => 3 -> 2 -> 1 => null;

  let dummyNode = new LinkedList();
  let prev = dummyNode;
  let current = head;

  while (current !== null) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.reverseLinkedList = reverseLinkedList;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function mergeLinkedLists(headOne, headTwo) {
  //receive the head of two LL;
  //return one LL with sorted values;

  // 1-> 3 -> 5 -> null;
  //2 -> 4 -> 9 -> null;
  // => 1 -> 2 -> 3 -> 4 -> 5 -> 9 -> null;

  //edge case; if one is emtpy, return the other
  if (!headOne) return headTwo;
  if (!headTwo) return headOne;

  //capture the head of both LL
  //compare the values
  //then add them in;
  //if one list has any remaining, add in the rest
  //else return the head;

  let current1 = headOne;
  let current2 = headTwo;
  let head;
  let tail;

  if (current1.value < current2.value) {
    head = current1;
    current1 = current1.next;
  } else {
    head = current2;
    current2 = current2.next;
  }
  tail = head;

  while (current1 !== null && current2 !== null) {
    if (current1.value < current2.value) {
      tail.next = current1;
      current1 = current1.next;
    } else {
      tail.next = current2;
      current2 = current2.next;
    }
    tail = tail.next;
  }

  if (current1 !== null) tail.next = current1;
  if (current2 !== null) tail.next = current2;

  return head;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.mergeLinkedLists = mergeLinkedLists;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function removeDuplicatesFromLinkedList(linkedList) {
  //receive the head of a linkedlist
  //return the linkedlist removing duplicate values
  //1 -> 2 ->  2 -> 3 -> null
  // => 1 -> 2 -> 3 -> null

  //edge case: if the head is empty, return null;

  //capture the head of the linkedlist
  //traverse through entire LL until hit null;
  //check the current node values and the next node values,
  //if they are the same, current node point to the next node after it
  //else move the current node to the node next since they are not the same
  //return linkedlist

  if (!linkedList) return null;

  let current = linkedList;

  while (current !== null && current.next !== null) {
    if (current.value === current.next.value) {
      current.next = current.next.next;
    } else {
      current = current.next;
    }
  }
  return linkedList;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.removeDuplicatesFromLinkedList = removeDuplicatesFromLinkedList;

// This is an input class. Do not edit.
class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function reverseLinkedList(head) {
  // receive the head of a LL
  //return the LL in reverse
  // 1-> 2 -> 3 -> null => 3-> 2 -> 1 -> null

  //edge case: if it's empty, return null;

  //create a prev node set it null;
  //have a pointer on the first node of LL
  //capture the next node;
  //have the pointer point to prev;
  //move prev to current node;
  //move current node to next
  //return prev

  if (!head) return null;

  let prev = null;
  let current = head;

  while (current !== null) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
}

// Do not edit the lines below.
exports.LinkedList = LinkedList;
exports.reverseLinkedList = reverseLinkedList;

function saleHotdogs(n) {
  //receive an integer
  //return the amount paid per unit
  //4 => 400;

  //if n < 5, 100 * n; else if n >= 5 && n < 10 , 95 * n; else n * 90

  return n < 5 ? n * 100 : n >= 5 && n < 10 ? n * 95 : n * 90;
}

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  //input: string : consist of lowercase, uppercasae, space, puncations, number
  //return a boolean; true if it is a palindrome; else false;

  //'RaCecar' => 'racecar' => true;
  // 'racecar'

  //'h5ll0!' => 'h5ll0' => false
  //'0ll50'

  //'hi, the FiSh' => 'hithefish'

  //edge case: if it's empty, return true;
  //if string only has one element, return true;  'a' => 'a'

  //take the string, lowercase it. split it on spaces

  //initialize an empty string
  //check to see if it has numbers and letters; (helps ignore the punctation marks)
  //reverse method -
  //join it back with ""

  //check to see if the reverse string matches the string input

  if (!s) return true;
  if (s.length === 1) return true;

  s = s.toLowerCase();

  let left = 0;
  let right = s.length - 1;
  //ensures condition is met as long as left pointer is left of the right pointer
  while (left < right) {
    //the inner while loops
    //Within each iteration of the outer while loop, the code compares the characters at the left and right pointers.
    //If the characters don't match, the function returns false, indicating that the string is not a palindrome.
    //If they do match, the pointers are moved inward (left++ and right--), and the process repeats for the next pair of characters.
    while (left < right && !isAlphanumeric(s[left])) {
      left++;
    }

    while (left < right && !isAlphanumeric(s[right])) {
      right--;
    }
    // Compare the characters at the left and right pointers
    if (s[left] !== s[right]) {
      return false;
    }

    // Move pointers inward
    left++;
    right--;
  }
  return true;
};

function isAlphanumeric(char) {
  return (char >= "a" && char <= "z") || (char >= "0" && char <= "9");
}

//time: O(N)
//space: O(N)

import { Interval } from "/opt/node/lib/lintcode/index.js";

/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

export class Solution {
  /**
   * @param intervals: an array of meeting time intervals
   * @return: if a person could attend all meetings
   */
  canAttendMeetings(intervals) {
    //receive an array of meetings (start and end)
    //return boolean; true if they can make it; else, false;
    //[(3, 15), (4, 8)] => false since 15 overlaps with 4 - 8

    //sort start time
    //iterate through the intervals
    //check if the end time is >= start time
    //return false
    //else return true

    intervals.sort((a, b) => a.start - b.start);

    for (let i = 0; i < intervals.length; i++) {
      const [end] = intervals[i].end;
      const [nextStart] = intervals[i + 1].start;
      if (end > nextStart) {
        return false;
      }
    }
    return true;
  }
}

console.log(
  canAttendMeetings([
    [3, 15],
    [4, 8],
  ])
);

function isMonotonic(array) {
  //receive an array of integers
  //return boolean ; true if monotonic; else false
  //[-3, 1, 5, 1, 4] => false [ 5 -> 1]
  //[3] = true;;

  //check for both at the same time;
  //set isDecreasing to true;
  //set isIncreasing to true;

  //iterate through the array
  //look at the next value;
  //check if the next value less than the current value, switch boolean to false

  //return the value for isDecreasing and isIncreasing;

  //edge case: if empty return true;
  if (array.length <= 2) return true;

  let isIncreasing = true;
  let isDecreasing = true;

  for (let i = 1; i < array.length; i++) {
    if (array[i] < array[i - 1]) isDecreasing = false;
    if (array[i] > array[i - 1]) isIncreasing = false;
  }

  return isIncreasing || isDecreasing;
}

// Do not edit the line below.
exports.isMonotonic = isMonotonic;

function isMonotonic(array) {
  //receive an array of integers (pos and neg)
  //return true or false
  //[3, 5, 6,7 2, 4, ] => false b/c 72 -> 4

  //intiialize two variables set to true;
  //iterate trhough the array
  //check for both instances
  //return the array back

  if (array.length < 2) return true;

  let isIncreasing = true;
  let isDecreasing = true;

  for (let i = 1; i < array.length; i++) {
    if (array[i] < array[i - 1]) isDecreasing = false;
    if (array[i] > array[i - 1]) isIncreasing = false;
  }
  return isDecreasing || isIncreasing;
}

// Do not edit the line below.
exports.isMonotonic = isMonotonic;
