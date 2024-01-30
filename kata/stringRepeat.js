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


  class SmallestIntegerFinder {
    findSmallestInt(args) {


      //get an array of integer
      //return the smallest value
      
      //[-342,-453, 452,47, 8] => -453
      
      //set a minNumber to 0;
      //iterate through looking to see if this should be the new min
      //return the minNumber
      
      let minNumber = 0;
      for (let i = 0; i < args.length; i++) {
        console.log(array[i])
        minNumber = Math.min(minNumber, array[i])
        return minNumber
      }


      //return Math.min(...args)
    }
  }

//   console.log(SmallestIntegerFinder(findSmallestInt([-342,-453, 452,47, 8])))

  function countSheeps(sheep) {
    //an array of true or false
    //return the sheeps present in the array
    //[true, false, true, true] => 3
    
    //edge case:
    //if null or undefined or empty, return 0 
    
    //keep count
    //look through each element
    //if true, add to count
    //if false, ignore
    
    //return count
    
    if (!sheep || sheep === undefined || sheep === null) return 0;
    
    // let count = 0;
    // for (let i = 0;i < sheep.length; i++) {
    //   if (sheep[i] === true) {
    //     count += 1
    //   }
    // }
    // return count;
  
    return sheep.filter(Boolean).length;
  }

  console.log(countSheeps([true, false, true, true]))

  function basicOp(operation, value1, value2){
    //string of an operation, an integer, and an integer
    //return the sum of the operation
    //('/', 16, 4) => 4
    
    //if operation is a +, then add the two values
    //if the operation is a -, then subtract the two values
    //if operation is a *, then multiply the two values
    //if the operation is a /, then divide the two values
    
    if (operation === '+') {
      return value1 + value2
    } else if (operation === '-') {
      return value1 - value2
    } else if (operation === '*') {
      return value1 * value2
    } else {
      return value1 / value2
    }
  }