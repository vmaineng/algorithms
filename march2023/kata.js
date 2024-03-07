function isDivisible(n, x, y) {
  //receive positive integers
  //return true of divisble by x and y, else return false
  //isDivisible(16, 4, 2) => true b/c 16 % 4 = 4 & 16 % 2 = 8

  //if n leaves no remainders from x and y, return true, else return false

  if (n % x === 0 && n % y === 0) {
    return true;
  } else {
    return false;
  }
}

var countSheep = function (num) {
  //receive an integer
  //return "1 sheep....2 sheep... n sheep"
  //countSheep(4) => "1 sheep....2 sheep...3 sheep...4 sheep"

  //iterate up to nums and add a sheep afterwards

  let string = "";
  for (let i = 1; i <= num; i++) {
    string += i + ` sheep...`;
  }
  return string;
};

function accum(s) {
  // recive a string of letters
  //return a string where first letter is captialize
  // and for every new letter added, add an addt'l letter
  //'abEd' => 'A - Bb-Eee- Dddd'

  //iterate through the string
  //for each letter, capitialize the first one
  //and for each index position, add char letter extra if applicable
  //join them together with a '-'

  return s
    .split("")
    .map((char, idx) => char[0].toUpperCase() + char.repeat(idx).toLowerCase())
    .join("-");
}

function greet(name, owner) {
  // receive string for name and owner
  //return if the name is the same as the owner's, return 'Hello boss', else return 'Hello guest'
  //greet(Mai, Mai) => 'Hello boss'

  if (name === owner) {
    return "Hello boss";
  } else {
    return "Hello guest";
  }
}

function dnaStrand(dna) {
  //receive a string of letter
  //return a new string back with A replacing T, T relace A, C replace G, and G replace C
  //'TACG' => 'ATGC'

  //split the string
  //look through each char, and swap it out with the replacements
  //return new string

  let newString = "";

  let stringSplit = dna.split("");

  for (let i = 0; i <= stringSplit.length; i++) {
    if (stringSplit[i] === "A") {
      newString += "T";
    } else if (stringSplit[i] === "T") {
      newString += "A";
    } else if (stringSplit[i] === "C") {
      newString += "G";
    } else if (stringSplit[i] === "G") {
      newString += "C";
    }
  }
  return newString;
}

function greet(name) {
  if (name === "Johnny") {
    return "Hello, my love!";
  } else {
    return "Hello, " + name + "!";
  }
}

function solution(str, ending){
    // string for both arguments passed in
    //return true if ending is str's end
    //solution('roar', 'er') => false; in order to be true, 'roar', 'ar'
  
  //edge case: if ending is more than str, return false
    //solution('hi', 'hilo') => false

    if (ending.length > str.length) return false;

    // ! loop through ending's word
    //when you loop through str's word, there might be additional
    
    //create pointers for str and ending, both at the last character
    //see if they are the same, then decrement down
    //if they are not the same, we can return false automatically
    //else return true
    
    //'abc', 'bc'
    //   SP    EP 
    
    //  let strPointer = str.length - 1;
    // console.log(ending.length - 1) //index position
  
    // for (let endingPointer = ending.length - 1; endingPointer >= 0; endingPointer--) {
    //   console.log(ending[endingPointer], str[strPointer])
    //   if (ending[endingPointer] !== str[strPointer]) {
    //     return false;
    //   }
    //   strPointer--;
    // }
    // return true;

    return str.endsWith(ending)
  }

console.log(solution('abc', 'bc'))

function rentalCarCost(d) {
    // receive an integer for days
    //return the total amount for different days
    //
    
    //1 days = $40
    //or > 3 days = total - $20
    // > 7 days = total - $50
    
    let total = 0;
    
    if (d < 3) {
      return total = 40 * d
    } else if (d >= 3 && d < 7){
      return total = (40 * d) - 20
    } else {
      return total = (40 * d) - 50
    }
  
  }