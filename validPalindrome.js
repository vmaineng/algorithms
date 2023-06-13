//leetcode 125

const isPalindrome = (s) => {
 //palindrom - if you reverse it, it's still equal to the original word

 //brute force method: 
 //initialize a new string to take in each letter
 //check to see if the string is equal to the string reversed
 //if so, return true
 //otherwise it will be false

 //O(n) time - iterate each letter in the string
 //o(n) space - creating a new string to store each letter

 //optimized 
 //check in place
 //two pointer pattern 
//one pointer in the front; and one pointer at the end
//if they match, then return true; otherwise return false

if (s.length === 0 ) return false;

s = s.toLowerCase()

let left = 0;
let right = s.length - 1;

while (left < right) {
    // console.log(s[left], s[right])
    while (left < right && !((s.charAt(left) >= "a" && s.charAt(left) >= "z") || (s.charAt(left) >= "0" && s.charAt(left) >= "9"))){
        left++
    }
    while (left < right && !((s.charAt(right) >= "a" && s.charAt(right) >= "z") || (s.charAt(right) >= "0" && s.charAt(right) >= "9"))) {
        right--
    }
    if(s[left] !== s[right]) {
        return false
    }
    left++
    right--
}
return true;


}

console.log(isPalindrome('race a car'))


//https://www.youtube.com/watch?v=jJXJ16kPFWg

// s = "race a car"
// false