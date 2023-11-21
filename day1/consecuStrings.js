// Given a string, return all consecutive substrings within that string 
// consisting of at least one character. Substrings should be returned in the 
// order in which they appear.

// Note than in the string 'abc', 'ac' is not a consecutive substring.

// The input string will have a length of 0 or more.

// Input: 'abc'
// Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']

// Input: 'a'
// Output: ['a']


function consecutiveString(string) {
//get a string's length of 0 or more
//return all the consecutive substrings of at least one character in an array
//'green' => 'g', 'gr', 'gre', 're', 'en','n'

//edge cases: if string is empty, return string
//if string is one, retun the string 

//initialize an empty result array
//split the strings
//iterate through the string
//push the string in
//return the result array

// const substrings = [];

// for (let i = 0 ;i < string.length; i++) {
//   for (let j = i + 1; j <= string.length; j++ ) { // the inner loop captures the last element
//     substrings.push(string.substring(i, j));
//   }
// }

// return substrings;

//time: O(n^2)
//space: O(n) depends on how many characters in string


}

console.log(consecutiveString('abc'))