const valSub = (string, subString) => {
//take in two strings
//return true if substring exists in string
//'browniesaredelicious', 'delicacy' => false

//edge case: 
//if substring is greater than string, return false

//keep a pointer on first letter of the strings, 
//keep going through the strings until they match
//return true

if (subString.length > string.length) return false;

let subPointer = 0;

for (let i = 0; i < string.length; i++) {
    if (string[i] === subString[subPointer]) {
        subPointer++
    }
}

console.log(subPointer, subString.length) //2, 3
//pointer stopped at index 2 and does not match the full length of string
return subPointer === subString.length;

}

console.log(valSub('applesaregood', 'arh'))