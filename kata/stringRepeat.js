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

  function greet(name){
    //your code here
    
    return `Hello, ${name} how are you doing today?`
  }

  function findNeedle(haystack) {
    // an array filled with strings, integers of characters/words
    //return the index where the word need is found
    //["needle", "ja", 'rawr', '234', 2]
    
    //edge case:
    //if haystack is empty, return "Your function didn't return anything"
    
    //iterate through each element in the array
    //if the value is "needle",
    //return "found the needle at position " index value
    
    if (!haystack) return "Your function didn't return anything"
    
    // for (let i = 0; i < haystack.length; i++) {
    //   if (haystack[i] === "needle") {
    //     return `found the needle at position ${i}`
    //   } 
    // }
    
return `found the needle at position ${haystack.indexOf("needle")}`

  }

  function lovefunc(flower1, flower2){
    // a value for both flowers
    //return true, if in love, else false
    //if one flower is even and the other flower is odd, true
    //else it's false
    
    // if ((flower1 % 2 === 0) && (flower2 % 2 !== 0)) {
    //   return true
    // } else if ((flower1 % 2 !== 0) && (flower2 % 2 === 0)) {
    //   return true
    // } else {
    //   return false
    // }


    //condense it into one:

    // ! essentially stating that the reminder does not equal the same 
    return flower1 % 2 !== flower2 % 2
  }

  function squareDigits(num){
    //get a number
    //return the number of each digit squared and add them back together as a Number
    //428 => 16464
    
    //if the num is 0, return 0
    
    //take the num and convert to string => "428"
    //traverse through each num and 
    //square the digit
    //then concat them
    //return the number
    
    if (num === 0) return 0;
    
    let answer = "";
    
    let stringNum = String(num);
    
    for (let i = 0; i < stringNum.length;i++) {
      let powNum = Math.pow(parseInt(stringNum[i]), 2)
     answer += powNum
    }
    return Number(answer)
  }

  console.log(squareDigits(3212))

  //3212 => 9424

  function booleanToString(b){
    //boolean - true, false
    //return 'true', 'false' (string type)
    //false => 'false'
    
    return String(b)
    //return b.toString();
  }

  function areYouPlayingBanjo(name) {
    // receive a string of a name
    //return 'plays banjo' if first name is 'R' or 'r', else 'does not play banjo'
    //'joe' => 'does not play banjo'
    //'ro' => 'plays panjo'
  
    
    //check the first letter of the name to see if it equals 'r' or 'R'
    //then return 'plays banjo'
    //else, 'does not play banjo'
    
    
  //   console.log(name[0])
    
    return name[0] === 'r' || name[0] === "R" ? `${name} plays banjo` : `${name} does not play banjo`
  
//return name + (name[0].toLowerCase() === 'r' ? 'plays' : 'does not play ') + 'banjo';

}

function getCount(str) {
    //get a string of characters
    //return the count of vowels existing in the string
    //'jumped' => 2
    
    //initialize a count
    //create an array containing the vowels
    
    //iterate through each letter in string
    //if it's a vowel, increase count
    //return count
    
    let count = 0;
    let vowels = ['a', 'e', 'i', 'o', 'u']
    
    for (let char of str) {
      if (vowels.includes(char)) {
        count++
      }
    }
    return count
  }