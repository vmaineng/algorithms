const longestRepeat = (s, k) => {
  //a string of letters (uppercase), and an integer of how many times you can change it
  //return the length of how many letters you can replace
  //"APPLE", 1 => "PPPLE" => 3

  //create an object to keep track of the count of letters seen
  //create a sliding window
  //go through the letters and make sure the window does not exceed k amoutn of times
  //if so, then we need to increment left window
  //decrement letter from the object
  //after checking, return the length

  //edge case: if K exceeds s, then return s length
  if (k > s.length) return s.length;

  let track = {};
  let maxLength = 0; //kkeeps track of length
  let count = 0; //keeps track of count of letters

  let left = 0;
  let right = 0;

  while (right < s.length) {
    let rightChar = s.charAt(right);
    track[rightChar] = track[rightChar] + 1 || 1;
    count = Math.max(count, track[rightChar]);

    if ((right - left + 1) - count > k) {
      let leftChar = s.charAt(left);
      track[leftChar]--;
      left++;
    }
   
    maxLength = Math.max(maxLength, right - left + 1); // keeps track of length
    right++;  // ! after capturing longest length then can move teh right side of the window
}
  return maxLength;
};

// console.log(longestRepeat("APPLE", 1));

function check(n) {
  console.log(Math.sqrt(n) % 1 )
}

console.log(check(25))

function palindromeNum(num) {
  return num.toString().split('').reverse().join('') === num.toString();
}

function fib(n) {
  return fib(n-1)
}

function twosum(num, target) {
  //create an object to store the value as key, and index as value
  //look for the difference of nums and target
  //check if object has the difference as a property
  //and return the index position
  //otherwise, store the index 

  let indexCheck = {};

  for (let i = 0; i <num.length; i++) {
    let difference = target - num[i];
    if (indexCheck.hasOwnProperty(difference)) {
      return [indexCheck[difference], i]
    } else {
      indexCheck[num[i]] = i 
    }
  }
}

function longRepeat(s, k) {
  //receive a string of uppercase characters, and an integer to represent how many times you can switch out numbers
  //return the longest substring containing the same letter
  //"JUMPPER", 3 => "JUPPPPP" => 5

  //keep count of how many letters
  //create an object to store how many values have seen, length of what you have seen
  //start at the first letter, keep adding values seen to the object
  //can shrink window from the left if K amount of switches have occured,
  //return the maxlength;

let count = 0;
let length = 0;
let seenValues = {};

let left = 0;
let right = 0;

while (left < right) {
  const rightChar = s.charAt(right);
  seenValues[rightChar] = seenValues[rightChar] + 1 || 1
  count = Math.max(count, seenValues[rightChar])

  if ((right - left + 1) - count > k) {
    const leftChar = s.charAt(left)
    seenValues[leftChar] -= 1
    left++
  }
length = Math.max(length, (right - left + 1))
right++
}
return length;

}


function checkParen(string){
//receive a string of paranethesis
//return true if paranethesis matches, else false
//"{}([)" => true

//create a stack
//push on the parenthesis
//if the parenthesis in the stack does not match the prior one, return false, otherwise, keep looking 
//return true if stack is empty

let checkStack = [];
let addParen = 0;

for (let i = 0; i < string.length;i++) {
  if (string[i] === '(') {
    checkStack.push(string[i])
  } else if (string[i] === ')') {
    if (checkStack.length > 0) {
      checkStack.pop()
    } else {
      addParen++
    }
  }
}
addParen += checkStack.length
return addParen

}

function flick(array) {
  //an array of words that gets switched to opposite when 'flick'
  //return the array with true or false
  //['aapple', 'flick', 'jump', 'roar', 'flick', 'jill'] => [true, false, false false, true]

  //set the flick to true
  //go through the words and if you see flick, switch it, return the array

  // let newArray = [];
  let flickSwitch = true

  return array.map((word) => {
    if (word === 'flick') {
      flickSwitch = !flickSwitch
    }
    return flickSwitch
  })

  // for (let i = 0; i < array.length; i++) {
  //   if (array[i] === 'flick') {
  //     flickSwitch = !flickSwitch
  //     newArray.push(flickSwitch)
  //   }
  // }
  // return newArray
}