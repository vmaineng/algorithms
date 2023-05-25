const longestPalindrome = (s) => {

    //substring = continous next to each other ; 
    //palindrome = same as it is forward as it is backward

    //brute force; two for nested loops and create poitners with i and j
    //store the results in a new string (+=)
    //return new string

    //optimized method: 
    //create two pointers (one at beginning, one at end)
    //check if they are the same
    //do one more check of the letters on the inside
    //then add to the result
    //keep track of the length

    //odd vs even

    //check palindrome

  
    let longest = "";
    let longestLength = 0;

    let left = 0;
    let right = 0;

    while (left >= 0 && right < s.length && letters[left] === letters[right]) {
        left--;
        right++
    }

for (let i = 0; i < s.length; i++) {
    let i = 0;
    let 
}

return longest

}

console.log(longestPalindrome("cbbd"))

//time = O (n^2)

  // ! when do we use split to get each letter
  // ! when do you traverse through s.length - 1 vs s.length;