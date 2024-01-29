function repeatStr (n, s) {
    //get an integer stating how many times to repeat, s is a string
    //return a string of the repeated word/letter provided n times
    
    //ex: (10,"Mai") => "MaiMaiMaiMaiMaiMaiMaiMaiMaiMai"
    
    //create a new string
    //keep repeating the same actions onto the new String n times
    //add the s word/char on to the string
    //return string
    
  //   let newString = "";
  //   for (let i = 0;i < n; i++) {
  //     newString += word
  //     return newString
  //   }
    
    return s.repeat(n)
  }