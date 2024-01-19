const checkParen = (string) => {
//get a string of paranethesis
//return true if opening matches with closing
//'{{[]}' => false => '{'

//if string length is 1, return false

//create an object: of matching opening and closing parenthesis

//iterate through the string
//check to see if the closing parenthesis matches
//then pop off of the stack
//return if the stack's length is equal to the string's length

if (string.length === 1) return false;

let pairings = {
    '[': ']',
    '{': '}',
    '(': ')'
}

let stack = [];

for (let char of string){
    if (pairings[char]) {
        stack.push(pairings[char])
    } else {
        if (stack.pop() !== char) {
            return false
        }
    }
}
return !stack.length;

}

console.log(checkParen('{{}'))

function makeNew(array) {
   let result = [];
   for (let i = 0 ; i < array.length; i++) {
   result.push([array[i], array[i + 1]])
   }
   return result;
}

console.log(makeNew([0,1,]))

const replaceChar = (s,k) => {
    //get a string of letter, and an integer that states how many letters can be replaced
    //return the length of the longest substring containing same letters
    //'ARGRRGR',4 => 'RRRRRRR' => 7

    //edge cases:
    //if the number of replacements exceed the letters of the string

    //keep track of length size
    //!have to keep track of most frequent character seen
    //iterate at first letter
    //see if second letter is equal to the first letter
    //if so, keep going until k is reached
    //return maxLength

//     let maxLength = 0;
//     let charFreq = {};
//     let maxFreq = 0;
//     let i = 0; 
//     let j = 0;

//    while (j < s.length) {
//     const rightChar = s.CharAt(right);
//     charFreq[rightChar] = charFreq[rightChar] + 1 || 1
//     maxFreq = Math.max(maxFreq, charFreq[rightChar])

//     while ((j - i + 1) - maxFreq > k) {
//         const leftChar = s.CharAt(left);
//         charFreq[leftChar] -= 1
//         left++
//     }
//     maxLength = Math.max(maxLength, (right - left + 1)) 
//     right++
//    }
//    return maxLength;


//initiate an object to keep track of how many characters seen
//keep track of length;
//start window at the first letter
//iterate through until end of string
//store the letters seen in the object and how many times we've seen it
//keep track of the letter we have seen the most
//during this operation,
//make sure the window and the maxLetter seen does not exceed k operations
//if it does, move left window up
//keep track of length
//move right window
//return the length;

// let trackFrequencies = {};
// let maxLength = 0;
// let maxChar = 0; 

// let left = 0;
// let right = 0; 

// while (right < s.length) {
//     const rightChar = s.charAt(right);
//     trackFrequencies[rightChar] = trackFrequencies[rightChar] + 1 || 1
//     maxChar = Math.max(maxChar, trackFrequencies[rightChar])

//     while ((right - left + 1) - maxChar > k) {
//         const leftChar = s.charAt(left)
//         trackFrequencies[leftChar] -= 1
//         left++
//     }
//     maxLength = Math.max(maxLength, (right - left + 1))
//     right++
// }

// return maxLength;

// }

// console.log(replaceChar('ABA', 1))

const revLL = (head) => {
    //get a head of a linked list
    //return it reverse
    //1 -> 3 -> 4 -> null => 4 -> 3 -> 1 -> null

    //edge case:
    //if head is empty, return nulll

    //set up pointers: prev, curr

    //iterate through while the linked list is not null
    //capture the next node
    //switch the pointer from next to prev
    //move pointers: next, curr, prev
    //return the prev

    if (!head) return null;

    let prev = null;
    let current = head;
    
    while (current !== null) {
        const next = current.next;
        current.next = prev; 
        prev = current; //! move prev to current first
        current = next;
       
    }
    return prev;
}

//recursive;
// const revLL = (head, prev = null) {
//     if (head === null) return prev;
//     const next = head.next;
//     head.next = prev ; // !have to switch pointers
//     return revLL(next, head)
// }

function add(array) {
    return array.map((letter, idx) => { //return for overall function
      return idx + 1 + " : " + letter//returns for each individual transformed element of the array
    })
}

// console.log(add(["a", "b"]))

const groupAna = (array) => {
    //an array of strings
    //return anagrams together in one array
    //["bat", 'abt', 'rat'] => [['rat'], ["bat", 'abt']]

    //if only one word, return the word

    //create an array to store the answers
    //split the strings, sort them, and create an object to store the words as values
    //return the values as arrays

    if (array.length === 1) return [array];

//     let sortedWords = array.map(string => string.split("").sort().join(""))
//    return sortedWords

let answer = [];
let trackWords = {};

for (const word of array) {
    let sortedWords = word.split("").sort().join("");

    if (!trackWords[sortedWords]) trackWords[sortedWords] = [];
    trackWords[sortedWords].push(word)

}
return Object.values(trackWords) //return the values from the object


}
}
// console.log(groupAna(["bat", 'abt', 'rat']))

const longestRepeating = (string, k) => {
    //received a string of letters, an integer to state how many to replace
    //return the length of longest substring of replacement available
    //"ABCDBCD", 4 => "ABBBBBB" => 6

    //edge case:
    //if the amount of replacements exceeds the string, then can't do that much replacement
    if (k > string.length) return "can't complete";

    //create an object to keep track of the letters seen
    //keep track of maxFreq
    //keep track of maxLength;

    //create pointers starting at the first letter

    //iterate through the string and keep track of letters seen
    //find the max frequeny letter

    //while looping through, make sure the length and the changes does not exceed what k stated
    //otherwise, shift window in from left side

    //find max length
    //return the max length;

    let trackFreq = {};
    let maxFreq = 0;
    let length = 0; 

    let left = 0;
    let right = 0;

    while (right < string.length) {
        const rightChar = string.charAt(right) 
        trackFreq[rightChar] = trackFreq[rightChar] + 1 || 1
        maxFreq = Math.max(maxFreq,trackFreq[rightChar])

        while ((right - left + 1) - maxFreq > k) {
            const leftChar = string.charAt(left);
            trackFreq[leftChar] -= 1
            left++
        }
        length = Math.max(length, (right - left + 1))
        right ++
    }
    return length;
}

console.log(longestRepeating('ABCDBCD', 4))