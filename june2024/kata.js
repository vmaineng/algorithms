function divisibleBy(numbers, divisor) {
  //receive two array of integers (positive)
  //return back an array of integers from numbers that are divisible by divisor
  //[21, 36, 15], 3 => [21, 36, 15]

  //if anything mod the divisor leaves no remainder, add to the output array

  let outputArray = [];

  for (let i = 0; i <= numbers.length; i++) {
    if (numbers[i] % divisor === 0) {
      outputArray.push(numbers[i]);
    }
  }
  return outputArray;

  //return numbers.filter((number % divisor === 0 )
}

//time: O(n)
//space: O(n)

function order(words) {
  //receive a string with space and chars and letters
  //return the string back in order '1', '2', '3'
  //'hi2 kit3 air1' => 'air2 hi2 kit3'

  //edge case: if string is empty, return string
  if (!words) return "";

  //split the string into an array to get individual words
  //iterate through the array to find 1, then add to new string
  //add count?
  //join them back together

  let splitWords = words.split(" ");
  const sortedWords = splitWords.sort((a, b) => {
    const numA = parseInt(a.match(/\d/)[0]);
    const numB = parseInt(b.match(/\d/)[0]);
    console.log(numA, numB);
    return numA - numB;
  });
  console.log(sortedWords);
  return sortedWords.join(" ");
}
function reverseWords(str) {
  //receive a string of words and spaces
  //return the string back reversed and spaces in same order
  //'this fish' => 'hsif siht'

  //split the words
  //take the word and reverse it
  //join the word back into one
  //then join it back with spaces

  let newStr = [];

  let splitStr = str.split(" ");
  for (let i = 0; i < splitStr.length; i++) {
    splitStr[i] = splitStr[i].split("").reverse().join("");
    newStr.push(splitStr[i]);
  }
  return newStr.join(" ");
}

console.log(order("is2 Thi1s T4est 3a"));

var replaceDots = function (str) {
  const regex = /\./g;
  return str.replaceAll(regex, "-");
};

function dutyFree(normPrice, discount, hol) {
  //receive integers for norm Price, discount, and hol
  //return bottles you have to purchase (round down)

  //dutyFree (12, .50, 1000) => 166 bottles
  //12  * .5 = 6; 1000 / 6 = 166

  //calc rate of normPrice * discount
  //take hol % rate
  //return round down of hol % rate

  let rate = normPrice * (discount / 100);

  return Math.floor(hol / rate);
}

function duplicateEncode(word) {
  // receive a string of chars
  //return a string back showcasing '(' if char only occurs once, else ')' for the letter that appears
  //more than once
  //'apple' => '())(('

  //create a new string

  //store the values in a map
  //if values > than one, then new string will add a ')'
  //else, add a '('

  //return new string

  let lowercaseWords = word.toLowerCase();

  let result = "";

  let charsSeen = {};

  for (let char of lowercaseWords) {
    charsSeen[char] = (charsSeen[char] || 0) + 1;
  }

  for (let char of lowercaseWords) {
    if (charsSeen[char] > 1) {
      result += ")";
    } else {
      result += "(";
    }
  }
  return result;
}

function noBoringZeros(n) {
  //receive an integer
  //return an integer back; if it has a 0, remove the zero at end
  //45 => 45
  //450 => 45

  //turn the number to string
  //iterate through stringNum starting at the end
  //check if it is a 0, slice it out
  //return new string

  let stringNum = n.toString();

  while (stringNum.endsWith("0")) {
    stringNum = stringNum.slice(0, -1);
    //0, -1 => grab everything from beginning until the very last one
  }

  return Number(stringNum);
}

function friend(friends) {
  //receive an array of strings
  //return a new array back of strings with chars = 4

  //filter method on it

  return friends.filter((name) => name.length === 4);
}
function problem(x) {
  //receive an integer
  //return a new integer where input is * 50 + 6
  //problem(4) = 50 * 4 = 200 + 6 = 206

  //edge case, if value is string, return "Error"
  //take input * 50 + 6

  if (typeof x === "string") return "Error";

  let sum = x * 50 + 6;
  return sum;
}

function nthEven(n) {
  // receive a number to pull the even number from the numerical order
  //return the even number in numerical order
  //nthEven(4) => 0, 2, 4, 6 => 6

  //take the input value * 2 then - 2
  return n * 2 - 2;
}

var humanYearsCatYearsDogYears = function (humanYears) {
  // receive an integer for humanyears
  //return an array back with the human years, catYears, dogYears
  //[5] => (1: 15, 2: 9, 3: 4, 4: 4,5:4)
  //[5,36, 39]

  //intiialize a variable to humanYears = number passed in
  //initialize a variable to cat years
  //if humanYears > +15, after 2 years, +9, after 3, +4
  //initialize a variable to dog years
  //if humanYears > +15, after 2 years, +9, after 3, +5

  //push into an array

  let catAge = 0;
  let dogAge = 0;

  //for every year after 3 years, add 4 (cat), 5(dog)

  for (let i = 1; i <= humanYears; i++) {
    if (i === 1) {
      catAge += 15;
      dogAge += 15;
    } else if (i === 2) {
      catAge += 9;
      dogAge += 9;
    } else {
      catAge += 4;
      dogAge += 5;
    }
  }
  return [humanYears, catAge, dogAge];
};

function position(letter) {
  //receive a string of char
  //return the posiition it is in the alphabet
  //'c' => 3

  //create an alphabet to hold all the strings in an array
  //return the indexOf the letter

  const alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];

  return `Position of alphabet: ${alphabet.indexOf(letter) + 1}`;
}

function mergeArrays(arr1, arr2) {
  //receive two arrays of integers
  //return back one array with integers sorted in order
  //[2, 3, 4, 5, 7], [1, 2, 3, 4] => [1, 2, 3, 4, 5, 7]

  //edge cases: if one array is empty, return the other one if it's not empty
  //otherwise if both empty, return an empty array back

  if (!arr1) return arr2;
  if (!arr2) return arr1;
  if (!arr1 && !arr2) return [];

  //add them all together into one big array
  //filter out duplicates
  //return sorted array

  let groupedArray = arr1.concat(arr2).sort((a, b) => a - b);
  return [...new Set(groupedArray)];
}

//time: O(n);
//space: O(n); //creating a new Array to store

function sortReindeer(reindeerNames) {
  //receive an array of strings with firstName and lastName
  //return the array back with last Names in alphabetical order
  //['joe jim', 'mary blige', 'array ham'] => ['mary blige', 'array ham', 'joe jim']

  //brute force
  //create an array to hold the sorted names
  //iterate through the array
  //split the strings
  //check the first letter of the lastName
  //sort
  //return back with " "

  return reindeerNames.sort((a, b) => {
    const lastNameA = a.split(" ")[1];
    const lastNameB = b.split(" ")[1];

    if (lastNameA < lastNameB) {
      return -1;
    } else if (lastNameA > lastNameB) {
      return 1;
    } else {
      return 0;
    }
  });
}

function gHappy(str) {
  //receive a string of letters
  //return true if 'g' is spotted next to a 'gg', else false
  //'happg' => 'false'

  //edge case: if string is empty, return false

  //if str does not include two g's, return false

  //split the string
  //iterate through it
  //check if it equals a 'g'
  //check previous one before and after
  //if there isn't, return false
  //else return true

  //all 'g' have to have a matching pair

  if (!str) return false;

  let splitStr = str.split("");

  for (let i = 0; i < splitStr.length; i++) {
    if (splitStr[i] === "g") {
      console.log(splitStr[i]);
      if (splitStr[i - 1] !== "g" && splitStr[i + 1] !== "g") {
        return false;
      }
    }
  }
  return true;
}

function combat(health, damage) {
  // receive integers
  //return back one integer that sums up the newHealth
  //combat(40, 20) => 40 - 20 = 20
  //combat(10, 30) => 0,

  //edge cases: if a parameter isn't a number,

  //initialize to capture newHealth at 0;
  //take health - damage
  //return the total back
  //if it is negative, return 0

  let newHealth = health - damage;

  return newHealth > 0 ? newHealth : 0;
}

//time: O(1)
//space: O(n)

function alphabetPosition(text) {
  //receive a string of letters with spaces
  //return back a string of integers - ignore spaces & punctuations
  //'joe jam' => '10 15 5 10 1 13'

  //a: 1, b: 2, c:3, d: 4, e: 5, f: 6, g: 7, h: 8, i: 9, j: 10, k: 11, l:12
  //m: 13, n: 14, o: 15

  //edge cases: if the string is empty, return back an empty string

  //create an object and store the position as the value
  //key: letter, value: position in the alphabet

  //iterate through the text, add it to the new string
  //return the string

  //.charAt

  let newString = "";

  let letterPosition = {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
    e: 5,
    f: 6,
    g: 7,
    h: 8,
    i: 9,
    j: 10,
    k: 11,
    l: 12,
    m: 13,
    n: 14,
    o: 15,
    p: 16,
    q: 17,
    r: 18,
    s: 19,
    t: 20,
    u: 21,
    v: 22,
    w: 23,
    x: 24,
    y: 25,
    z: 26,
  };

  for (let char of text.toLowerCase()) {
    console.log(char);
    if (letterPosition[char]) {
      newString += letterPosition[char] + " ";
    }
  }
  return newString.trim();
}

//time: O(n);
//space: O(n); creating a new string

function isIsogram(str) {
  //receive a string of letters
  //return true if all chars are unique
  //else return false
  //'jump' => true
  //'he1l0' => false

  //lowercase all the letters
  //keep track o it in an object
  //if the value has been seen, return false
  //else add one

  //after checking everything, return true

  let seenVals = {};
  for (let char of str.toLowerCase()) {
    if (seenVals[char]) {
      return false;
    } else {
      seenVals[char] = 1;
    }
  }
  return true;
}

String.prototype.toJadenCase = function () {
  //receive a string of words & spaces
  //return the string back with the first letter of each word capitalize
  //'i'm doing great' => 'I'm Doing Great'

  //split the string into words
  //take each word and capitalize the first letter and add in the rest
  //return the string back joined by spaces

  let splitWords = this.split(" ");

  for (let i = 0; i < splitWords.length; i++) {
    splitWords[i] = splitWords[i][0].toUpperCase() + splitWords[i].slice(1);
  }
  return splitWords.join(" ");
};

function twoSum(nums, target) {
  //receive an array of integers and an integer for the target
  //return back the index position
  //[3, 4, 5, 3], 6 => [0, 3]

  //create an object
  //store the value as key, index position as value
  //check the object if it has the difference stored as a value
  //return the index position
  //else store

  let valsSeen = {};

  for (let i = 0; i < nums.length; i++) {
    let different = target - nums[i];
    if (valsSeen.hasOwnProperty(difference)) {
      return [valsSeen[difference], i];
    } else {
      valsSeen[nums[i]] = i;
    }
  }
}

/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  //receive two strings of one word
  //return one string back with each alternating letter from both words
  //'hi', 'joe' => 'hjioe'

  //create a new string
  //iterate through the longest string
  //add the letter from the first word
  //then add in the letter from the second word
  //return the new string

  let newString = "";

  for (let i = 0; i < Math.max(word1.length, word2.length); i++) {
    if (i < word1.length) newString += word1[i];
    if (i < word2.length) newString += word2[i];
  }

  return newString;
};

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  //receive an array of integers
  //return back an array of integers where it is the product of all the other elements excluding the current value
  //[3, 4, 5, 2] => [40, 30, 24, 60]

  //initialize an empty array
  //initialize a count
  //iterate through the nums array
  //take the product and multiply the other
  //push the product into the array
  const n = nums.length;
  const result = new Array(n).fill(1);

  let leftProduct = 1; //multiply by current element
  for (let i = 0; i < n; i++) {
    result[i] *= leftProduct; //multiply by 1 to capture each value
    console.log(result);
    leftProduct *= nums[i]; //update actual values
  }

  let rightProduct = 1;
  for (let i = n - 1; i >= 0; i--) {
    result[i] *= rightProduct;
    rightProduct *= nums[i];
  }

  return result;
};

var isPalindrome = function (x) {
  //receive a number
  //return boolean - true if palindrome, else false
  //75638 => false

  //using methods:
  //turn the number to string, split it, reverse it, join it back together
  //check if teh reversed string is equal to the origianl

  return x.toString().split("").reverse().join("") === x.toString();
};

function revLL(head1) {
  //receive a head of a linked list
  //return the LL in reverse
  // 1-> 2 -> 3
  //3 -> 2 -> 1

  //edge case: if head is empty

  //create a prev node ; set it null;
  //capture the current node of head1

  //iterate through the linked list
  //capture the next node in the iteration
  //switch the pointer from next to point to the prev node
  //move prev node to current node
  //move current node to next node

  //return prev

  if (!head1) return;

  let prev = null;
  let current = head1;

  while (current !== null) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
}
