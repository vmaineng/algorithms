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

function groupAna(arr) {
//receive an array of strings
//return an array with arrays of anagrams together

//split the chars in arr, sort them, and join them back together
//iterate through the sorted chars
//create an object to store similar values seen
//insert the original word as values, keys are the sorted word
//return the values as an array


let anaObject = {}

for (let word of arr) {
    let sortedWord = word.split("").sort().join("");
    if (!anaObject[sortedWord]) anaObject[sortedWord] = []
    anaObject[sortedWord].push(word)
}
return Object.values(anaObject)

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

    let vowelsArray = ['a', 'e', 'i', 'o', 'u']

    let lowerCaseStr = str.toLowerCase();

    for (let i = 0; i <= lowerCaseStr.length; i++) {
        if (vowelsArray.includes(lowerCaseStr[i])){
            vowelsCount++
        }
    }
    return vowelsCount
}

const longestRepeat =(s)=> {
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
        uniqueChar.add(s[right])
        right++
    } else {
        uniqueChar.delete(s[left])
        left++
        
    }
    maxLength = Math.max(maxLength, uniqueChar.size)
}

return maxLength
}

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
            return false
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
            uniqueVals.add(s[right])
            right++
        } else {
            uniqueVals.delete(s[left])
            left++
        }
        maxLength = Math.max(maxLength, uniqueVals.size)
    }
    return maxLength
}

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
    let newArr = []

    for (let i = 0; i < arr.length; i++) {
        newArr.push(arr[i], arr[i + 1])
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
    head.next = prev
    return revLL(next, head)
}