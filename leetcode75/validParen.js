// Given a string s containing just the characters '(', ')',
//  '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open 
// bracket of the same type.
 

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false


const validParen = (s) => {
//a string filled with opening and closing parenthesis/brackets
//return true if the string can open and close themselves
//validParen("{]}[") => no b/c [ after ]

//use an object to see if you found the closing 
//if can't find it, return false
//otherwise, after searching entire string, return true;

let obj = {
    "[" : "]",
    "{" : "}",
    "(" : ")"
}

for (let paren of s) {
    if (paren !== obj[propery]) {
        return false
    }
}

return true;


}

console.log(validParen("[]"))