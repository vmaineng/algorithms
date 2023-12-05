const repeat = (s, k) => {
//get a string of uppercase english characters and an integer
//return the longest substring containing same letter
//"JUMPOPPPR", 4 => "jupppppppr" => 9

//edge case: if string is all unique and k = 0; that means, the outpout length would be one

//keep track of characters visited
//start window at beginning of string
//keep track of length
//keep track of frequent characters seen

//iterate through the string
//update the characters by 1 if seen
//keep track of max freq character

//during the string, verify the characters have not exceeded k times
//if it does, shorten window by moving left side in
//decrement by 1 if the values have been seen
//keep track of max length seen
//tell right window it can keep incrementing

let visited = {};
let maxLen = 0;
let maxFreq = 0; 

let left = 0;
let right =0;

while (right < s.length) {
    let charRight = s.charAt(right);
    visited[charRight] = charRight + 1 || 1
    maxFreq = Math.max(maxFreq, visited[charRight] )

    while ((right - left + 1) - maxFreq < k) {
        let charLeft = s.charAt(left);
        visited[charLeft] -= 1
        left++
    }

    maxLen = Math.max(maxLen, (right - left + 1))
    right++
}
return maxLen

}

console.log(repeat("JUMPOPPPR", 4))