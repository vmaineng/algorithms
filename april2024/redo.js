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

    let sortedWords = {}

    for (let word of sortedArr ) {
        let sortedArr = arr.split("").sort().join("")
        if (!sortedWords[sortedArr]) sortedWords[word] = []
        sortedWords[word].push(word)
    }
return Object.values(sortedWords)
}