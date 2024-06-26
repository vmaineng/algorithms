function arrayPlusArray(arr1, arr2) {
  //add arr1 and arr2 together in one array
  //use reduce method on it
  return arr1.concat(arr2).reduce((accum, cv) => accum + cv, 0);
}

function minMax(arr) {
  //receive an array of integers
  //return [min, max] number from the array
  //[5,6,3, 4, 0] => [0, 6]

  //edge case: if the length is one, return it as min and max

  //spread out the numbers for min, and max
  //return it as an array

  if (arr.length === 1) return [arr[0], arr[0]];

  let min = Math.min(...arr);
  let max = Math.max(...arr);
  return [min, max];

  //return [Math.min(...arr), Math.max(...arr)]
}

function doubleChar(str) {
  //receive a string
  //return a new string with double the characters
  //'Super' => 'SSuuppeerr'

  //iterate through string
  //repeat the same digit
  //return new string

  let doubleStr = "";

  for (let char of str) {
    doubleStr += char.repeat(2);
  }
  return doubleStr;
}

function dontGiveMeFive(start, end) {
  //receive an integer for start and end
  //return the total amount of all numbers with no 5 in it
  //Five(8, 16) => 8, 9, 10, 11, 12, 13, 14, 16 => 7

  //initialize a count to keep track of the numbers seen
  //iterate through starting at start to the end
  //if number does not have a five, add to count
  //return count

  let count = 0;

  for (let i = start; i <= end; i++) {
    // 1, 2, 3, 4, 6, 7, 8, 9
    // i
    let stringNum = i.toString();
    if (!stringNum.match(/5/)) {
      count++;
    }
  }
  return count;
}

function bonusTime(salary, bonus) {
  // receiving salary (number), boolean for bonus
  //return the salary + bonus if bonus is true, else return the salary
  //(15000, false) => 15000
  //(20000, true) => 20000 * 10 => 200000

  if (bonus === true) {
    let newSalary = salary * 10;
    return "\u00A3" + `${newSalary}`;
  } else {
    return "\u00A3" + `${salary}`;
  }
}

// write the function isAnagram
var isAnagram = function (test, original) {
  //receive string of chars for test and original
  //see if they are anagrams if each other, return true, if they are
  //else return false
  //(happy, pappy) => false

  //sort both words
  //see if they both start with same letters
  //return false

  //else return true after searching entire string

  return (
    test.toLowerCase().split("").sort().join("") ===
    original.toLowerCase().split("").sort().join("")
  );

  //   let sortedTest = test.split("").sort().join("").toLowerCase();
  //   let sortedOriginal = original.split("").sort().join("").toLowerCase();

  // console.log(sortedOriginal, sortedTest)

  //   for (let j = 0; j < sortedOriginal.length; j++) {
  //     if (sortedOriginal[j] !== sortedTest[j]) {
  //       console.log(sortedOriginal[j], sortedTest[j])
  //       return false
  //     }
  //   }
  //   return true
};

function sumStr(a, b) {
  //receive string of integers
  //return the sum in string format
  //("4", "8") => "12"

  //turn the string into number
  //add them up
  //return the sum in string format

  if (b === "" && a === "") return "0";

  let sum = 0;

  if (a === "") {
    sum = 0 + parseInt(b);
  } else if (b === "") {
    sum = 0 + parseInt(a);
  } else {
    sum = parseInt(a) + parseInt(b);
  }
  return sum.toString();

  //return String(Number(a) + Number(b))
}

function oddCount(n) {
  //receive a whole integer
  //return how many odd numbers are below n
  //oddCount(13) => [1, 3, 5, 7, 9, 11] => 6

  //keep an oddCount
  //iterate up to n
  //if not mod by 2, increment oddcount
  //return oddcount

  //   let oddTotal = 0;

  //   for (let i = 1; i < n; i += 2) {

  //       oddTotal += 1

  //   }
  // return oddTotal;

  return Math.floor(n / 2);
}

//return string.split("").reduce((acc, cv) => cv + acc, "")

function isPalindrome(x) {
  // receive strings
  //return true if it's a plaindrome,e lse false
  //'happy' => false

  //take string x, reverse it, and see if it's still the same as x
  //reversed === original

  let revWord = x.toLowerCase().split("").reverse().join("");

  //   console.log(revWord, x) //abbA, Abba

  return revWord === x.toLowerCase();
}

function sumDigits(number) {
  //receive integers
  //return the sum of all digits included
  //-342 => -3 + 4 + 2 => 1

  //turn the numbers into string
  //split them
  //parseInt them to add them up
  //and return the number back

  let sum = 0;

  let numString = Math.abs(number).toString();

  for (let i = 0; i < numString.length; i++) {
    console.log(numString[i]);
    sum += parseInt(numString[i]);
  }
  return sum;
}

String.prototype.toAlternatingCase = function () {
  // Define your method here :)
  //this is a method
  //return opposite of the letter; if it's uppercase, make it lowercase and vice versa
  //'jUmp around'.toAlternatingCase => 'JuMP AROUND'

  //if string is empty, return empty string
  //split string,
  //iterate through it
  //if lowercase, make it uppercase
  //else make it lowercase
  //return string

  let newStr = "";
  //   let stringSplit = this.split(" ")
  for (let i = 0; i < this.length; i++) {
    if (this[i] === this[i].toLowerCase()) {
      newStr += this[i].toUpperCase();
    } else {
      newStr += this[i].toLowerCase();
    }
  }
  return newStr;

  //return this.split("").map((str) => str === str.toLowerCase() ? str.toUpperCase : str.toLowerCase()).join("")
};

function expressionMatter(a, b, c) {
  //receive 3 integers
  //return max total maount using +, *, and () once
  //(2, 3, 4) =>
  //2 * (3 + 4) => 2 * 7 = 14
  //2* 3 * 4 => 24

  //edge case: if number is not sorted in order, return can't do

  //initialize a max sum

  //if a * (b + c), take the math sum of this one
  //if (a * b * c), record as max sum

  let output = [];
  output.push(a * b * c);
  output.push(a * (b + c));
  output.push(a + b * c);
  output.push((a + b) * c);
  output.push(a + b + c);

  return Math.max(...output);

  //return Math.max(
  //       a + b + c,
  // a * b * c,
  // a * (b + c),
  // (a + b) * c,
  // a + b * c,
  // a * b + c,
  //     )
}

function shortcut(string) {
  //receive a string of chars
  //return string with no vowels, if lowercase
  //if it's uppercase, vowels can stay
  //"JUMP" => "JUMP"
  //"run" => "rn"

  //create an array of lowercase vowels
  //iterate through string
  //see if any of char matches the array of lowecase vowels
  //remove it
  //else return string as is

  let lowercaseVowels = ["a", "e", "i", "o", "u"];

  let stringArray = string.split("");

  let newStr = "";

  for (let i = 0; i < stringArray.length; i++) {
    if (!lowercaseVowels.includes(stringArray[i])) {
      newStr += stringArray[i];
    }
  }
  return newStr;

  //return string.split("").filter((str) => !lowercaseVowels.includes(str)).join("")
}

const doPillars = (pillars, distance, width) => {
  //receive amoutn of pillars, distance in meters, width in cms
  //return the distance between the first and the last pillar
};

const naughtyOrNice = (data) => {
  //receive an obj instead in obj
  //return "Naughty!" or "Nice!" based on total amts

  //iterate through the data
  //then iterate through the month
  //then grab the dates (key)
  //tally up the total amount based on wehther the value is "Naughty" or "Nice"

  let naughtyCount = 0;
  let niceCount = 0;

  for (let month in data) {
    for (let day in month) {
      if ([month][day] === "Nice") {
        niceCount++;
      } else {
        naughtyCount++;
      }
    }
  }

  if (niceCount > naughtyCount) {
    return "Naughty!";
  } else {
    return "Nice!";
  }
};

function correct(string) {
  //receive uppercase strings with numbers
  //return the answers back in uppercase letters
  //"K0REA" => "KOREA"

  //if the char is a 5, turn it into an S
  //if the char is a 0, turn it into a O
  //if the char is a 1, turn it into a I

  let stringArray = string.split("");
  let correctedString = "";

  for (let i = 0; i <= stringArray.length - 1; i++) {
    if (stringArray[i] === "5") {
      correctedString += "S";
    } else if (stringArray[i] === "0") {
      correctedString += "O";
    } else if (stringArray[i] === "1") {
      correctedString += "I";
    } else {
      correctedString += stringArray[i];
    }
  }
  return correctedString;
}

//return array.reduce((acc, cv) => acc * cv)
//return array.match(/brown/);

//grab total sum
//[1, 2, 3, 4, 5] ==> 15
//grab last item
//
//const lastItem = array[array.length - 1];
//return lastItem * (lastItem + 1) / 2 ==> 15

function duplicateCount(text) {
  //receive a string of chars and numbers
  //return the count of chars and numbers that appear more than once
  //'hello' => 1 => 'l'

  //create an object
  //iterate through the string
  //if the char is seen, add 1 to it

  //iterate through the object, check the amount of chars that > 1
  //return the amount of chars

  //edgecase: if string is empty, return 0

  if (text.length === 0) return 0;

  let lowercaseString = text.toLowerCase();

  let seenValues = {};
  let total = 0;

  for (let char of lowercaseString) {
    seenValues[char] = (seenValues[char] || 0) + 1;
    //     console.log(seenValues)
  }

  for (let key in seenValues) {
    if (seenValues[key] > 1) total += 1;
  }
  return total;
}

//time: O(n) - looping through every data structure once
//space: O(n) - creating a new object

function reverseList(list) {
  //receive an array of integers - unsorted
  //return the list reversed back
  //[6, 3, 8] => [ 8, 3, 6]

  //create a new array
  //iterate through the current list
  //add from the end to the new array
  //return the new array

  //time: O(n)
  //space: O(n) - creating a new array

  // let reversedArray = [];

  //   for (let i = list.length - 1; i >= 0; i--) {
  //     reversedArray.push(list[i])
  //   }

  // return reversedArray

  //space: O(1) - reverse in place
  return list.reverse();
}

function noOdds(values) {
  // receive an array of values of integers
  //return values in order that are not odd
  //[2,3, 4, 5] => [2, 4]

  //edge case: if there's only 1 element in the array, then have to check if you mod it by 2, it equals 0 and return the value

  //create an array

  //iterate through the values array
  //check if the remainder % 2 is 0, then it's an even number
  //push to the array
  //return the array

  //   let evenArray = []

  // for(let i = 0; i < values.length; i++) {
  //   if (values[i] % 2 === 0) {
  //     evenArray.push(values[i])
  //   }
  // }
  // return evenArray

  //optimized:
  //use .filter?

  return values.filter((ele) => ele % 2 === 0);
}

function solution(number) {
  //receive an integer to iterate up to
  //return the sum of multiples of 3 or 5
  //(5) => 3, 5 => 8

  //edge case: if number is negative, return 0
  if (number < 0) return 0;

  //intialize a sum
  //iterate up to number
  //check if it is a multiple of 3 & 5,
  //add to sum
  //check if it is multiple of 3
  //add to sum
  //check if it is a mutiple of 5
  //add to sum

  let sum = 0;

  for (let i = 1; i < number; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      sum += i;
    } else if (i % 3 === 0) {
      sum += i;
    } else if (i % 5 === 0) {
      sum += i;
    }
  }
  return sum;

  //time: o(n) - iterate through each number once
  //space: O(1) - sum is changing;
}

function fixTheMeerkat(arr) {
  //receive an array of 3 strings: "tail", "body", "head"
  //return it back in order of ["head", "body", "tail"]

  //["body", "tail", "head"] => ["head", "body", "tail"]

  //create a new array
  //iterate through the current array
  //check if the element is equal to head
  //push it into the array
  //then check if next element is equal to body, push in body
  //then do same thing for tail

  return arr.reverse();
}

function reverseLetter(str) {
  //receive a string of chars and numbers
  //return a string back reversed ; only with chars
  //"3425se324see" => "eeses"

  //filter them out to equal only chars
  //then reverse it

  return str
    .replaceAll(/[^a-z]/gi, "")
    .split("")
    .reverse()
    .join("");
}

function peopleWithAgeDrink(old) {
  //receive an age
  //return the statement on the age given
  //drink(12) => "drink toddy"

  //check if age is < 13, "drink toddy", else if age is > 13 and < 17, "drink coke"
  //if age is > 17, "drink beer", else over 21, "drink whisky"

  return old < 15
    ? "drink toddy"
    : old > 14 && old < 18
    ? "drink coke"
    : old > 18 && old < 21
    ? "drink beer"
    : "drink whisky";
}

for (let i = 0; i < this.length; i++) {
  // If any character is lowercase, return false
  if (this[i] !== this[i].toUpperCase()) {
    return false;
  }
}
// If all characters are uppercase, return true
return true;

function wordsToMarks(string) {
  ////receive an array of strings
  //return the total value dervied from the strings in the order of the alphabet
  //'hi' => 8 + 9 = 17

  //create an object that holds a - z with the matching value in the alphabet
  //iterate through the strings
  //total up the value

  let charMatch = {
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

  let sum = 0;

  for (let char of string) {
    if (charMatch[char]) {
      sum += charMatch[char];
    }
  }

  return sum;
}

function gooseFilter(birds) {
  var geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"];
  //receive an array of strings of birds
  // return an array containing all of the strings in the input array except those that match strings in geese
  //['African', "Mallard", 'Crested', 'Roman Tufted'] => ["Mallard", "Crested"]

  //iterate through the array of birds
  //check if the word does not contains any of the geese
  //add them to the new array
  //return new array

  let noGeese = [];

  // for (let i = 0; i < birds.length; i++) {
  //   if (!geese.includes(birds[i])) {
  //     noGeese.push(birds[i])
  //   }
  // }
  // return noGeese

  return birds.filter((bird) => !geese.includes(bird));
}

function longestConsec(strarr, k) {
  //receive an array of strings, and an integer dictating how many strings you can connect together
  //return the longest length string
  //['hi', 'hello', 'char'], 2 => ['hellochar']

  //keep track of length of k strings together
  //iterate through strarr array
  //add the next string
  //until k times
  //track the length
  //return the length

  if (strarr.length === 0 || k > strarr.length || k <= 0) {
    return "";
  }

  let maxStr = "";
  let newStr = "";

  for (let i = 0; i < strarr.length; i++) {
    newStr = strarr.slice(i, i + k).join("");
    if (newStr.length > maxStr.length) {
      maxStr = newStr;
    }
  }
  return maxStr;
}

let canBeCorrect = true;
let canBeIncorrect = true;

for (let i = 0; i < answerKey.length; i++) {
  if (answerKey[i] !== "_" && answerKey[i] !== studentAnswers[i]) {
    canBeCorrect = false;
  }
  if (answerKey[i] !== "_" && answerKey[i] === studentAnswers[i]) {
    canBeIncorrect = false;
  }
}

return canBeCorrect || canBeIncorrect;

function moveZeros(arr) {
  //receive an array of multiple data types
  //return the same array back in order, but with the 0's placed at the end
  //['hi', 3, 0, 2, 0, true] => ['hi', 3, 2, true, 0 , 0]

  //edge case: if array is empty or only has one element

  //create two empty arrays = one to hold 0, one to hold everything else
  //iterate through the array
  //if 0, push into the array that holds zero
  //else push to the other array
  //return the array added back together with the 0's second

  //time: O(n); iterate through arr at least once
  //spacee: O(N); creating two new arrays

  let zeroArray = [];
  let restArray = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      zeroArray.push(arr[i]);
    } else {
      restArray.push(arr[i]);
    }
  }
  return restArray.concat(zeroArray);
}

function getRealFloor(n) {
  //receive an integer
  //return the floor in European style
  //floor(18) => 16

  //if the floor is less than 0, return the actual num
  //if the floor is less 13, and between 1, reduce it by 1
  //else if anything is over 13, reduce it by 2

  if (n <= 0) {
    return n;
  } else if (n >= 1 && n < 13) {
    return n - 1;
  } else {
    return n - 2;
  }
}

function wave(str) {
  //receive a string
  //return an array back with strings and in each string, a wave is occuring starting from first letter to the last where it's capitalized first
  //wave("ate") => ['Ate', 'aTe', 'atE']

  //split the string
  //create an array to store the wave of strings
  //iterate through each char
  //for each round we go through,
  //capitalize that letter
  //add back to the string
  //return the array back

  let answerArr = [];

  for (let i = 0; i < str.length; i++) {
    if (str[i] !== " ") {
      answerArr.push(str.slice(0, i) + str[i].toUpperCase() + str.slice(i + 1));
    }
  }

  return answerArr;
}

function enough(cap, on, wait) {
  // receive 3 integers
  //return 0 if there's enough space, else, return the number of passengers that he can't take
  //enough(15, 5, 20) => Can't fit 5 people

  //if on + wait > cap, cap - on + wait
  //else return 0

  if (on + wait > cap) {
    return Math.abs(cap - (on + wait));
  } else {
    return 0;
  }
}
function mxdiflg(a1, a2) {
  //receive an array of strings
  //return the max length from a1 - max length from a2 (integer)

  //if a1 and/or a2 are empty, return -1

  //iterate through the array, find the length of each strings
  //take the longest lenght from a1 - longest length from a2

  if (!a1 || !a2) return -1;

  let longestA1 = a1.map((str) => str.length);
  let longestA2 = a2.map((str) => str.length);

  console.log(Math.max(...longestA1));
  console.log(Math.max(...longestA2));

  return Math.max(
    Math.max(...longestA1) - Math.min(...longestA1),
    Math.min(...longestA1) - Math.max(...longestA2)
  );
}

function solution(a, b) {
  // receive two strings of numbers or chars
  //return the shorter string on the outside and longer string on the inside
  //solution("45", "2") => "2452"

  //create a new string
  //compare the string's length
  //if the string's length is shorter, add that one in first
  //then add in the other one, then add in the first one again

  let newString = "";

  if (a.length < b.length) {
    newString = a + b + a;
  } else {
    newString = b + a + b;
  }

  return newString;
}

function goodVsEvil(good, evil) {
  //receive two strings of numbers
  //return good win if good total > evil total, else if evil total > good evil, return Evil wins
  //or if tie, return no victor
  //goodVsEvil('1 1 1', '1 0 1') => "Battle Result: Good triumphs over Evil"

  //turn the strings into an array
  //find the sum (by using reduce function)
  //compare the sum of two teams
  //return the result based on the total

  const goodStrengths = [1, 2, 3, 3, 4, 10]; // Strengths of good characters
  const evilStrengths = [1, 2, 2, 2, 3, 5, 10]; // Strengths of evil characters

  const goodTotal = good
    .split(" ")
    .reduce((acc, cv, index) => acc + cv * goodStrengths[index], 0);
  const evilTotal = evil
    .split(" ")
    .reduce((acc, cv, index) => acc + cv * evilStrengths[index], 0);

  if (goodTotal > evilTotal) {
    return "Battle Result: Good triumphs over Evil";
  } else if (evilTotal > goodTotal) {
    return "Battle Result: Evil eradicates all trace of Good";
  } else {
    return "Battle Result: No victor on this battle field";
  }
}

function finalGrade(exam, projects) {
  //receive two integers (exam, projects)
  //return 100 (if exam > 90 or if a number of completed projects > 10)
  //else return 90 (if exam > 75 and if completed projects >= 5)
  //else return 75 (if exam > 50 and if completed projects >= 2)
  //else return 0

  return exam > 90 || projects > 10
    ? 100
    : exam > 75 && projects >= 5
    ? 90
    : exam > 50 && projects >= 2
    ? 75
    : 0;
}

function findOutlier(integers) {
  //receive an array of integers
  //return the outlier value
  //[3, 9, 13, 4] => 4

  //keep track of odds and evens
  //if evens are greater than odds, return the odds
  //else return the evens

  //edge case: if length is less than 3

  let oddCount = [];
  let evenCount = [];

  for (let i = 0; i < integers.length; i++) {
    if (integers[i] % 2 === 0) {
      evenCount.push(integers[i]);
    } else {
      oddCount.push(integers[i]);
    }
  }

  if (evenCount.length > oddCount.length) {
    return oddCount[0];
  } else {
    return evenCount[0];
  }
}

let naughtyCount = 0;
let niceCount = 0;

for (let month in data) {
  for (let day in data[month]) {
    if (data[month][day] === "Naughty") {
      naughtyCount++;
    } else {
      niceCount++;
    }
  }
}

return niceCount > naughtyCount ? "Nice!" : "Naughty";

function unusualFive() {
  //receive nothing
  //return 5 w/o using any 0123456789*+-/
  // unusualFive() => 5
  //create a string of five chars
  //return the length
  const str = "=====";
  return str.length;
}

function humanReadable(seconds) {
  //receive a number for seconds
  //return the time in a readable human format (HH: MM : SS)

  //80 => '00:01:20'

  //calculate the seconds received
  //for hour: divide by 3600
  //for minutes: divide by 60
  //for seconds: mod by 60 to see what remainder is

  let hour = Math.floor(seconds / 3600);
  let minutes = Math.floor((seconds % 3600) / 60);
  let second = seconds % 60;

  if (hour < 10) {
    hour = "0" + hour;
  }
  if (minutes < 10) {
    minutes = "0" + minutes;
  }

  if (second < 10) {
    second = "0" + second;
  }

  return `${hour}:${minutes}:${second}`;
}

function nameShuffler(str) {
  //receive a string with space
  //return the words in string swapped
  //'Mary Joe' => 'Joe Mary'

  //create a new string
  //iterate up to a space
  //then add tot he next one
  //split on space
  //console.log(str.split(" ")) //['john', 'McClane']
  //let splitString = str.split(" ");
  //return splitString[1] + " " + splitString[0];

  return str.split(" ").reverse().join(" ");
}

String.prototype.toJadenCase = function () {
  //receive a string
  //return the string back with first letter of every word capitalized
  //"hi, how you doing?" => "Hi, How You Doing?"

  //create a new string
  //split the string on spaces
  //iterate through the string
  //take the first letter of the word and capitalize
  //add in the rest of the letter in the word
  //add to the string

  let splitString = this.split(" ");

  for (let i = 0; i < splitString.length; i++) {
    splitString[i] = splitString[i][0].toUpperCase() + splitString[i].slice(1);
  }
  return splitString.join(" ");
};

function distinct(a) {
  //receive an array of integers
  //return an array back of unique integers
  //[3, 5, 6,5] => [3, 5, 6]

  //edge case: if the element only has one, return the array back
  if (a.length === 1) return a;

  //create an array
  //iterate through the a array,
  //check if the next element to it is !== to the second element in the array
  //push to the array
  //return the array

  let answer = new Set(a);
  return Array.from(answer);
}

function well(x) {
  //get an array of 'good', 'bad'
  //return 'Publish' = if one or two 'good'
  //else return 'I smell a series' if > 'good' > 2
  //else 'return 'Fail'

  let goodCount = 0;
  for (let i = 0; i < x.length; i++) {
    if (x[i] === "good") {
      goodCount++;
    }
  }

  if (goodCount === 0) {
    return "Fail!";
  } else if (goodCount > 0 && goodCount < 3) {
    return "Publish!";
  } else {
    return "I smell a series!";
  }
}

function howManyLightsabersDoYouOwn(name) {
  //receive a string for a name with no space
  //return 18 if your name is Zach, otherwise it's 0
  //("Joe") => 0; ("Zach") => 18

  //if name is not Zach, return 0, else return 18
  return name !== "Zach" ? 0 : 18;
}

function checkExam(array1, array2) {
  //receive two same lengths arrays
  //return a total sscore
  //['a', 'b', 'b'], ['a','','c'] => +4, +0, -1 => 3

  //create a score
  //iterte through student's answer
  //check if the same value at the same index are equal, then +4
  //else check if they do not equal each other then, -1
  //else check if the answer's blank, return +0
  //return score

  let score = 0;

  for (let i = 0; i < array2.length; i++) {
    if (array2[i] === "") {
      score += 0;
    } else if (array2[i] === array1[i]) {
      score += 4;
    } else if (array2[i] !== array1[i]) {
      score -= 1;
    }
  }
  return score > 0 ? score : 0;
}

function checkParent(s) {
  //receive a string of s
  //return true if matching pairs, else false
  //']()' => false b/c can't start with closing brackets

  //create a stack to hold the opening parens
  //itereate through
  //check if it is an open one
  //add to the stack
  //if it is a closing one
  //check if the stack is not empty
  //pop it off if it matches the closing
  //if it doesn't, return false
  //otherwise return true

  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(s[i]);
    } else {
      if (!stack.length) {
        if (stack.pop() !== s[i]) {
          return false;
        }
      }
    }
  }
  return true;
}

function addLength(str) {
  //receive a string of words with spaces
  //return an array with the length of the word with a space next to the word
  //'hi, i'm hungry" => ["hi 2", "i'm 2", 'hungry 6']

  //split the strings by spaces => which converts into an array
  //map through the array and grab the length
  //return the str + length in one string

  let splitString = str.split(" ");
  //   splitString.map((word) =>
  //     word + ' ' word.length
  //)

  let newAnswer = [];
  for (let i = 0; i < splitString.length; i++) {
    //[apple, ban]
    let length = splitString[i].length;
    let newItem = splitString[i] + " " + length;
    newAnswer.push(newItem);
  }
  return newAnswer;
}

function plural(n) {
  //receive a number
  //return true if pluaral is needed, else return false
  //plural (4) =>true

  //if greater than 1, return true, else return false

  return n === 1 ? false : true;
}
function mouthSize(animal) {
  //receive a string of an animal
  //return a string of "small" if meets alligator, otherwise return "wide"
  //"mouse" => "wide"
  //"alligator" => "small"

  return animal.toLowerCase() === "alligator" ? "small" : "wide";
}

String.prototype.toJadenCase = function () {
  //receive a string with words and spaces
  //return the first letter of each word capitalize
  //"what's new with you" => "What's New With You"

  //split the string on spaces to grab each word
  //iterate through the words
  //capitalize the first letter
  //and add on the rest of the letters in the strings
  //join back together on space

  let splitString = this.split(" ");
  // console.log(splitString) //[
  //   'How',     'can',
  //   'mirrors', 'be',
  //   'real',    'if',
  //   'our',     'eyes',
  //   "aren't",  'real'
  // ]

  for (let i = 0; i < splitString.length; i++) {
    //"how"
    splitString[i] = splitString[i][0].toUpperCase() + splitString[i].slice(1);
  }

  return splitString.join(" ");
};

const gauss = (array) => {
  const last = array[array.length - 1];

  return (last * (last + 1)) / 2;
  3 * 2;
  //[1,2, 3] = 6
};

function removeSmallest(numbers) {
  //receive an array of integers, not sorted
  //return an output array with min val removed and not mess up orders of other values
  //[3, 2, 5, 56, 7] => [3, 5, 56, 7]

  //sort the array
  //find min value index in numbers
  //splice it out
  //return the array back

  const copyNumbers = numbers.slice(0);
  const minVal = numbers.indexOf(Math.min(...numbers)); //findng index of min numbers
  copyNumbers.splice(minVal, 1);
  return copyNumbers;
}

function feast(beast, dish) {
  //receive two strings for beast and dish
  //return boolean if first letter of dish is same as first letter of beast's
  //feast(rooster, pig roast) => false
  //feast(cat, candy) => true

  //check if the first letter of beast is equal to first letter in dish
  //return true, else return false

  if (
    beast[0] === dish[0] &&
    beast[beast.length - 1] === dish[dish.length - 1]
  ) {
    //   console.log(beast[beast.length -1 ])
    return true;
  } else {
    return false;
  }

  //return dish.starts(beast[0]) && dish.ends(beast[beast.length - 1]);
}

function replace(s) {
  //receive a string of letters and chracters
  //return the string back where vowels (upper and lower) are replaced with a '!'
  //'jump' => 'j!mp'

  //split string, if it includes vowels, then replace with ! instead

  let vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];

  let sSplit = s.split(""); //['j', 'i', 'm', 'p']

  let newString = "";

  for (let i = 0; i < sSplit.length; i++) {
    if (vowels.includes(s[i])) {
      newString += s[i] = "!";
    } else {
      newString += s[i];
    }
  }
  return newString;

  //return s.replace(/aeiou/g, !)
}

//time: O(n)
//space:O(n)
