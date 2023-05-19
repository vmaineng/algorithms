const reverseVowels = (s) => {
  //split out letters in strings
  //create pointers
  //iterate and create a temp variable
  //if found, switch them
  //if the letter is not in the vowels string, keep iterating

  //return the string

  let letter = s.split("")
  let vowels = "aeiou"
  let i= 0;
  let j = s.length - 1

  while (i < j) {
      if (vowels.includes(letter[i].toLowerCase()) && vowels.includes(letter[j].toLowerCase())){
          [ letter[i], letter[j]] = [letter[j], letter[i]]
          i++
          j--
      } else if (!vowels.includes(letter[i].toLowerCase())) {
          i++
      } else if (!vowels.includes(letter[j].toLowerCase())) {
          j--
      }
  }
  return letter.join("")
};

console.log(reverseVowels("leetcode"));
