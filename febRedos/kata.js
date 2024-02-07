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