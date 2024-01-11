function longestSub(string) {
    //get a string of letters
    //return the longest substring w/ no repeating characters
    //'abcdeba'=> 'abcde' => 5

    //if string has only one letter, return 1

    //create a set to hold unique characters
    //store the max integer
    //create a pointer on the first letter and second letter
    //keep moving the right letter down, add it to set
    //if set already has the letter
    //return set.size


const hasLetter = new Set();
let i = 0;
let max = 0;

for (let j = 0; j < string.length; j++) {
   while (hasLetter.has(string[j])) {
        hasLetter.delete(string[i])
        i++;
   }
   hasLetter.add(string[j])
   max = Math.max(max, hasLetter.size )
}
return max;
}

console.log(longestSub('abcdeba'))

//objective: 
//j accounts for new letter so need to check if the letter at j exists yet
//seaerch the entire word
//which then requires shrinking the previous (window) letter seen at i
