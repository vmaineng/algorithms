const pdrome = (string) => {
    //gets a string of a phrase
    //return true if palindrome, else return false
    //'5faaf5' => true
    //'f' => true

    //edge case: if empty, return true
    //if one letter, return true


    //make a new string and add in the letter
    //check to see if the length matches the input

    if (string.length === 1) return true;
    if (!string) return true; 

    let newString = "";

for (let word of string.toLowerCase()) {
    let nospaceWord = word.split(" ").join("")
    newString += nospaceWord
}

return newString === string 

    // let sortedWord = word.split(" ").reverse().join("")
    // console.log(sortedWord, word)
}

console.log(pdrome('race'))