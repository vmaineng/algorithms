function reverseWordsInString(string) {
  //receive a string of words in a string
  //return the words reversed
  //'hello world' => "world hello"

  //create a new string
  //iterate at the end of the string
  //add it in to new string
  //check if it is a space, then add space
  //else add in word
  //return new string

  let newString = "";
  let word = "";

  for (let i = string.length - 1; i >= 0; i--) {
    if (string[i] === " ") {
      console.log(string[i]);
      newString += word + " ";
      word = "";
    } else {
      word = string[i] + word;
    }
  }
  return newString + word;
}

// Do not edit the line below.
exports.reverseWordsInString = reverseWordsInString;

console.log(reverseWordsInString("hello world"));
