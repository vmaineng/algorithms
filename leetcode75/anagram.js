// Given two strings s and t, return true if t is an anagram of s, 
// and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of
//  a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false

const anAnagram = (s, t) => {
//two strings
//return true if all letters are in each string
//s="jump23" t="2pujm3" => true

//brute force
//sort strings
//compare each letter in order
//if found any letter that does not match, return false
//otherwise if search through entire string, return true
//time: O(n log n) due to sort
//space: O (n) - under the hood, split creates an array to store the characters of each input of strings

// let str1 = s.split("").sort().join(""); //splits the input string in an array of individual characters, then sorts in dictionary order, then joins back into a single string
// let str2 = t.split("").sort().join("");

// for (let i = 0; i < str1.length; i++) {
//     if (str2[i] !== str1[i]) {
//         return false;
//     }
//     console.log(str2[i], str1[i])
// }
// return true;

//optimized approach: 
//edge case - if length doesn't equal the same, we know they are not anagrams
//use an object to keep track of frequencies instead of sorting
//check to see if they have the same amount of frequencies of characters
//if so, return true; else return false; 

if (s.length !== t.length) return false;

let charCount1 = {};
let charCount2 = {};

for (let char of s) { //iterate through the array
    charCount1[char] = (charCount1[char] || 0) + 1 //store it in the object
}

for (let char of t) {
    charCount2[char] = (charCount2[char] || 0) + 1
}

for (let char in charCount1) { //check charCount2 against the values in charCount1
    if (charCount1[char] !== charCount2[char]) {
        return false;
    }
}

return true;
}

console.log(anAnagram("rat", "tar"))

//notes
//with strings, have to split them up by the quotation marks, can sort, then join them back together
