function findMissingLetter(array){
    //an array of string letters
    //return the missing letter
    
    //['l', 'm', 'o', 'p','q'] => 'n'
    
    //['a', 'c'] => 'b'
    
    
  const alphabet = 'abcdefghijklmnopqrstuvwxyz'
         //         i            i
         //         0.        12                   
    //['l', 'm', 'o', 'p','q']
    //         j
                             
     //    if i and j point to the same letter, i would keep incrementing though until they no longer match
    
    //return the value from i
  
  let letterIdx = alphabet.indexOf(array[0].toLowerCase()) //index of 'l'
  let j = 0;
    
        for (let i = letterIdx; i < alphabet.length; i++) { //i = a; j = l
          if (alphabet[i] === array[j].toLowerCase()) {
            j++
          } else {
            return array[j].toUpperCase() === array[j] ? alphabet[i].toUpperCase() : alphabet[i]
                  // U   ===  u
          }
        }                     
    
    // let letter.toUpperCase === letter
                             
    
    //if x = y, x++, y++; if x > y, return y; if x < y, return x; 
                          //d > a, return d    //a < l, return 
  }

  //pay attention to whether it's lowercase or uppercase