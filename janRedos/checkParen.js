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

}

console.log(checkParen('{{}'))