const mergeAlternately = (word1, word2) => {
  //create a new string
  //iterate through word1 and word 2
  //grab each individual letter
  //push to the new string

  // ! can't do nested for loops b/c it will do apaqaras;
  //it will pair up each letter from the first word and to each letter in second wrod
  //double the work
  //therefore, need to only iterate through the longest length

  let mergedString = "";
  let wordMax = Math.max(word1.length, word2.length);

  for (let i = 0; i < wordMax; i++) {
    //iterate through only the longest string
    if (i < word1.length) mergedString += word1[i];
    //iterate through the first word string making sure i has not reached the end of the string
    //then add the letter the pointer is on
    if (i < word2.length) mergedString += word2[i];
  }
  return mergedString;
};

console.log(mergeAlternately("ab", "pqrs"));
