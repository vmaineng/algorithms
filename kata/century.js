function century(year) {
    //receive integers for a year
    //return what century it is in
    //'3000'=> 29
    
    //if stmts
    
  //   if (year < 101) {
  //     return 1
  //   } else if (year < 1801) {
  //     return 18
  //   } 
  // }
    
    //optimized solution: add one to the yearCount
    //century = 100 years
    return Math.ceil (year/100)
    }