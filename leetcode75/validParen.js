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


//if you are the closing bracket, add it on to stack
//if found an opening bracket, check last item on the stack to see
//if same element
let stack = [];
let obj = {
    "[" : "]",
    "{" : "}",
    "(" : ")"
}

for (let paren of s) {
    if (obj[paren]) { //if obj has the other corresponding one from the s string
        console.log(obj[paren], paren)// obj[paren] = ], paren = [
        stack.push(paren)
    } else {
        stack.pop();
    }
}

return stack.length === 0;


}

console.log(validParen("[]"))