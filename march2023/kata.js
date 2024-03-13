function isDivisible(n, x, y) {
  //receive positive integers
  //return true of divisble by x and y, else return false
  //isDivisible(16, 4, 2) => true b/c 16 % 4 = 4 & 16 % 2 = 8

  //if n leaves no remainders from x and y, return true, else return false

  if (n % x === 0 && n % y === 0) {
    return true;
  } else {
    return false;
  }
}

var countSheep = function (num) {
  //receive an integer
  //return "1 sheep....2 sheep... n sheep"
  //countSheep(4) => "1 sheep....2 sheep...3 sheep...4 sheep"

  //iterate up to nums and add a sheep afterwards

  let string = "";
  for (let i = 1; i <= num; i++) {
    string += i + ` sheep...`;
  }
  return string;
};

function accum(s) {
  // recive a string of letters
  //return a string where first letter is captialize
  // and for every new letter added, add an addt'l letter
  //'abEd' => 'A - Bb-Eee- Dddd'

  //iterate through the string
  //for each letter, capitialize the first one
  //and for each index position, add char letter extra if applicable
  //join them together with a '-'

  return s
    .split("")
    .map((char, idx) => char[0].toUpperCase() + char.repeat(idx).toLowerCase())
    .join("-");
}

function greet(name, owner) {
  // receive string for name and owner
  //return if the name is the same as the owner's, return 'Hello boss', else return 'Hello guest'
  //greet(Mai, Mai) => 'Hello boss'

  if (name === owner) {
    return "Hello boss";
  } else {
    return "Hello guest";
  }
}

function dnaStrand(dna) {
  //receive a string of letter
  //return a new string back with A replacing T, T relace A, C replace G, and G replace C
  //'TACG' => 'ATGC'

  //split the string
  //look through each char, and swap it out with the replacements
  //return new string

  let newString = "";

  let stringSplit = dna.split("");

  for (let i = 0; i <= stringSplit.length; i++) {
    if (stringSplit[i] === "A") {
      newString += "T";
    } else if (stringSplit[i] === "T") {
      newString += "A";
    } else if (stringSplit[i] === "C") {
      newString += "G";
    } else if (stringSplit[i] === "G") {
      newString += "C";
    }
  }
  return newString;
}

function greet(name) {
  if (name === "Johnny") {
    return "Hello, my love!";
  } else {
    return "Hello, " + name + "!";
  }
}

function solution(str, ending){
    // string for both arguments passed in
    //return true if ending is str's end
    //solution('roar', 'er') => false; in order to be true, 'roar', 'ar'
  
  //edge case: if ending is more than str, return false
    //solution('hi', 'hilo') => false

    if (ending.length > str.length) return false;

    // ! loop through ending's word
    //when you loop through str's word, there might be additional
    
    //create pointers for str and ending, both at the last character
    //see if they are the same, then decrement down
    //if they are not the same, we can return false automatically
    //else return true
    
    //'abc', 'bc'
    //   SP    EP 
    
    //  let strPointer = str.length - 1;
    // console.log(ending.length - 1) //index position
  
    // for (let endingPointer = ending.length - 1; endingPointer >= 0; endingPointer--) {
    //   console.log(ending[endingPointer], str[strPointer])
    //   if (ending[endingPointer] !== str[strPointer]) {
    //     return false;
    //   }
    //   strPointer--;
    // }
    // return true;

    return str.endsWith(ending)
  }

console.log(solution('abc', 'bc'))

function rentalCarCost(d) {
    // receive an integer for days
    //return the total amount for different days
    //
    
    //1 days = $40
    //or > 3 days = total - $20
    // > 7 days = total - $50
    
    let total = 0;
    
    if (d < 3) {
      return total = 40 * d
    } else if (d >= 3 && d < 7){
      return total = (40 * d) - 20
    } else {
      return total = (40 * d) - 50
    }
  
  }

  // return masked string
function maskify(cc) {
    //receive a string - numbers or characters
      //return a new string and cover everything with #, excep tthe last four
      //'applesauce' => '######auce'
      
      //initialize a new string
      //iterate through the string
      //check if it is not the last four, then add it to the string as #
      //else, enter it is the value
      
    //edge case: if length is less than 4, return the same string back
    if (cc.length < 4) return cc
      
      let maskedString = "";
      let splitStr = cc.split("");
      
      for (let i = 0; i < splitStr.length; i++) {
        if (i < splitStr.length - 4) {
          maskedString += '#'
        } else{
          maskedString += splitStr[i]
        }
      }
      return maskedString
    
// return masked string
function maskify(cc) {
    const last4Digits = cc.slice(-4)
    return last4Digits.padStart(cc.length, '#')
    }
    
    }
    
    function getGrade (s1, s2, s3) {
        // receive 3 scores
        //return the letter value associated with it
        
        //getGrade(42, 85, 55) => 42 + 85 + 55 / 3 => 60.67 => 'D'
        
        //find the average of the score
        //if the score is between 90 and 100, it's an 'A'
        
        let gradeAverage = (s1 + s2 + s3)/3
        console.log(gradeAverage)
        
        if (gradeAverage >= 90 ) {
          return 'A'
        } else if (gradeAverage >=80 && gradeAverage < 90){
          return 'B'
        } else if (gradeAverage >=70 && gradeAverage < 80){
          return 'C'
        } else if (gradeAverage >=60 && gradeAverage < 70){
          return 'D'
        } else {
          return 'F'
        }
      }

      function friend(friends){
        //receive an array of string
        //return an array with string that contains only name with 4 letters in it
        //friend(['Mai', 'Joe', 'Joey', 'Mary']) => ['Joey', 'Mary']
      
      //iterate through, and return the array where string's length is excactly 4
        
      //   return friends.map((friend) => friend.length === 4 ? )
        
        let newFriend = []
        
        for (let i = 0; i < friends.length;i++) {
          const name = friends[i]
      console.log(name)
          if (name.length === 4) {
            newFriend.push(name)
          }
        }
      return newFriend

      return friends.filter(friend => friend.length === 4)
      }

      class Kata {
        static getVolumeOfCuboid(length, width, height) {
          // receive postive whole number integers 
          //return the volume
          
          //getVolofCuboid(4, 5, 5) = taking (width * height) * length = 100
          
          return (width * height) * length
        }
      }

      function addBinary(a,b) {
        //receive two numbers (positive)
          //return the binary number in a string
          
          //addBinary(9, 3) => 12 => "0011"
        //12/2 = 6 = 0
          //6/2 = 3 = 0
          //3 /2 = 1
          //1 /2 = 0
        
        //add the two numbers together
          //divide the total by 2,
          //if a remainder, it's a 1, else it's a 0
          //add 0 to the string
        
          
          
        //   let binaryNumber = "";
        //   let total = a + b;
          
        //   //edge case: if total is 0, return "0"
        //   if (total === 0) return '0';
        
        //   while (total > 0) {
        //   let remainder = total % 2 
        //     binaryNumber = remainder + binaryNumber
        //     total = Math.floor(total / 2);
        //       }
        // return binaryNumber

        return (a+b).toString(2)
        }

        function removeExclamationMarks(s) {
            //receive a string of characters
            //return the word back with no '!'
            //"Jump In!" => "Jump In"
          
          //split string into an array, filter out '!', join it back together
            
            //  return s.split(" ").filter((str) => str !== '!').join(" ")
             //let splitS = s.split(" ") //[ 'Jump', 'In!' ]
                //let splitS = s.split("") //
             console.log(splitS) // [
            //     'J', 'u', 'm',
            //     'p', '!', ' ',
            //     'I', 'n', '!'
            //   ]

            // return s.replaceAll("!", "")
          }

          console.log(removeExclamationMarks('Jump! In!'))

          function longest(s1, s2) {
            //receive two strings
            //return one string sorted
            //a='apple', b='banana' => 'abelnp'
            
            //edge case, if one string is empty, rturn the other, vice versa;
            //use a Set
            //iterate through s1 and add to Set,
            //then iterate in s1, check if Set does not have it, add
            //return the set back sorted
            
            if (!s1) return s2;
            if (!s2) return s1;
            
        //     let seenValues = new Set();
            
        //     for (let i = 0; i < s1.length; i++) {
        //       const s1Char = s1[i]
        //       if (!seenValues.has(s1Char)){
        //         seenValues.add(s1Char)
        //       }
        //     }
            
        //     for (let i = 0; i < s2.length; i++){
        //       const s2Char = s2[i]
        //    if (!seenValues.has(s2Char)){
        //         seenValues.add(s2Char)
        //       }
        //     }
        //     return Array.from(seenValues).sort().join("")

        return [...new Set(s1 + s2)].sort().join("");
        //concats the strings together
        //creats a new Set from the strings to ensure unique chars
        //spread out the elements into an array; converts set back into an array;
        //sort the characters 
        //join it back together with strings from the array element
          }


          function points(games) {
            //receive an array of string key value pair
             //return total points x achieved
             //"3: 1"
             // x: y = 3 points
             
             //["4:0", "2:4", "3: 5"] => 3 + 0 + 0 = 3 points
             
             //edge case: if there are less than 10 matches, then it's not valid
             
             //initialize a total
             //iterate over every string
             //check if the first value is > second value, add 3 points
             //or if first value is < second value, add 0 points
             //else add one point if tied
             
        //      let total = 0;
             
        //      for (let str of games) {
        //    //     console.log(str[0], str[2])
        //        if (str[0] > str[2]) {
        //          total += 3
        //        } else if (str[0] < str[2]) {
        //          total += 0
        //        } else {
        //          total += 1
        //        }
        //      }
        //      return total

        // ! reduce method can be used strings and arrays

        return games.reduce((game, element) => { // ! game = accummulated value and element is CV being processed
            let arraySplit = element.split(":");
            return (arraySplit[0] > arraySplit[1]) ? game += 3 : (arraySplit[0] < arraySplit[1]) ? game += 0 : game+= 1
        }, 0);
           }

           function updateLight(current) {
  
            //receive a string of one color
            //return the next following color afterwards
            
            //'red' => 'green'
            
            //if else stmts?
            
            if (current === 'green') {
              return 'yellow'
            } else if (current === 'yellow') {
              return 'red'
            } else if (current === 'red') {
              return 'green'
            }
          
          }