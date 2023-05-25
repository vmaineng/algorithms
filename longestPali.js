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

    let left = 0;
    let right = s.length - 1;

    // ! when do we use split to get each letter

    let letters = s.split("")
    let longest = ""

    while (left < right) {
        if (letters[left] === letters[right]) {
            longest += letters[left], letters[right]
        }
    }
return longest

}

console.log(longestPalindrome("cbbd"))