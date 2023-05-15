//leetcode 125

const isPalindrome = (s) => {
    //lowercase the string
    //remove the empty spaces
    //create left pointer at the start
    //create right pointer at the end
    //check if they equal each other
    //if they do, keep traversing
    //if they don't, return false

    const newWord = s.toLowerCase();
    const noSpace = newWord.split("");
    console.log(noSpace)

}

console.log(isPalindrome('Jump through the window!'))