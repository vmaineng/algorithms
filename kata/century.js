function century(year) {
    //receive integers for a year
    //return what century it is in
    //'3000'=> 30
    
    //if stmts
    
  //   if (year < 101) {
  //     return 1
  //   } else if (year < 1801) {
  //     return 18
  //   } 
  // }
    
    //optimized solution: add one to the yearCount
    //century = 100 years
    return Math.ceil (year/100) //using ceiling method to round up to nearest century (100)
    }

    // console.log(century(3000))

    function abbrevName(name){

        //receive a name with a space
      //return initials uppercase
      //"ma van" => "M.V"
    
      //edgecase:
      //if they only provide first or last name, capitalize the first letter
      
    //create a new string
      //iterate through
      //push the first letter of first part
      //push first letter of second part
    //return string uppercase
    
//split on spaces
//map through it and grab first letter
//return it capitalize

return name.split(" ").map(letter => letter[0].toUpperCase()).join(".")
      
    }

    console.log(abbrevName("ma van"))