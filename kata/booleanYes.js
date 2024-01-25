function boolToWord( bool ){
    //...
    //get a string of boolean value
    //return yes for true, and no for false
    //"yes" => true; 'no' => false
    
//   if (bool === true) {
//     return "Yes"
//   } else {
//     return "No"
//   }
  
// return bool === false ? "No" : "Yes"

return bool ? "Yes" : "No"

//bool itself is a boolean value and its truthiness is being checked;

  }


  function removeChar(str){
    //get a string of word with no spaces and all lowercase
     //return the string back with first and last letter not included
     //'apple' => 'ppl'
     
     //iterate through the string
     //capture the substring and remove the first and last
     //return the string
     
//    for (let i = 1; i < str.length; i++) {
//     for (let letter of str) {
//      let splitWord = str.substring(letter, str.length - 1)
//      console.log(splitWord)
//    }
    //  return splitWord;

    // return str.substring(1, str.length-1)
    return str.slice(1, -1) //slice extracts a section of the string
   
   };

//    console.log(removeChar('apple'))


   function squareSum(numbers){
    //an array of numbers
      //return the sum of all numbers from array
      
      //[1, 2, 3] => 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
      
      //intiialize a sum
      //iterate through the numbers
      //square root it
      //add to sum
      //return sum
      
//       let sum = 0; 
      
//       for (let i of numbers) {
//     // for (let i = 0; i < numbers.length; i++){
//         const sqRoot = i**2
//         console.log(sqRoot, i)
//         sum += sqRoot
//       }

// let sqRtNums = numbers.map(num => Math.exp(num))
// console.log(sqRtNums)

//       return sum

return numbers.reduce((acc, num) => acc + (num **2), 0)

    }

    console.log(squareSum([1,2,3]))