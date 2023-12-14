function firstNonRepeatingLetter(s) {
    // Add your code here
  //string of characters with no spaces
    //return the first character that appears the least
    //'aeae' => ""; //'jarra' => 'j'
  
  //create an object to hold the character count
    //iterate through and keep track of count
    //then find the first intance that has the value of one
    //find the index in the array and return it back
    
//     let lowerChars = s.toLowerCase().split("");
//     let characterCount = {};
//   let result = 0;
    
//     for (let i =0; i < lowerChars.length; i++) {
//       let characterValue = lowerChars[i]
//       characterCount[characterValue] = (characterCount[characterValue] || 0 ) + 1
//   }
//   for (let char in characterCount) {
//   if (characterCount[char] === 1) {
//    let result = char
//    return s[lowerChars.indexOf(result)]
//   }
//   }
//   return "";

let str = s.toLowerCase();
for (let i = 0; i < str.length; i++) {
    //str.indexOf(str[i]) => finds the first occurence index
    //str.lastIndexOf(str[i]) => finds the last occurence index
    // console.log(str.indexOf(str[i]), str.lastIndexOf(str[i]))
    if(str.indexOf(str[i]) === str.lastIndexOf(str[i])) {
        //checks for the first occurence index of the current char is same as last occurence index
        return s[i];
}
}
 return ""; 
  }

  console.log(firstNonRepeatingLetter("ApplleE"))