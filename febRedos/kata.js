function multiply(a, b) {
  return a * b;
}

function simpleMultiplication(number) {
  //receive a number
  // if the output is even, return 8, otherwise 9

  //edge cases: if it's not a number

  //take the number and multiply by 8
  //if the output is even, return 8; otherwise return 9

  return number % 2 === 0 ? number * 8 : number * 9;
}

// Sum Numbers
function sum(numbers) {
  "use strict";

  //get an array of integers
  //return the sum of all the integers added
  //[-1, -2, -2, -34] => -39

  //if empty, return 0

  //create a sum
  //add up each integer in the loop
  //return the sum

  //use reduce to calculate the total

  return numbers.length > 0 ? numbers.reduce((acc, cv) => acc + cv, 0) : 0;
}

function makeUpperCase(str) {
  // receive a string of letters
  //return it uppercase
  //"hi" => "HI"

  return str.toUpperCase();
}

function isIsogram(str) {
  //receive a string
  //return true if letters are used once, else false
  //'jump' => true
  //'apple' => false

  //edge case: if string is less than 1, it is unique => true

  //iterate through the string
  //keep track of the values in a frequnecy counter

  //check if the counter has more than two values
  //return false

  //otherwise return true after checking;

  if (str.length <= 1) return true;

  let checkLetter = {};

  //PIT frequency counter:

  for (let char of str.toLowerCase()) {
    if (checkLetter[char]) {
      //if character exists already
      return false;
    } else {
      checkLetter[char] = 1;
    }
  }

  return true;

  //   for (let char of str.toLowerCase()) {
  //     checkLetter[char] = checkLetter[char] + 1 || 1
  //   }

  //   for (let values in checkLetter) {
  //   if (checkLetter[values] > 1) {
  //     return false;
  //   }
  //  }
  //   return true;

  //optimized: use a set
  return new Set(str.toLowerCase()).size === str.length;
}

function getMiddle(s) {
  //receive a string of characters
  //return the middle character(s)
  //'apple' => 'p'
  //'fork' => 'or'

  //edge case: if string is less than 1, return the str

  //find the middleIndex
  //if the string's length is even,
  //return the value before the index and after index
  //else string is odd,
  //return the char at the middle

  if (s.length <= 1) return s;

  const middleIndex = Math.floor(s.length / 2); //2

  if (s.length % 2 === 0) {
    console.log(s[middleIndex]); //r
    console.log(s.slice(middleIndex - 1, middleIndex + 1)); //or b/c // ! extract the beginning up to and exclude the letter next to middleIndex
  } else {
    return s.charAt(middleIndex);
  }
}

console.log(getMiddle("fork"));
//                     MI

function invert(array) {
  //receive an array of integers
  //return the array and invert the values
  //[-3, 0, 4, -2] > [3, 0, -4, 2]

  //edge case: if the array has no element, return the array

  //go through each number and return the absolute number

  if (!array) return 0;

  return array.map((num) => -num);
}

function hero(bullets, dragons) {
  //get integers for bullets and dragons
  //return true if he survives, else return false
  //to kill a dragon = 2 bullets

  //30, 30 => false
  //hero(15, 5) => true

  //if the amount of bullets is equal to dragson * 2, return true, else return false

  return dragons * 2 <= bullets;
}

function grow(x) {
  //receive an array with integers
  //return the sumproduct of all the integers, in order
  //[3, 4, 5, 3] => 900

  return x.reduce((acc, cv) => acc * cv);
}

function XO(str) {
  //receive a string of characters
  //return true if same amount of x's and o's, else false
  //'xOOxO' => false

  //lowercase all the letters
  //split on the x's and o's
  //check if equal lengths

  let lowercaseStr = str.toLowerCase();

  return lowercaseStr.split("x").length === lowercaseStr.split("o").length;
}


String.prototype.toJadenCase = function () {
    //receive a string with spaces and letters
    //return the first letter in each word capitalize
    
    //"how to help you today?" => 'How To Help You Today?'
    
    //split on spaces
    //iterate trhough each word and capitalize the first letter
    //return the string
    
   let words = this.split(' ') //split = turned the string into an array
   
   for (let i = 0; i < words.length; i++) {
     words[i] = words[i][0].toUpperCase() + words[i].slice(1)
   }
    
    return words.join(" ")
     
     
  };