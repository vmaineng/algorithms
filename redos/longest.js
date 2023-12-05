const longestSubstring = (s) =>  {
    //get a string of lowercase with no spaces
    //return the longest length that is unique
    //"green" => "gre"; 

    //if s is empty, return null;

    //initialize a Set to keep track of substring
    //initialize a max to keep track of length of substring
    //iterate through the string until meet same letter, then start new window all over again
    //then take max

    // let longestSub = {};
    // let maxLength = 0;
    // let i = 0;

    // for (let j = 0; j < s.length; j++) {
    //     if (s[j] in longestSub && longestSub[s[j]] >= i) {
    //         i = longestSub[s[j]] + 1;
    //     }

    //     longestSub[s[j]] = j;
    //     maxLength = Math.max(maxLength, j - i + 1)
    // }

    // return maxLength;

    let longestSub = new Set();
    let maxLength = 0;
    let i = 0;

    for (let j = 0; j < s.length; j++) {
        if (longestSub.has(s[j])) {
            j = 
        }
    }
}

console.log(longestSubstring("green"))