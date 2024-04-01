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

for(let i = 0; i < s.length; i++) {
    if(s[i] === '(' || s[i] === '[' || s[i] === '{') {
        stack.push(s[i])
    } else {
        //if found closing bracket
        if (!stack.length || //if stack is empty or if you can't find the corresponding  opening character, then return false;
        (s[i] === ')' && stack[stack.length - 1] !== '(') ||
        (s[i] === '}' && stack[stack.length - 1] !== '{' ) ||
        (s[i] === ']' && stack[stack.length - 1] !== '[' )) {
            return false
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
    let difference = target - nums[i]
    if (answer.hasOwnProperty(difference)) {
        return [answer[difference], nums[i]]
    } else {
        answer[difference] = i
    }
}
}


