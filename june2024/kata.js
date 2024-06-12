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
