//leetcode 680

const validPalindrome = (s) => {
//brute force: 
//create another string and push letters into it and see if the reverse string would 
//equal the same as previous string?
//space: O(n) by creating a new string
//time: O(n) iterate through each letter once in the string

//optimized: 
//create a pointer at the first letter
//create a pointer at the end of the string
//check to see if they equal each other
//if they don't equal each other, see if you can delete a letter from left or right
//check to see if they are equal
//return true

let left = 0;
let right = s.length - 1;

while (left < right) {
    if (s[left] !== s[right]) {
        //left + 1 is to skip a letter from left, skip letter from right and keep checking if it is a palindrome
        return checkPalindrome(left + 1, right, s) || checkPalindrome(left, right-1, s)
    }
    left++, right--;
}
return true
}

//helper function to check if it is a palindrome
const checkPalindrome = (left, right, s) => {
    while (left < right) {
        //if letters do not equal other, return false
        if (s[left] !== s[right]) return false;
        //otherwise keep incrementing
        left++, right--;
    }
   return true;
}

console.log(validPalindrome("abcdefsa"))

//expected output: true