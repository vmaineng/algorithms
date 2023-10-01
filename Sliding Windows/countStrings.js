
// A string is good if there are no repeated characters.

// Given a string s​​​​​, 
//return the number of good substrings of length three in s​​​​​​.

// Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

// A substring is a contiguous sequence of characters in a string.


// Input: s = "xyzzaz"
// Output: 1
// Explanation: There are 4 substrings of 
// size 3: "xyz", "yzz", "zza", and "zaz". 
// The only good substring of length 3 is "xyz".

const countSubstring = (string) => {
//receive a string in the parameter
//return the number of good substrings in length of 3
//"rawr" => "raw", "awr" => 2

//brute force
//check every possible substrings in length of 3

//intiialize a window to 0; 
//iterate through
//check to see if length is 3; 

//check in set to see if substring is unique = 1 good one

let result = 0; 
let k = 3;

for (let i = 0; i < k; i++) {
    
}

}