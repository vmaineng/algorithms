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

s.split("").sort().join("");
t.split("").sort().join("");

for (let i = 0; i < s.length; i++) {
    if (t[i] !== s[i]) {
        return false;
    }
}
return true;

}

console.log(anAnagram("rat", "car"))

//notes
//with strings, have to split them up by the quotation marks, can sort, then join them back together
