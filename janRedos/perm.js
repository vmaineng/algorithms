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

if (s1.length > s2.length) return false;

let seen1 = {}; //tracks frequency/count of string1

for (let i = 0; i < s1.length; i++) {
    seen1[s1[i]] = (seen1[s1[i]] || 0) + 1
}
console.log(seen1)

let left = 0;
let right = 0;
let s1Length = s1.length;

while (right < s2.length) {
  
    if (seen1[s2[right]] > 0) s1Length--;
    seen1[s2[right]]--;
    right++

    if (s1Length === 0) return true;

    if (right - left === s1.length) {
        if (s1[s2[left]] >= 0) s1Length++;
        seen1[s2[left]]++
        left++
    }
}
return false;

}

console.log(perm('abdfs', 'rhinabo'))

//objective; keep a fixed size window
//keep track of frequencies to make sure they match
//decrement from s1's length until its 0, return true;
//else after searching entire string, return false 


const perm2 = (s1, s2) => {
    //get two strings of lowercase letters
    //return true if s2 contains s1, else false
    //'joe', 'paeoj' => true => 'eoj'
    //'abcd', 'a' => false

    //edge case:
    //if s2's length is shorter than s1, return false; not enough to search and confirm

    //keep track of the letters seen in s1

    //keep track of s1's length
    //iterate and look through s2's string
    //extend right side of window up to s1's lenth

    //if the window size is = s1's length ,return true;

    //if the right side value exceeds 0, then decrement
    //left side window

    //after searching entire strings, return false


}