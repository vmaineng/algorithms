// Given an array of strings strs, group the anagrams together. 
// You can return the answer in any order.

// An Anagram is a word or phrase formed by rearranging the letters of
//  a different word or phrase, typically using all the original letters 
//  exactly once.

 

// Example 1:

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

function groupAna(words) {
    //get an array of words
    //return anagrams in one array together
    //else return each words individually
    //["apple", "orange", "papel"] => [["apple", "papel"], ["orange"]]

    //brute force - involve comparing each work with every other word to see if they are 
    //anagrams of each other

    
    
    //optimized approach - use an object to keep track of values
    //sort each word
    //check to see if eaach word are equal
    //push to an array together

    let answer = [];

    let objSource = {};

    for (let word of words) {
        word.split("").sort().join("");
        console.log(word)
    }

}

console.log(groupAna(["eat", "tea", "tan", "ate", "nat", "bat"]));