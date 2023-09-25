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

    //edge case - if less than 1, send back the word
    if (words.length <= 1) return [words];

    let objSource = {};

    for (let word of words) {
       // let sortedStr = word.split("").sort().join(""); this returns sorted strings in the array;
       word.split("").sort().join(""); //this returns the original words
       // console.log(word)

        if (!objSource[word]) objSource[word] = [];
        objSource[word].push(word)

    }
    return Object.values(objSource)


}

console.log(groupAna(["eat", "tea", "tan", "ate", "nat", "bat"]));