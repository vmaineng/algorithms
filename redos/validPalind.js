const validPali = (string) => {
//get a string of letters - uppercase and lowercase
//return true if it is a palidrome, else false
//palidrome = spelled the same forward as it is backwards
//"apple" => false; "batab" => "false"

//create a new string starting from the ending letter
//add to string
//check if strings are the same, return true
//else return false

// if (string.length === 0) return false;

// let reversedString = "";
// for (let i = string.length - 1; i >= 0; i--) {
//     reversedString += string[i]
// }

// return reversedString === string ? true : false

//time = O(n) b/c going through the string once
//space = O(n) b/c creating a new string as much as string's input intakes

//optimized solution in space
//iterate through the string with two pointers; one at beginning and one at end
//check to see if they are not identical, return false
//else return true

let left = 0;
let right = string.length - 1;

while (left < right) {
    if (string[left] !== string[right]) {
        return false
    }
    left++
    right--
}

return true;

}

console.log(validPali("appa"))