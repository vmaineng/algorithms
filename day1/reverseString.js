//reverse a string

const reverseString = (string) => {
//given a string of letters
//return the string in reverse
//"hi" => "ih"; "hell3" => "3lleh"

//initialize a new string
//iterate through the string from backwards
//add on to the string
//return string

// let reverseString = "";

// for (let i = string.length - 1; i >= 0; i-- ) {
//     reverseString += string[i]
// }

// return reverseString

//time: O(n)
//space: O(N)

//optimized method without using a reverse method

//initialize two pointers - one at beginning, one at end
//split the string into individual characters
//swap it
//return string and join it back together;

if (string.length === 1) return string;

let stringArray = string.split("")

let left = 0
let right = string.length - 1;

while (left < right) {
    let temp = stringArray[left]
    stringArray[left] = stringArray[right]
    stringArray[right]= temp
    left++
    right--
}

return stringArray.join("")

}

console.log(reverseString("hi"))