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