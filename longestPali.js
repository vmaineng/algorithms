const longestPalindrome = (s) => {

    //substring = continous next to each other ; 
    //palindrome = same as it is forward as it is backward
        //compare two letters at the same time

    //brute force; two for nested loops and create poitners with i and j
    //store the results in a new string (+=)
    //can't verify palindrome by moving only one pointer
    //return new string

//work from in to out;

    //optimized method: 
    //create two pointers (start in middle)
    //check if they are the same
    //do one more check of the letters on the inside
    //then add to the result
    //keep track of the length

    //odd vs even

    //even; check next one to see if it's equal to each other

    //check palindrome


    let longest = "";
    let longestLength = 0; //to keep track for longest substring; && keeps track of #1 palindrome


for (let i = 0; i < s.length; i++) { //assume i is in the middle //for left and right pointers
    let i = 0;
   //odd check - pointers both start at middle and work out; //
    oddLength = checkPalindrome(s, i, i) //calling functions (arguments) ; i stands for left and right pointer
    //check if the substring brought back from Palindrome is the longestLength, if so, update it
  
    //even check - pointers start next to each other
    evenLength = checkPalindrome(s, i, i + 1) //i stands for right pointer and left pointer
    longestLength = Math.max(oddLength, evenLength, longestLength) //can do a check for both odd and even here
}

return longest

}

const checkPalindrome = (s, left, right) => { //parameters for functions
    //return the longest length if this was the middle

    while (left > 0 && right < s.length) { //captures if i + 1 exceeds the boundary for the right scene
        if (s[left] === s[right]) {
            right++
            left--
        } else {
            break //invalid palindrome
        }
    }
    return (right - 1) - (left+ 1) //impacted by one b/c the previous ones were valid palindrome
}

console.log(longestPalindrome("cbbd"))

//time = O (n^2)

//checks memory
//java can't == check
  // ! when do we use split to get each letter

  //[ 0, 1, 2, 3, 4]
  // ! when do you traverse through s.length - 1 vs s.length;
    //s.length is outside of your bound
    //have to use s.length-1 to get the last index when using pointers
    //greatest index is less than the length of the array
        //let letter = s[0] //strings act like arrays