const reverseVowels = (s) => {
  //split out letters in strings
  //create pointers
  //iterate and create a temp variable
  //if found, switch them
  //if the letter is not in the vowels string, keep iterating

  //return the string

  let str = s.split("");
  const vowels = "aeiou";
  let i = 0;
  let j = s.length - 1;

  while (i < j) {
    if (vowels.includes(str[i]) && vowels.includes(str[j])) {
      console.log(str[i], str[j]);
      [str[i], str[j]] = [str[j], str[i] ]
      i++;
      j--;
    }
     if (!vowels.includes(s[i])) {
        i++
    } 
    if(!vowels.includes(str[j])) {
       j--
    }
  }

  return str.join("");
};

console.log(reverseVowels("leetcode"));
