//reverse a string

const reverseString = (string) => {
//given a string of letters
//return the string in reverse
//"hi" => "ih"; "hell3" => "3lleh"

//initialize a new string
//iterate through the string from backwards
//add on to the string
//return string

let reverseString = "";

for (let i = string.length - 1; i >= 0; i-- ) {
    reverseString += string[i]
}

return reverseString

//time 

}

console.log(reverseString("hi"))