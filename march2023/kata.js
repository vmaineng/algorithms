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