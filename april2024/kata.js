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

const doPillars = (pillars, distance, width)  => {
//receive amoutn of pillars, distance in meters, width in cms
//return the distance between the first and the last pillar
}

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
  for (let day in month)  {
    if ([month][day] === "Nice") {
      niceCount++
    } else {
      naughtyCount++
    }
  }
}

if (niceCount > naughtyCount) {
  return "Naughty!"
} else {
  return "Nice!"
}
}

function correct(string)
{
	//receive uppercase strings with numbers
  //return the answers back in uppercase letters
  //"K0REA" => "KOREA"
  
  //if the char is a 5, turn it into an S
  //if the char is a 0, turn it into a O
  //if the char is a 1, turn it into a I
  
  let stringArray = string.split("");
  let correctedString = "";
  
  for (let i = 0; i <= stringArray.length -1; i++) {
    if (stringArray[i] === '5') {
    correctedString += "S"
  } else if (stringArray[i] === '0') {
    correctedString += "O"
  } else if (stringArray[i] === '1') {
    correctedString += "I"
} else {
  correctedString += stringArray[i]
}
}
return correctedString
  }