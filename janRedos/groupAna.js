const groupAna = (array) => {
    //an array of strings
    //return similar anagrams together
    //["gre", "reg", "erg", "app"] => [["app"], ["gre", "reg", "erg"]]

    //if the array of string has only one string, return the string
    //if array is empty, return an empty string

    if (array.length === 1) return [array];
    if (array.length === 0) return [""];

    //create an array to capture the sorted results
    //iterate through each word, sort them
    //push them into the array
    //return the array

    let groupedAnagrams = {};


    for (let word of array) {
       let sortedWord = word.split("").sort().join("")
        if (!groupedAnagrams[sortedWord]) {
            groupedAnagrams[sortedWord] = [word];
        } else {
            groupedAnagrams[sortedWord].push(word)
        }
    }
return Object.values(groupedAnagrams)
}

console.log(groupAna(["eat","tea","tan","ate","nat","bat"]))

function sum(array) {
    // let sum = 0;
    
    // for (let i = 0; i < array.length; i++) {
    //     sum+= array[i]
    // }
    // return sum;
    const lastItem = array[array.length-1]
    return  lastItem * (lastItem + 1 )/ 2
}

console.log(sum([1,2,3,4]))