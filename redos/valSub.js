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

}

console.log(valSub('applesaregood', 'arg'))