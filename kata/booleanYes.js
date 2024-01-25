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
     
   for (let i = 1; i < str.length; i++) {
     str.substring(i, str.length - 1)
   }
     return str;
   
   };