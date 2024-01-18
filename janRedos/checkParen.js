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
}