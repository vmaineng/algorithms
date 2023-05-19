const reverseVowels = (s) => {
    //split out letters in strings
    //create pointers
    //iterate and create a temp variable

    //if the letter is not in the vowels string, keep iterating
    //if found, switch them
    //return the string


const vowels = "aeiou"
let str = s.split("")
let i = 0; 
let j = s.length - 1
let temp = 0;

while (i < j) {
    if (!vowels.includes(str[i]) && !vowels.includes(str[j])) {
       
        j--
        i++
    } else if (vowels.includes(s[i])) {
        temp = str[i]
        str[i] = str[j]
        str[j] = temp
        i++
    } else if (vowels.includes(s[j])) {
        temp = str[i]
        str[i] = str[j]
        str[j] = temp
        j++
    }
 
    return str.join("")
}


}

console.log(reverseVowels("leetcode"))