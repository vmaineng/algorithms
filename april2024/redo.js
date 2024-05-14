function checkParen(str) {
  //receive a string of parenthesis
  //return true if they pair up, else false
  //'()()' => true

  //if paren starts with a closing bracket first, then return false;

  //create a stack
  //iterate through string
  //if it's an opening bracket, add to the stack
  //if it's a closing bracket, and if the stack is not empty
  //pop it off
  //return if stack is empty

  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(" || s[i] === "[" || s[i] === "{") {
      stack.push(s[i]);
    } else {
      //if found closing bracket
      if (
        !stack.length || //if stack is empty or if you can't find the corresponding  opening character, then return false;
        (s[i] === ")" && stack[stack.length - 1] !== "(") ||
        (s[i] === "}" && stack[stack.length - 1] !== "{") ||
        (s[i] === "]" && stack[stack.length - 1] !== "[")
      ) {
        return false;
      }
      stack.pop(); //else pop off the opening bracket
    }
  }
  return !stack.length;
}

const twoSum = (nums, target) => {
  //receive an array of numbers, target
  //return the index position
  //[3, 4, 5, 8], 9 => [1, 2]

  //create an object
  //iterate through nums array
  //look for a the difference by taking the target - current value
  //check if the object already has the value as key, then return the index positions
  //else set the index position in

  let answer = {};

  for (let i = 0; i < nums.length; i++) {
    let difference = target - nums[i];
    if (answer.hasOwnProperty(difference)) {
      return [answer[difference], nums[i]];
    } else {
      answer[difference] = i;
    }
  }
};

function revLL(head1) {
  //receive the head of a linked list
  //return the list in reverse
  // 1 -> 2 -> 3 => 3 -> 2 -> 1

  //edge case if the ll is empty, return null

  //create a prev node set to null
  //capture head as current node
  //iterate through ll
  //capture the next node
  //switch pointers from next to prev
  //push prev node to capture current node
  //then push current to next node
  //return prev node;

  if (!head1) return null;

  let prev;
  let current = head1;

  while (current !== null) {
    let next = current.next;
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev;
}

function groupAnagrams(arr) {
  //receive an array of strings
  //return an array back with anagroups in the array

  //edge case: //if array is empty, return an empty array back
  //if array has one element, return the eleement back

  //sort the strings
  //create an object
  //iterate through the sorted Strings
  //check if the key exists,
  //then add array of strings as the value
  //return the values as an array

  if (arr.length === 1 || !arr) return [arr];

  let sortedWords = {};

  for (let word of sortedArr) {
    let sortedArr = arr.split("").sort().join("");
    if (!sortedWords[sortedArr]) sortedWords[word] = [];
    sortedWords[word].push(word);
  }
  return Object.values(sortedWords);
}

function groupAna(arr) {
  //receive an array of strings
  //return an array with arrays of anagrams together

  //split the chars in arr, sort them, and join them back together
  //iterate through the sorted chars
  //create an object to store similar values seen
  //insert the original word as values, keys are the sorted word
  //return the values as an array

  let anaObject = {};

  for (let word of arr) {
    let sortedWord = word.split("").sort().join("");
    if (!anaObject[sortedWord]) anaObject[sortedWord] = [];
    anaObject[sortedWord].push(word);
  }
  return Object.values(anaObject);
}

function countVow(str) {
  //receive a string
  //return count of vowels in string
  //'window' => 2

  //create a vowels array holding all vowels
  //iterate through the string
  //if the char matches any of the vowels char
  //add to count
  //return count

  let vowelsCount = 0;

  let vowelsArray = ["a", "e", "i", "o", "u"];

  let lowerCaseStr = str.toLowerCase();

  for (let i = 0; i <= lowerCaseStr.length; i++) {
    if (vowelsArray.includes(lowerCaseStr[i])) {
      vowelsCount++;
    }
  }
  return vowelsCount;
}

const longestRepeat = (s) => {
  //receive a string of lowercase letters
  //return the maxlength of chars that are not repeating
  //'applesauce' => 'plesauc' => 7

  //create a Set to capture unique values
  //create two pointers starting at the first index
  //check if the Set has not seen the values, increase the right window
  //else if the set has it, decrease the window from the left
  //keep track of maxLength

  let uniqueChar = new Set();

  let left = 0;
  let right = 0;
  let maxLength = 0;

  while (right < s.length) {
    if (!uniqueChar.has(s[right])) {
      uniqueChar.add(s[right]);
      right++;
    } else {
      uniqueChar.delete(s[left]);
      left++;
    }
    maxLength = Math.max(maxLength, uniqueChar.size);
  }

  return maxLength;
};

function paliNum(num) {
  //receive a number
  //return true if palindrome, else false
  //34565 => false

  //convert num to string
  //use left and right pointer ; left at 1st num and right at the end num
  //check if they are not equal to each other, return false
  //return true

  let numString = num.toString();

  let i = 0;
  let j = numString.length - 1;

  while (i < j) {
    if (numString[i] !== numString[j]) {
      return false;
    }
    i++;
    j--;
  }
  return true;
}

const longSubstring = (s) => {
  //receive a string of chars
  //return max length of chars
  //'unique' => 'uniq' => 4

  //create a Set of values seen
  //iterate through string
  //check if the value exists in Set,
  //if so, delete from set and move the pointer
  //keep track of maxLength
  //return maxLength

  let uniqueVals = new Set();

  let left = 0;
  let right = 0;
  let maxLength = 0;

  while (right < s.length) {
    if (!uniqueVals.has(s[right])) {
      uniqueVals.add(s[right]);
      right++;
    } else {
      uniqueVals.delete(s[left]);
      left++;
    }
    maxLength = Math.max(maxLength, uniqueVals.size);
  }
  return maxLength;
};

function create(arr) {
  //receive an array
  //return an array with arrays + idx
  //[0, 1, 2] => [[0,1], [1,2], [2, 3]]

  //iterate through arr, capture the idx + 1
  //return the arr

  // return arr.map((ele, idx) => {
  //     const newIdx = idx + 1
  //     return "ele, newIdx"
  // })
  let newArr = [];

  for (let i = 0; i < arr.length; i++) {
    newArr.push(arr[i], arr[i + 1]);
  }
  return arr;
}

//return (goose - 1) % goose.length
//return arr.filter((ele) => typeof ele === 'number')
//return word[0].toUpperCase + word.slice(1)

//const lastEle = array.length - 1;
//return lastEle - lastEle / 1

function revLL(head, prev = null) {
  if (head === null) return prev;
  const next = head.next;
  head.next = prev;
  return revLL(next, head);
}

//return array.map((ele, idx) => {
// const newIdx = idx + 1
// return newIdx + ":" + ele
// })

function move(position, roll) {
  //receive two integers (current position, # on dice roll)
  // return the new position
  //move(4, 4) => 4 * 2 = 8 , 4 + 8 = 12

  //take the roll * 2
  //add the amount of Moves needed to current position
  //return new Position

  let amtOfMoves = roll * 2;
  return position + amtOfMoves;
}

function twoSort(s) {
  //receive a an array of strings
  //return the first string and have "***"between each of its letters
  //['hello', 'is', 'you', 'doing'] => ['doing', 'hello', 'is', 'you'] => 'd***o***i***n***g'

  //sort the array by first letter in each string
  //grab the first value in the array and split it with '***'' in between

  let sortedWords = s.sort();
  //console.log(sortedWords)

  return sortedWords[0].split("").join("***");
}

function revWords(s) {
  //receive a string of chars with spaces
  //return a string with the words reversed in the same order
  //'Hello, it's you' => 'olleH, s'ti uoy'
  //split on spaces, reverse it, join back on spaces
}

function twoSumObj(nums, target) {
  //receive a nums array, and a target
  //return the index position of the values that add up to target

  //create an object
  //iterate thorugh nums
  //find the difference
  //check if object has the property
  //return the value given
  //else set the index positon as the values for the values seen

  let answer = {};

  for (let i = 0; i < nums.length; i++) {
    let difference = target - nums[i];
    if (answer.hasOwnProperty(difference)) {
      return [nums, answer[difference]];
    } else {
      answer[nums[i]] = i;
    }
  }
}

//for (let month in data) {
//for (let day in data[month]) {
//         if (data[month][day] === "nice")
//     }
// }

function checkParen(s) {
  //receive a string of opening and closing chars
  //return true if string is valid (opening and closing), return false
  //'([]' => false

  //edge case: if it does not start with opening char, then return false

  //create a stack

  //iterate through the string
  //if the string is an opening char, push it on the stack
  //else if the char is an closing char, pop it off the stack
  //if the stack is empty, return true, else return false

  //  let stack = [];

  //  let anyParen = 0;

  //  for (let i = 0; i <= s.length; i++) {
  //     if (s[i] === '(') {
  //         stack.push(s[i])
  //     } else if (s[i] === ')') {
  //         if( stack.length > 0) {
  //             stack.pop()
  //         } else {
  //             anyParen++
  //         }
  //     }
  //  }

  for (let char of s) {
    if (checkObj[char]) {
      stack.push(checkObj[char]);
    } else {
      if (stack.pop() !== char) {
        return false;
      }
    }
    return !stack.length;
  }

  function validAnagram(s, t) {
    //receive two strings
    //return true if anagram of each other, else return false
    //'apple', 'pear' => false

    //edge case: if they are not the same length, they can't be anagrams
    if (s.length === t.length) return false;

    //split each string, sort and join them back together to see if they are equal to each other
    return s.split("").sort().join("") === t.split("").sort().join("");
  }

  function groupsAna(strs) {
    //receive an array of strings
    //return anagrams back together in one array in an array
    //['app', 'pap', 'tan'] => [ ['app', 'pap'], ['tan']]

    //create an object

    //iterate through the array
    //split the words, sort, and join them back together as the key
    //add values that start together the same
    //return the object values back

    let sortedWordObj = {};

    for (let word of strs) {
      let sortedWord = word.split("").sort().join("");
      if (!sortedWordObj[sortedWord]) sortedWordObj[sortedWord] = [];
      sortedWordObj[sortedWord].push(word);
    }

    return Object.values(sortedWordObj);
  }

  function paliNumber(x) {
    //receive an integer
    //return true if palindrome number, else false
    //345 => false, 45654 => true

    //convert number to string
    //create a pointer on left side, and right side
    //if they are they not the same, return false
    //else increment them

    let stringX = x.toString();

    let left = 0;
    let right = stringX.length - 1;

    while (left < right) {
      if (stringX[left] !== stringX[right]) {
        return false;
      }
      left++;
      right--;
    }
    return true;
  }
}
//return word[0].toUpppercase() + word.slice(1)

//if (vowels.includes(string[i])) {
//     vowelCount++
// }

const longRepeat = (s, k) => {
  //receive a string of chars uppercase, an amount that you can replace chars
  //return length of the string, up to k amount of replacements
  //'FSISHS', 3 => 'SSSSSS' => 6

  //keep track of max length, count of letters we've seen

  //create pointers (left and right) starting at the first char

  //iterate through the string
  //update the values seen in an object
  //if the current window exceeds k replacement,
  //then we need to move left window in
  //remove left window's value from the object

  //return the current window

  let count = 0;
  let maxLength = 0;
  let seenChars = {};

  let left = 0;
  let right = 0;

  while (right < s.length) {
    // ! iterate from right window to the end of the string
    const rightChar = s.charAt(right);
    seenChars[rightChar] = (seenChars[rightChar] || 0) + 1;
    count = Math.max(count, seenChars[right]);

    if (right - left + 1 - count > k) {
      const leftChar = s.charAt(left);
      seenChars[leftChar] = -1;
      left++;
    }
    maxLength = Math.max(maxLength, right - left + 1);
    right++; // ! increment right window to keep moving
  }
  return maxLength;
};

//return (goose - 1) % goose.length

//for (let i = 0; i < array.length; i++) {
// const lastEle = array[array.length - 1]
// return lastEle * (lastEle + 1) /2
//      3            4
//       12 /2 = 6
// }

//[1, 2, 3] = > 1 + 2 + 3 = 6

//return [ele, ele + 1]

// function makeNew(array) {
//let newArray = [];
// for (let i = 0; i < array.length; i++) {
//   newArray.push([array[i], array[i + 1]])
// }
// }

//return array.map( ele, idx => {
//   const num = idx + 1
//   return idx + ":" + ele
// }

function stringy(size) {
  // receive an integer to determine the length
  //return a string back with the length of size starting with 1, then add a 0
  //stringy(5) => '10101'

  //create a new string
  //iterate up to size
  //add 1 for odds to new string
  //odd 0 for positive number to new string
  //return new string

  let output = "";

  for (let i = 1; i <= size; i++) {
    if (i % 2 !== 0) {
      output += "1";
    } else {
      output += "0";
    }
  }
  return output;

  //return "".padStart(size, "10")

  //time: O(n) we are going through everything once
  //space: O(n) creating `output`
}

function findUniq(arr) {
  // receive an array of integers (whole and floats)
  //return the value that is different
  //[3,3,3,3,4,3] => 4

  //brute force:
  //look through each individual one and compare it to the previous
  //if different, then return the value

  // for (let i = 0; i <= arr.length; i++) {
  //   if (arr[i] !== arr[i + 1]) {
  //     return arr[i + 1]
  //   }
  // }

  // for (let i = 0; i < arr.length; i++) {
  //   if (arr.indexOf(arr[i]) === arr.lastIndexOf(arr[i])) {
  //     return arr[i];
  //   }
  // }

  //optimized:
  //use Set to get unique value

  // let setUnique = new Set(...arr)
  // console.log(setUnique)

  let freqCounter = {};

  for (let num of arr) {
    freqCounter[num] = (freqCounter[num] || 0) + 1;
  }

  for (let key in freqCounter) {
    if (freqCounter[key] === 1) return Number(key);
  }
}

function mergeLL(head1, head2) {
  //receive two sorted linked lists
  //return one LL in sorted order
  //create a dummy node
  //then check if head1's first node is < head2's first node,
  //then add in head1,
  //else add in head2

  let current1 = head1;
  let current2 = head2;
  let dummy = new Node();
  let tail = dummy;

  while (current1 !== null && current2 !== null) {
    if (current1.val < current2.val) {
      tail.next = current1;
      current1 = current1.next;
    } else {
      tail.next = current2;
      current2 = current2.next;
    }
    tail = tail.next;
  }

  if (current1) tail.next = current1;
  if (current2) tail.next = current2;

  return dummy.next;
}

//if char.hasOwnProperty()
//char++

function recurRevLL(head, prev = null) {
  //receive a linked list
  //return the ll in reverse
  //base case: if head === null, return prev
  //recursive call and create
  //next variable to capture next node
  //pass in head and next to the function

  if (head === null) return prev;

  const next = head.next;
  head.next = prev;
  return recurRevLL(next, head);
}

function repeatChar(s, k) {
  //receive a string of uppercase letters, an integer amount of how many times you can replace
  //return max length of how many chars you can replace
  //'FOOD", 1 ="OOOD" => 3
  //create an object to store the values seen
  //create a count
  //create a length
  //create two pointers (left and right) starting at 0 index
  //iterate through s string to keep track of how many chars seen
  // if the amount of replacements has been breached,
  //move left window up and remove value seen from object
  //return max length

  let valuesSeen = {};
  let count = 0;
  let length = 0;

  let left = 0;
  let right = 0;

  while (right < s.length) {
    const rightChar = s.charAt(right);
    valuesSeen[rightChar] = (valuesSeen[rightChar] || 0) + 1;
    count = Math.max(count, valuesSeen[rightChar]);

    if (right - left + 1 - count > k) {
      const leftChar = s.charAt(left);
      valuesSeen[leftChar] -= 1;
      left++;
    }
    length = Math.max(length, right - left + 1);
    right++;
  }
  return length;
}

function subStringLong(s) {
  //receive a string of chars with no whitespaces
  //return an integer of the longest length with no repeating chars
  //'fishing' => 'fish' => 4

  //create a Set
  //iterate through the string
  //check if the set does not have it
  //add it in
  //if the set does have it already
  //delete the char out of it
  //update size
  //return size

  let seenSet = new Set();
  let length = 0;
  let left = 0;
  let right = 0;

  while (right < s.length) {
    if (!seenSet.has(s[right])) {
      seenSet.add(s[right]);
      right++;
    } else {
      seenSet.detlete(s[left]);
      left++;
    }
    length = Math.max(length, set.size);
  }
  return length;
}

//time: O(n) - going through the elements once
//space: O(n) - creating a new Set

function twoSum(num, target) {
  //receive an array of integer, and a target (integer)
  //return the index position of the two integers that total up to target
  //[3, 4, 5, 8], 9 => [1, 2]

  //create an object
  //iterate through num
  //store the index positon for each num
  //return the index position
  //else, set the index position

  let targetObject = {};

  for (let i = 0; i < nums.length; i++) {
    let difference = target - nums[i];
    if (targetObject.hasOwnProperty(difference)) {
      return [targetObject[difference], i];
    } else {
      targetObject[nums[i]] = i;
    }
  }
}

function checkParens(s) {
  //receive a string of parens
  //return true if they pair up, else return false
  //'({)' = false

  //edge case: if it did not start with an opening bracket, then false

  //create a stack
  //if it is a opening paren, then add to the stack
  //then check if stack's not empty
  //check if the previous one added was a closed one
  //if so, remove it
  //check if stack's length is empty

  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(s[i]);
    } else {
      if (!stack || stack.pop !== ")") {
        return false;
      }
    }
  }
  return true;
}

function paliNumb(x) {
  //receive an integer
  //return true if palindrome
  //3455 => false

  //modify to string, split it, reverse, join and see if it's equal to x
  return x.toString().split("").reverse().join("") === String(x);
}

function altLL(head1, head2) {
  //receive two heads of two linked lists
  //return one linked list with nodes alternating between
  // 1 -> 2 -> 3 -> null
  // 4 -> 5 -> 6 -> null
  //=> 1 -> 4 -> 2 - > 5 -> 3 -> 6 -> null

  //edge cases: head1 is empty, return head2 and vice versa
  if (!head1) return head2;
  if (!head2) return head1;

  //capture current node in head1 and head2
  //initialize a count to keep track of odd or even
  //capture tail
  //iterate through while linkedlist is not empty
  //if head1 has been added, add from head2

  let current1 = head1;
  let current2 = head2;
  let tail = current1;
  let count = 0;

  while (current1 !== null && current2 !== null) {
    if (count % 2 !== 0) {
      tail.next = current1;
      current1 = current.next;
    } else {
      taill.next = current2;
      current2 = current2.next;
    }
    tail = tail.next;
    count++;
  }

  if (current1) tail.next = current1;
  if (current2) tail.next = current2;

  return head1;
}

return array.filter((ele) => typeof ele === "number");

return array.map(ele, idx => {
  const newIdx = idx + 1
  return newIdx + ":" ele
})

const array = [1,2,3] 
const lastEle = array[array.length-1]
return lastEle * (lastEle + 1) /2 
         3             4

function revWords(s) {
  //receive a string with space and uppercase && lowercase letters
  //return the words reversed
  //revWords("Hey, it's happy!") => ("!yppah s'ti ,yeH")

  //edge case:
  //if there's only one word, reverse it, and return the reversed word

//brute force:
//split on the spaces
//grab each word in the array
//reverse it, join it back on spaces

// console.log(s.split(" ")) [ "Let's", 'take', 'LeetCode', 'contest' ]
let newString = ""
let arrayWord = s.split(" ")
for (let word of arrayWord) {
  let revWod = word.split("").reverse().join("") //'s'teL
  newString += revWod + " "
}
 return newString.trim();

};

function groupAnaTwo(strs) {
//receive an array of strings
//return an array back of anagrams of strings grouped together

//edge case: if length is one, return the strs back in an array

//create an object
//split the words, sort, and join it back togehter as key
//insert the words where it matches the keys
//return the values back in an array

if (strs.length === 1) return [strs];

let sortedAna = {}
for (let str of strs) {
  let sortedWord = str.split("").sort().join("")
  if (!sortedAna[sortedWord])sortedAna[sortedWord] = []
  sortedAna[sortedWord].push(str)
}
return Object.values(sortedAna)
}

function twoSumTwo(num, target) {
  //receive an array of numbers, and a target
  //return the index positions of the numbers that make up the target
  //[3, 5, 6,3,1], 9 => [0, 2]

  //create an object
  //iterate through num
  //find the difference between target and the current value looking for
  //if the difference has been found,
  //return the index positions of both
  //else set the difference in 

  let answer = { }
  for (let i = 0; i< nums.length; i++) {
    let difference = target - nums[i]
    if (answer.hasOwnProperty(difference)) {
      return [i, answer[difference]]
    } else {
      answer[nums[i]] = i
    }
  }
}

function vowelCo(array) {
let count = 0;
let vowel = ['a', 'e', 'i', 'o', 'u']

for (let i = 0; i < array.length; i++) {
  if (vowel.includes(array[i])) {
    count++
  }
}
return count
}

function paliTwo(num) {
  //receive an integer
  //return true if palindrome, else false
  //89789 => true

  //stringfy the num
  //use two pointers at the outside of the num
  //return false if they don't equal to the eqeual other when pointing
  //else return true

  let stringNum = num.toString();

  let i =0;
  let j = stringNum.length - 1;

  while (i < j) {
    if (stringNum[i] !== stringNum[j]) {
      return fasle
    }
    i++;
    j--;
  }
  return true
}