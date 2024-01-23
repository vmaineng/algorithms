const perm = (s1, s2) => {
//get two strings of a word
//return true if s2 contains s1
//'barbie', 'aquabarbuous' => false
//'barbie', 'ba' => false

//permutation: substring of exact same size contains same exact characters
//similar to an anagram

//edge case:
//if s2 is smaller than s1, return false;

//use an object to keep track of chars
//iterate through s2
//keep track of the values seen
//once we have seen the same values, return true
//else return false

if (s2.length < s1.length) return false;

let seen = {};

let si1 = 0;

for (let i = 0; i < s2.length; i++) {

}

}

console.log(perm('ab', 'rhinabo'))

//objective; keep a fixed size window