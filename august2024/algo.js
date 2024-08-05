function caesarCipherEncryptor(string, key) {
  //receive a string of chars with no spaces and lowercase alphabet letters, and a key of integers
  //return a new string with key added

  //'abc', 3 => 'def'

  //create an alphabet to hold all letters of alphabet
  //create a new key % 26 to get the remainders
  //look for the index of each char in string
  // add new index to it with key
  //if new index is greater than 25, then subtract from 26
  //return new letters

  let newWord = [];
  const alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
  let newKey = key % 26;

  for (let char of string) {
    let oldIdx = alphabet.indexOf(char);
    let newIdx = oldIdx + newKey;
    if (newIdx > 25) newIdx -= 26;
    newWord.push(alphabet[newIdx]);
    // console.log(newWord);
  }
  return newWord.join("");
}

// Do not edit the line below.
exports.caesarCipherEncryptor = caesarCipherEncryptor;

// console.log(caesarCipherEncryptor("abc", 3));

function commonChar(strings) {
  //receive an array of strings
  //return an array of common chars
  //['hi', 'hello', 'hey'] => ['h']

  //create a set of the first word
  //iterate through the rest of the array
  //create a new set of second word
  //check if the letters in the first set is found in second set
  //if not, delete from first
  //return first set

  let firstSet = new Set(strings[0]);

  for (let i = 1; i < strings.length; i++) {
    let resetSet = new Set(strings[i]);
    for (let char of firstSet) {
      if (!resetSet.has(char)) {
        firstSet.delete(char);
      }
    }
  }
  return Array.from(firstSet);
}

console.log(commonChar(["hi", "hello", "hey"]));
