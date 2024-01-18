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

    let maxLength = 0;
    let charFreq = {};
    let maxFreq = 0;
    let i = 0; 
    let j = 0;

   while (j < s.length) {
    const rightChar = s.CharAt(right);
    charFreq[rightChar] = charFreq[rightChar] + 1 || 1
    maxFreq = Math.max(maxFreq, charFreq[rightChar])

    while ((j - i + 1) - maxFreq > k) {
        const leftChar = s.CharAt(left);
        charFreq[leftChar] -= 1
        left++
    }
    maxLength = Math.max(maxLength, (right - left + 1)) 
    right++
   }
   return maxLength;
}

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