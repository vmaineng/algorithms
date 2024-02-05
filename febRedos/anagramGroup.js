const anaGroup = (strs) => {
//an array of strings
//return anagrams grouped together
//anagram = using all the letter in each word once you get another word

//["cat", "bat", "float", "toalf"] => [[["cat", "bat"], ["float", "toalf"]]

//edge case: if string is empty, return an empty string
//if strs only has one letter, return the string in an array
// if (!strs) return [strs]
// if (strs.length === 1) return [strs]

if (!strs || strs.length === 1) return [strs];

//go through each word, sort it
//then create an object and store the word as keys, and update the values
//return the keys as an array

let trackWords = {};

for (let word of strs) {
    let sortedWord = word.split("").sort().join("")

    if (!trackWords[sortedWord]) trackWords[sortedWord] = [];
    trackWords[sortedWord].push(word) 
}

return Object.values(trackWords) // ! return the values from the object

}

console.log(anaGroup(["cat", "bat", "float", "toalf"]))

// ! if you set an array as the value, you can push into it
//  trackWords[sortedWord].push(word) 

//O(n) space
//O(n) time