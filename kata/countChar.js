function count(string) {
    //if string empty, return empty hash
    if (!string) return {}
  
    let hash = {};
    
    //iterate through letter in string
    for (let letter of string) {
        //update the value for each letter into the hash
          hash[letter] = (hash[letter] || 0) + 1
      }
    
    return hash;
  }

  console.log(count("ABD"))