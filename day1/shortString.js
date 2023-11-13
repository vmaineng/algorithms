// Given an Array of strings, return the shortest string. 
//If there is more than one string of that length, return the string that comes first in the list.
//  The Array will have a minimum length of 1.

function shortString(array) {
    //takes an array of strings
    //return the shortest string (the word)
    //["apple", "john", 'c', 'rawr'] => 'c'
    //["rawr", "john", "the", "tree"] => "the"

    //iterate through the strings
    //initialize a minValue at 0
    //split the strings to capture each letter
    //keep track of min of current word and the minValue
    //return the minvalue

    let minValue = array[0];

    for (let i = 0; i < array.length; i ++) {
        if (array[i].length < minValue.length)
        minValue = array[i]
    }
    return minValue;

}

console.log(shortString(["apple", "john", 'c', 'rawr']))