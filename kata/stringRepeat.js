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

  function past(h, m, s){
    //get an integer for hour, min, sec
    //return the time in milliseconds
    //milliseconds = 1000 = one thousandth of a second
    
    //past(1, 3, 3) => 360, 90, 3 => 360,000 + 90000 + 3000 => 3690300
    
  //keep a running total
    //calc for hours first
    //add to total
    //calc for mins
    //add to total
    //calc for second
    //add to total
    
    // let sum = 0;
    
    let totalHour = (60 * 60 * h) * 1000 // ! converting hours to mins; then mins to seconds
    let totalMin = (60 * m) * 1000
    let totalSec = (1 * s) * 1000

    return totalHour + totalMin + totalSec
    
    // if (h > 0 || m > 0 || s > 0) {
    //   console.log(totalHour, totalMin, totalSec)
    //   sum += totalHour + totalMin + totalSec
    // }
    // return sum 
  }

  // ! bringinghour and mins to level playing ground with seconds

  function findAverage(array) {
    //get an array of integers
     //return the average from the integers listed
     
     //[2,4,-2, 8] => 12/4 => 3 is average
     
     //if array is empty return 0
     
     //sum up all the integers in array
     //divide it by the length 
     //return avg
     
     if (array.length === 0) return 0;
     
   //   let sum = 0;
   //   let averageSum = 0;
     
   //   for (let i = 0; i < array.length; i++) {
   //     sum += array[i]
   //     averageSum = sum/array.length;
   //   }
   //   return averageSum
     
     let sum = array.reduce((acc, cv) => acc + cv, 0)
     let averageSum = sum/array.length;
     return averageSum;

  }

     function betterThanAverage(classPoints, yourPoints) {
      //receive an array of integers, and then an integer classifying my points
       //return true if myPoints was better than the class, else false
       
       //[2,4,3, 6], 2 => 17/4 => false
       
       //add up the sum in classPoints and divide it by the length to get the average
       //then check to see if the points are less than myPoints, return true
       //else return false
       
       
     //   let sum = 0;
     //   let avgClass = 0;
       
     //   for (let i = 0; i < classPoints.length; i++) {
     //     sum += classPoints[i]
     //     avgClass = sum/classPoints.length
     //   }
       
     //   return avgClass > yourPoints ? false : true
     
      //  let avgClass = classPoints.reduce((acc, cv) => acc +cv, 0)/classPoints.length 
      //  return avgClass > yourPoints ? false : true
     
      return yourPoints > classPoints.reduce((acc, cv) => acc +cv, 0)/classPoints.length 
     }

     function highAndLow(numbers){
      //get a string of numbers with spaces in between
      //return the highest number first, then the lowest number with spaces in between and as strings
      //" 34, 53, 55, -83, 92" => "92 -83"
      
      //if numbers only has one number, return the number as highest and lowest
      
      //split the string by spaces
      //find the max and min
      //join them back by spaces
      
      if (numbers.length === 1) return `${numbers} ${numbers}`
      
      let arrayNum = numbers.split(" ")
      let maxNum = Math.max(...arrayNum)
      let minNum = Math.min(...arrayNum)
      return `${maxNum} ${minNum}`
    }

    const quarterOf = (month) => {
      //get an integer to represent the month
      //return which quarter it is in
      //4 => 1 b/c of first quarter
      
      //edge case:
      //if the number pass in exceeds 12, it's not acceptable
      
      //if the number falls within 1-3, it is 1
      //if number falls within 4 - 7, it is 2
      //if number falls within 8 - 10, it is 3
      //else it is 4
      
      if (month > 12) return "Not acceptable. Please try again"
      
      if (month >= 1 && month < 4) {
        return 1
      } else if (month >= 4 && month < 7){
        return 2
      }   else if (month >= 7 && month < 10){
        return 3
      } else {
        return 4
      }
    }