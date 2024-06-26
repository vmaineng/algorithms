function checkParen(string) {
  //receive a string of parenthesis
  //return true if all pairs, else false
  //'))()' => false

  //create an object
  //store the opening as key, and closing as value

  //iterate through the string
  //check if it's an opening
  //add on to stack
  //else if it is a closing
  //check to make sure the stack's length is not empty
  //check the item from stack's length

  //return true if stack's length is empty after checking

  let stack = [];
  let addParen = 0;

  for (let paren of string) {
    if (paren === "(" || paren === "[") {
      //if you are an opening bracket, add to stack
      console.log(paren, stack);
      //if value exists
      stack.push(paren); //add to list
    } else {
      //if you are a closing bracket, check to make sure stack's not empty
      //then pop of the previous one
      if (stack.length > 0) {
        stack.pop();
      } else {
        //if don't match, keep track for paren
        addParen++;
      }
    }
  }
  addParen += stack.length; //2
  return addParen === 0 ? true : false;
}

console.log(checkParen("([()"));

var isPalindrome = function (x) {
  //receive a number
  //return true if palindrome, else return false
  //345 => 543 => false

  //edge case: if the length is 1, return true

  //convert number to String, split it, reverse it, join it back together and see if it's the same

  return x.toString().split("").reverse().join("") === x.toString();
};

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  //get the heads of two linked lists
  //return one LL where the nodes are sorted

  //if list2 is empty, return list1;
  //if list1 is empty, return list2;

  //create a dummy node;
  //capture the head1, head2 as current node in both lists;
  //check to see which value is less
  //if list2's value is less, add list 2
  //else add in list1
  //then if there's any remaining, add in the remaining from either list1, or list 2

  if (!list1) return list2;
  if (!list2) return list1;

  let dummy = new ListNode();
  let tail = dummy;
  let current1 = list1;
  let current2 = list2;

  while (current1 !== null && current2 !== null) {
    if (current1.val <= current2.val) {
      tail.next = current1; //tail's pointer points to new current1's node
      current1 = current1.next; //update pointer
    } else {
      tail.next = current2;
      current2 = current2.next;
    }
    tail = tail.next;
  }

  if (list1) tail.next = current1;
  if (list2) tail.next = current2;

  return dummy.next;
};

function LongestRepeat(s, k) {
  //receive a string and integer of how much to replace
  //return length of longest substring that does not exceed k replacement
  //'CRAYYYAB', 2 => 'CYYYYYAB' => 5

  //create track of the letters seen
  //keep track of the length of the window
  //if the window size - current count of replacements done exceeds, k,
  //then shrink window fom left
  //keep iterating through the rest of the string
  //return maxLength captured

  let count = 0;
  let valueCount = {};
  let length = 0;

  let left = 0;
  let right = 0;

  while (right < s.length) {
    const rightChar = s.charAt(right);
    valueCount[rightChar] = valueCount[rightChar] + 1 || 1;
    count = Math.max(count, valueCount[rightChar]);

    if (right - left + 1 - count > k) {
      const leftChar = s.charAt(left);
      valueCount[leftChar] -= 1;
      left++;
    }

    length = Math.max(length, right - left + 1);
    right++;
  }
  return length;
}

// console.log(LongestRepeat("ABAB", 2));

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function (nums) {
  //receive an integer of numbers/
  //return the total of the max frequences shown in nums * how many elements have the max
  //[1, 2, 3, 5, 3, 3, 5, 5] => { 3: 3, 5: 3} => 3 * 2 = 6

  //create an object to store the occurences
  //iterate and keep track of counter

  //then iterate through to find the max value

  //then iterate through to find the keys of the object

  //multiply each other and return the total

  let maxFreqElements = 0;
  let seenValues = {};
  let maxFrequency = 0;

  for (let i = 0; i < nums.length; i++) {
    const numValues = nums[i];
    seenValues[numValues] = seenValues[numValues] + 1 || 1;
  }

  for (let key in seenValues) {
    if (seenValues[key] > maxFrequency) {
      maxFrequency = Math.max(maxFrequency, seenValues[key]);
    }
  }

  for (let key in seenValues) {
    //multiple max frequency elements
    if (seenValues[key] === maxFrequency) {
      maxFreqElements++;
    }
  }

  return maxFreqElements * maxFrequency;
};

function twoSum(number, target) {
  //receive a number array, target (integer)
  //return the index position of the two numbers that add up to target
  //[3, 5, 2, 3], 6 => [0, 3]

  //create an object
  //look through number array
  //store the index position as value
  //take the difference subtract target's and current value
  //find the difference in the value of the object
  //return the two index position back as an array

  let seenValues = {};

  for (let i = 0; i < number.length; i++) {
    let difference = target - number[i];
    if (seenValues.hasOwnProperty(difference)) {
      return [difference, number[i]];
    } else {
      seenValues[difference] = number[i];
    }
  }
}

function revLL(head) {
  //receive a head of a LL
  //return the LL reverse
  // 1 -> 2 -> 3 => 3 -> 2 -> 1

  //edge case: if LL is empty

  //create a new node to capture the prev node
  //traverse through the head of the linked list
  //capture the next node
  //point to the prev node
  //then move the pointer of curr to the next node
  //the move the pointer to prev

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

function countVow(string) {
  //receive a string
  //return total vowels exist
  //'Hello' => 2

  //edge case: a word without no vowels
  //create an array of vowels
  //iterate through the string
  //check if it has the vowel, increment total
  //return total

  if (!string) return 0;

  const vowels = ["a", "e", "i", "o", "u"];
  let totalVowels = 0;

  for (let i = 0; i < string.length; i++) {
    if (vowels.includes(string[i].toLowerCase())) {
      totalVowels += 1;
    }
  }
  return totalVowels;
}

console.log(countVow("HELLO"));

function groupAnagrams(strs) {
  //receive an array of strings
  //return anagrams together in one array
  //['cat', 'bat', 'tac', 'sat'] => [['cat','tac'], ['bat'], ['sat']]

  //edge case: if strs is empty, return [""]

  if (strs.length === 0) return [""];
  if (strs.length < 2) return [strs];

  //iterate through each word in strs
  //sort it
  //use the sorted word as key, and the actual words as the values
  //return the values back in array format

  let sortedKey = {};

  for (let str of strs) {
    //'abt'
    let sortedWord = str.split("").sort().join("");
    if (!sortedKey[sortedWord]) sortedKey[sortedWord] = [];
    sortedKey[sortedWord].push(str); //'abt': ['bat']
  }
  return Object.values(sortedKey);
}
console.log(groupAnagrams(["cat", "bat", "tac", "sat"]));

// ! sort inside the loop, if it's empty, initialize an empty array, then push in the actual strings for the values

function altLL(head1, head2) {
  //receive two head of linked lists
  //return one list w/ nodes alternated

  //keep a count of odd or even
  //keep track of a current node starting from list 1
  //iterate through til it's null
  //if one list is not empty, add in the remaining nodes

  let current = head1.next;
  const head = head1;
  let tail = head1;
  let current2 = head2;
  let count = 0;

  while (current !== null && current2 !== null) {
    if (count % 2 === 0) {
      tail.next = current2;
      current2 = current2.next;
    } else {
      tail.next = current;
      current = current.next;
    }
    tail = tail.next;
    count++;
  }

  if (!current) return (tail.next = current2);
  if (!current2) return (tail.next = current);

  return head;
}

function longestSub(s) {
  //receive a string of lowercase letters
  //return the length of longest substring with no repeating characters
  //'apple' => 3 => 'ple'

  //keep track of length;
  //utilized a Set to store values seen;
  //iterate through the string
  //check if set already  has it;
  //if so, then remove from set, move left pointer
  //return max length;

  let maxLength = 0;
  let seenValues = new Set();

  let left = 0;
  let right = 0;

  while (right < s.length) {
    if (seenValues.has(s[right])) {
      seenValues.remove(s[left]);
      left++;
    } else {
      seenValues.add(s[right]);
      right++;
    }
    maxLength = Math.max(maxLength, seenValues.size);
  }
  return maxLength;
}

const paliNumber = (x) => {
  //receive an integer
  //return true if it is a palindrome, else return false
  //4323 => false

  //convert number to string
  //use left pointer on the first one, and right pointer on the last
  //see if they are identical, keep looking through rest of number
  //else return false

  const stringX = x.toString();

  let left = 0;
  let right = stringX.length - 1;

  while (left < right) {
    if (stringX[left] !== stringX[right]) {
      return false;
    } else {
      left++;
      right--;
    }
    return true;
  }
};

const gauss = (array) => {
  //receive a sorted array
  //return the total amt

  const lastDigit = array[array.length - 1];
  return (lastDigit * (lastDigit + 1)) / 2;
};

//return array.map((item, idx) => [item, idx])

const longRepeat = (s, k) => {
  //receive a string of uppercase letters, and an integer to state how much you can replace
  //return the max length of replacements can do
  //'APPLE', 2 => "PPPPE"or "APPPP" => 4

  //create an object to store letters seen
  //create a length to track maxLength;
  //keep count of how many letters have seen

  //iterate at the first letter and add to the object
  //keep adding letters until the replacement has not been breached
  //if window size and replacement has been breached, move left pointer up
  //return max length;

  let maxLength = 0;
  let count = 0;
  let seenVal = {};

  let left = 0;
  let right = 0;

  while (right < s.length) {
    const rightChar = s.charAt(right);
    seenVal[rightChar] = seenVal[rightChar] + 1 || 1;
    count = Math.max(count, seenVal[rightChar]);

    if (right - left + 1 - count > k) {
      const leftChar = s.charAt(left);
      seenVal[leftChar] -= 1;
      left++;
    }
    maxLength = Math.max(maxLength, right - left + 1);
    right++;
  }
  return maxLength;
};

//return array.map((element) element => typeof element === 'number')
//return array.map((ele, idx) =>{ 
//   const newIdx = idx + 1
//   return `${newIdx} : ${ele}`
// )

//return (players - 1) % players.length;

function mergeLL(list1, list2) {
  //receive two linked lists
  //return one sorted linked list
  //

  //edge case: if list1 is empty, return list2
  //if list2 is emptyr, return list1

  //capture the head of list1
  //capture tail of list1
  //capture current of list1, list2

  //check the values of the nodes
  //if list1's val < list2, add in list1, first
  //else add in list2,
  //move the tail node to point to next node;
  //add in remaining of list1, or add in remaining of list2

  //return head1

  if (!list1) return list2;
  if (!list2) return list1;

  let head1 = list1;
  let tail = new Node();
  let current = list1;
  let current2 = list2;

  while (current !== null && current2 !== null) {
    if (current.val < current2.val) {
      tail.next = current;
      current = current.next;
    } else {
      tail.next = current2;
      current2 = current2.next;
    }
    tail = tail.next;
  }

  if (!current)  tail.next = current;
  if (!current2)  tail.next = current2;

  return head1

}

//return letter[0].toUpperCase() + letter.slice(1)

function revLLRec(head, prev = null) {
  //get a head of linkedlist,
  //return the list reversed

  //base case
  if (head === null) return prev;

//pass in prev as a default parameter set to null
//capture next which is the next node after head
//call the function and pass in (next as head, )

const next = head.next;
head.next = prev //point to prev node;
return revLLRec(next, head)
}

function paliNum(num){
  //receive a num
  //return true if palindrome, else false
  //3456543 => false

  //turn to string, split it, and reverse it and compare it the same num passed in

  return num.toString().split().reverse().join("") = num.toString()
}

function checkPar(string) {
  //receive a string of paranethesis
  //return true if valid pairs; else false
  //'{()(}' => false

  //iterate through an object of pair parenthesis
//if it is '(', then add to a stack
//else if it is ')' closing,
//then check stack, to make sure it's not empty and retrieve the previous one has an open;
//return the opposite of stack if it's empty, return true else it will return false

let result = [];

for (let str of string) {
  if (str === '(') {
    result.push(str)
  } else {
    if (!result || str === ')' && result[result.lenght - 1] !== '(') {
      return false
    }
    stack.pop()
  }
}
return !result.length
}

function revWords(s) {
  //receive a string with spaces and uppercase
  //return the string reversed
  //'Applesauce is good' => 'doog si ecuaselppA'

  //create strings - word, sentence
  //split the s by space => ["Applesauce", "is", "good"]
//check if it is not a space,
  //then add in the letters tot he string
  //else add in the space and clear out the rev word

  const wrd = "";
  const newStr = "";

  for (let i = 0; i < s.length;i++) {
    if (s[i] !== " ") {
      wrd = s[i] + wrd
    } else { 
      newStr =  wrd + " "
      wrd = ""
    }
  }
return newStr + wrd
}