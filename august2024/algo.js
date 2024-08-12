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
