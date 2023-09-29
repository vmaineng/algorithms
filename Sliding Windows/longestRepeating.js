// You are given a string s and an integer k. You can choose any character of the string 
//and change it to any other uppercase English character. 
// You can perform this operation at most k times.

// Return the length of the longest substring containing the same letter you can get
// after performing the above operations.
 

// Example 1:

// Input: s = "ABAB", k = 2
// Output: 4
// Explanation: Replace the two 'A's with two 'B's or vice versa.

const longestRepeat = (s, k) => {
//get string of uppercase lettters (S), and a limit of how much you can change it out, K
//return max length of a substring containing same letter after performing K operations
//"ABCBCD", k = 2 => "BBBBCD" => 4

//brute force: 
//check out every possible subwindows starting at the first letter
//then move on to the next letter
//start out on A, then can work on B's window

//intiialize a length
//start out at first index
//perform the k operation
//add to length
//find max of length
//return length;

let length = 0;

for (let i = 0; i < s.length; i++) {
    if (s.length > k) {
        return Math.max(length, s[i])
    }
}


}


//objective: put a window up for the substring as long as the changes are <= k
//transform substring into an object to see which one has the most frequent character

