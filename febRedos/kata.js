function multiply(a, b){
    return a * b
   }
   

   function simpleMultiplication(number) {
    //receive a number
   // if the output is even, return 8, otherwise 9
   
   //edge cases: if it's not a number
   
   //take the number and multiply by 8
   //if the output is even, return 8; otherwise return 9
   
   return number % 2 === 0 ? number * 8 : number * 9;
 }
 

 // Sum Numbers
function sum (numbers) {
    "use strict";
    
    //get an array of integers
  //return the sum of all the integers added
  //[-1, -2, -2, -34] => -39
  
  //if empty, return 0
  
  //create a sum
  //add up each integer in the loop
  //return the sum
  
  //use reduce to calculate the total
  
  return numbers.length > 0 ? numbers.reduce((acc, cv) => acc + cv, 0) : 0;
};

function makeUpperCase(str) {
    // receive a string of letters
    //return it uppercase
    //"hi" => "HI"
    
    return str.toUpperCase();
  }

  function isIsogram(str){
    //receive a string
    //return true if letters are used once, else false
    //'jump' => true
    //'apple' => false
    
    //edge case: if string is less than 1, it is unique => true
    
    //iterate through the string
    //keep track of the values in a frequnecy counter
    
    //check if the counter has more than two values
    //return false
    
    //otherwise return true after checking;
    
    if (str.length <= 1) return true;
    
    let checkLetter = {};
    
    //PIT frequency counter:
    
    for (let char of str.toLowerCase()) {
      if (checkLetter[char]) { //if character exists already
        return false;
      } else {
        checkLetter[char] = 1
      }
    }
    
    return true;
    
  //   for (let char of str.toLowerCase()) {
  //     checkLetter[char] = checkLetter[char] + 1 || 1
  //   }
    
  //   for (let values in checkLetter) {
  //   if (checkLetter[values] > 1) {
  //     return false;
  //   } 
  //  }
  //   return true;

  //optimized: use a set
  return new Set(str.toLowerCase()).size === str.length;
  }