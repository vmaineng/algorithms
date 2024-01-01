function maxRecurringChar(string) {
//string of lowercase letters
//return the letter that occurs the most times
//'abaaabbadew' => 'a'

//if string is empty, return null;
//if string has only one letter, return the letter

//create an object
//loop through to keep track of the frequencies
//increment the value every time you see it
//then check the object to find the max value
//return the maxvalue

let answer = [];
let maxValue = 0; 
let maxChar = ''

for (let char of string) {
    if (answer.hasOwnProperty(char)) {
        answer[char]++
    } else {
        answer[char] = 1
    }
}

for (let letter in answer) {
    if (answer[letter] > maxValue) {
        maxValue = answer[letter] //only grabs value
        maxChar = letter //grabs the ltter as a string
    }
}
// return maxValue; //4 => 'a' occurs 4 times;
return maxChar;
}

console.log(maxRecurringChar('aaabcadd'))

function maxChar(string) {

    let charMap = {};
    let charArray = [];
    let valuesArray = [];
    let maxCharValue = 0; 

    for (let char of string) {
        if (charMap.hasOwnProperty(char)) {
            charMap[char]++
        } else {
            charMap[char] = 1
        }
    }

    charArray = Object.keys(charMap);
    //console.log(charArray) //[ 'a', 'b', 'd', 'e', 'w' ]
    // const val = Object.values(charMap)
    // console.log(val)
    valuesArray = Object.values(charMap)
    // console.log(valuesArray) //[ 4, 1, 2, 1, 1 ]
    maxCharValue = Math.max(...valuesArray)
   // console.log(maxCharValue) //4
   
    return charArray[valuesArray.indexOf(maxCharValue)]
}

console.log(maxChar('aabaadewd'))