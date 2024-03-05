function isDivisible(n, x, y) {
    //receive positive integers
    //return true of divisble by x and y, else return false
    //isDivisible(16, 4, 2) => true b/c 16 % 4 = 4 & 16 % 2 = 8
    
    //if n leaves no remainders from x and y, return true, else return false
    
    if (n % x === 0 && n % y === 0) {
      return true
    } else {
      return false;
    }
  }

  var countSheep = function (num){
    //receive an integer
    //return "1 sheep....2 sheep... n sheep"
    //countSheep(4) => "1 sheep....2 sheep...3 sheep...4 sheep"
    
  //iterate up to nums and add a sheep afterwards
    
    let string = ""
    for (let i = 1; i <= num; i++) {
      string += i + ` sheep...`
    }
  return string
  }

  function accum(s) {
	// recive a string of letters
  //return a string where first letter is captialize
  // and for every new letter added, add an addt'l letter
  //'abEd' => 'A - Bb-Eee- Dddd'

//iterate through the string
  //for each letter, capitialize the first one
  //and for each index position, add char letter extra if applicable
  //join them together with a '-'
  
  return s.split("").map((char,idx) => char[0].toUpperCase() + 
char.repeat(idx).toLowerCase()).join('-')
}

function greet (name, owner) {
    // receive string for name and owner
    //return if the name is the same as the owner's, return 'Hello boss', else return 'Hello guest'
    //greet(Mai, Mai) => 'Hello boss'
  
  if (name === owner) {
    return "Hello boss"
  } else {
    return 'Hello guest'
  }
  }

  function dnaStrand(dna){
    //receive a string of letter
    //return a new string back with A replacing T, T relace A, C replace G, and G replace C
    //'TACG' => 'ATGC'
    
    //split the string
    //look through each char, and swap it out with the replacements
    //return new string
    
    let newString = "";
    
    let stringSplit = dna.split("");
    
    for (let i = 0; i <= stringSplit.length; i++) {
      if (stringSplit[i]==='A') {
        newString += 'T'
      } else if (stringSplit[i]==='T') {
        newString += 'A'
    } else if (stringSplit[i]==='C') {
        newString += 'G'
  } else if (stringSplit[i]==='G') {
        newString += 'C'
    }
      }
  return newString
    }