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