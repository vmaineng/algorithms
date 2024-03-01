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



function bmi(weight, height) {
  //received integers for weight and height
  //return "underweight" if bmi <= 18.5, "normal" if bmi <= 25, "overweight" if <= 30, "obese"
  // bmi(32) => 'obese', bmi(28) => "overweight"
  
  let bmiCalc = weight / Math.pow(height, 2)
  
  if (bmiCalc < 0) return "Invalid Number. Try Again!"
  
  if (bmiCalc <= 18.5) {
    return "Underweight"
  } else if (bmiCalc > 18.5 && bmiCalc <= 25.0){
    return "Normal"
  } else if (bmiCalc > 25 && bmiCalc <= 30.0) {
    return "Overweight"
  } else {
    return "Obese"
  }
}

function fakeBin(x){
  //received a string of integers
  //return a new string of 0 if the digit is less than 5, and 5 and above is replaced with a 1
  //'038509237849' => '001101001101'
  
  
  //create a new string
  //iterate through the string
  //look at each value
  //check to see if the value is < 5, turn it into a 0, add it to the new string
  //else, > 5, turn it in a 1, add it to the new string
  
//   let replaceString = "";
  
//   for (let i = 0; i < x.length; i++) {
//     if (parseInt(x[i]) < 5) {
//       replaceString += '0'
//     } else {
//       replaceString += '1'
//     }
//   }
// return replaceString

//grabbed the string, split on "", look through each number to see if < 5, turn it to 0, else turn 1, then join back with strings
return x.split("").map((n) => n < 5 ? 0 : 1).join('')
}

//O(n) = time
//O(n) = space


function rr(head){
  //receive the head of a linked list
  //return the list reversed
  //1 -> 2 -> 3 -> null => 3-> 2 -> 1 -> null

  //create a prev node and set it to null (empty space)
  //take the head as current
  //traverse through the nodes
  //capture the next node
  //switch the pointer to prev node

  //return the node next to dummy

  if (!head) return null;

  let prev = null;
  let current =head;

  while (current !== null) {
    const next = current.next;
    current.next = prev;
    prev = current; //! move the previous to current first
    current = next;
    
  }
  return prev;
}

function groupAna(strs) {
  //receive an array of strings
  //return anagrams of word group together back in an array
  //['jum','iop', 'ewr','muj'] => [['jum','muj'], ['iop'], ['ewr']]

  //if string is less than one, return the string 

  //create an object to store the words sorted together
  //look through the words
  //and add in the words
  //return back the values in an array format

  if (strs.length === 1 || !strs.length) return [strs];

  let anagramObj = {};

  for (let word of strs) {
    let sortedWord = word.split('').sort().join("");

    if (!anagramObj[sortedWord]) anagramObj[sortedWord] = []
    anagramObj[sortedWord].push(word)
  }
  return Object.values(anagramObj)
}

function substringRepeat(s) {
  //receive a string
  //return the max length with no repeating chars
  //'igloo' => 'iglo' => 4

  //create an object to store values
  //look through the strings
  //if a value exists already, then grab the length

  //edge case: if s is empty, return 0
  if (!s) return 0; 

  
  let length = 0; 
  let subValues = {};
  let left = 0;

 for (let i = 0; i < s.length; i++) {
    const value = s[i]
    if (subValues[value] >= left) {
      left = subValues[value] + 1
      console.log(left, subValues)
    }
    subValues[value] = i; 
    length = Math.max(length, (i - left + 1))
  }
return length;
}

var lengthOfLongestSubstring = function(s) {

  if (!s) return 0; 
  
   let answer = new Set(); 
   let length = 0 ;
  let left = 0; 
  //create a set
  //look through each element
  //if an element has been found that exists in set,
  //decrease the left one
  //add element from the right
  //look at window size
  
  for (let i = 0; i < s.length; i++) {
      while (answer.has(s[i])) {
          answer.delete(s[left])
          left++
      }
      answer.add(s[i])
      length = Math.max(length, answer.size)
  }
  return length;
  }

  const repeatChar= (s, k) => {
    //receive a string and an integer of how many times you can switch out a char
    //return the max length of how many times a character can be switched out
    //'ROAMAN', 2 => 'ROAAAA' => 4

    //edge case: if the amount of operations of switching exceeds the s's length;
    //if s.length is one and k is greater than or equal to 1, return length of one

    //keep track of length, count of characters seen, and store the chars seen
    //loop through string, keep track of the values seen

    //make sure the amount of operations switch does not exceed k times,
    //if so, pull back from the left window side to keep looking at the right side;
    
    let seenValues = {};
    let count = 0;
    let maxLength = 0; 

   let left = 0;
   let right = 0;

   while (right < s.length) {
    const rightChar = s.charAt(right);
    seenValues[rightChar] =  seenValues[rightChar] + 1 || 1
    count = Math.max(count, seenValues[rightChar])

    if ((right - left + 1) - count > k) {
      const leftChar = s.charAt(left);
      seenValues[leftChar] -= 1
      left++
    }
    maxLength = Math.max(maxLength, (right - left + 1))
    right++
   }
   return maxLength;
    
  }

  const checkArr = (array) => {
    return array.filter((ele) => typeof ele === 'number')
  }

  // console.log(checkArr([1,2,3, 'a', 'b']))

  const mergeSortedLL = (head1, head2) => {
    //receive two sorted linked lists
    //return one linked list back sorted;

    //take the first node from head1 as current node
    //if the value of the first node is < second node,
    //add in first node
    //then add in second node from second head
    //add any remaining from head1, or head2

    let dummy = new ListNode(); // ! add in dummy node b/c unsure of which head is the smaller value
    let tail = dummy;
    let current = head1;
    let current2 = head2; 

    if (!current1) return current2; // ! add in edge cases
    if (!current2) return current1; // ! add in edge cases

    while (current !== null & current2 !== null) {
      if (current.val < current2.val) {
        tail.next = current;
        current = current.next;
      } else {
        tail.next = current2;
        current2 = current2.next;
      }
      tail = tail.next;
    }

    if (head1) return tail.next = head1;
    if (head2) return tail.next = head2;

    return tail;
    
  }

  function DNAtoRNA(dna) {
    //string of uppercase of 'G', 'C', 'A', 'T'
    // returns an RNA sequence from the given DNA sequence
    //'GACGT' => 'GACGU'
    
    //iterate through the string
    //if the char is a T, replace it with a U
    //return the new string
    
    let newString = dna.split("")
    
    for (let i = 0; i < newString.length; i++) {
      if (newString[i] === 'T') {
        
        newString[i] = newString[i].replace('T', 'U') //! need to assign back to newString[i]
        console.log(newString[i]) // with strings, have to reassign back to original ones
      }
    }
    return newString.join("")
  }

  console.log(DNAtoRNA('TTT'))

  function DNAtoRNA(dna) {
    //string of uppercase of 'G', 'C', 'A', 'T'
    // returns an RNA sequence from the given DNA sequence
    //'GACGT' => 'GACGU'
    
    //iterate through the string
    //if the char is a T, replace it with a U
    //return the new string
    
    let newString = dna.split("")
    let replaceString = ""
    
    for (let i = 0; i < newString.length; i++) {
      if (newString[i] === 'T') {
        replaceString += "U"
      } else {
        replaceString += newString[i]
      }
    }
    return replaceString
  //   return dna.toUpperCase().replace(/T/g, 'U')
  }

  function reverseRecuLL(head, prev= null) {
    //base case: if head is null, return the previous node, exit the loop
    //recall the function: 
    //capture the next node
    //assign pointer to prev node
    //call function again on prev and next

    if (head === null) return prev; // ! return previous node
    const next = head.next;
    head.next = prev;
    return reverseRecuLL(next, head)
  }

  //121
  return num.toString().split('').reverse().join("") === num.toString();

  function checkParen(string) {
//receive a string of parenthesis
//return true if there are pairs, else return false
//'{})()' => false

//create an object with opening paren as key and closing paren as value

//iterate through the string
//add the paren to the stack if it is opening
//else check if it is a closing 
  //then check if there's any element in the stack
//return if the stack is empty

let parenPairs = {
  '(' : ')',
  '{' : '}',
  '[' : ']'
}

let stack = [];

for (let char of string) {
  if (parenPairs[char])
}


  }


for (let i = 0; i < string.length; i++) {
  if (string[i] === '(' || string[i] === '{' || string[i] === '[' ) {
    stack.push(string[i])
  } else if (string[i] === ')' || string[i] === '}') {
    if (stack.length >0)
  }

  const reverseSeq = n => {
    //receive an integer
     //return an array of integers from n to 1 (reversed direction)
     //n = 4  => [4, 3, 2, 1]
     
     //create an array
     //start at n, add to the array
     //return the array
     
     let answer = [];
     for (let i = n; i > 0; i--) {
       answer.push(i)
     }
   return answer
   };