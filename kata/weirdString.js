function toWeirdCase(string){
    //TODO
    
    //split string into words by spaces
    //iterate through words to find letters
    //find all odd positions, lowercase
    //find all even positions, uppercase them
    let newWord = [];
    
    string = string.split(" ")
    
    for (let word of string) {
      let letter = word.split("")
      if (letter % 2 === 0) {
        newWord.push(letter.toUpperCase());
      } else {
        newWord.push(letter.toLowerCase());
      }
      //return letters together
      return letter.join("");
    }
    //return words together
    return newWord.join(" ")
  }