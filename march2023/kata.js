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

function solution(str, ending) {
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

  return str.endsWith(ending);
}

console.log(solution("abc", "bc"));

function rentalCarCost(d) {
  // receive an integer for days
  //return the total amount for different days
  //

  //1 days = $40
  //or > 3 days = total - $20
  // > 7 days = total - $50

  let total = 0;

  if (d < 3) {
    return (total = 40 * d);
  } else if (d >= 3 && d < 7) {
    return (total = 40 * d - 20);
  } else {
    return (total = 40 * d - 50);
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
  if (cc.length < 4) return cc;

  let maskedString = "";
  let splitStr = cc.split("");

  for (let i = 0; i < splitStr.length; i++) {
    if (i < splitStr.length - 4) {
      maskedString += "#";
    } else {
      maskedString += splitStr[i];
    }
  }
  return maskedString;

  // return masked string
  function maskify(cc) {
    const last4Digits = cc.slice(-4);
    return last4Digits.padStart(cc.length, "#");
  }
}

function getGrade(s1, s2, s3) {
  // receive 3 scores
  //return the letter value associated with it

  //getGrade(42, 85, 55) => 42 + 85 + 55 / 3 => 60.67 => 'D'

  //find the average of the score
  //if the score is between 90 and 100, it's an 'A'

  let gradeAverage = (s1 + s2 + s3) / 3;
  console.log(gradeAverage);

  if (gradeAverage >= 90) {
    return "A";
  } else if (gradeAverage >= 80 && gradeAverage < 90) {
    return "B";
  } else if (gradeAverage >= 70 && gradeAverage < 80) {
    return "C";
  } else if (gradeAverage >= 60 && gradeAverage < 70) {
    return "D";
  } else {
    return "F";
  }
}

function friend(friends) {
  //receive an array of string
  //return an array with string that contains only name with 4 letters in it
  //friend(['Mai', 'Joe', 'Joey', 'Mary']) => ['Joey', 'Mary']

  //iterate through, and return the array where string's length is excactly 4

  //   return friends.map((friend) => friend.length === 4 ? )

  let newFriend = [];

  for (let i = 0; i < friends.length; i++) {
    const name = friends[i];
    console.log(name);
    if (name.length === 4) {
      newFriend.push(name);
    }
  }
  return newFriend;

  return friends.filter((friend) => friend.length === 4);
}

class Kata {
  static getVolumeOfCuboid(length, width, height) {
    // receive postive whole number integers
    //return the volume

    //getVolofCuboid(4, 5, 5) = taking (width * height) * length = 100

    return width * height * length;
  }
}

function addBinary(a, b) {
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

  return (a + b).toString(2);
}

function removeExclamationMarks(s) {
  //receive a string of characters
  //return the word back with no '!'
  //"Jump In!" => "Jump In"
  //split string into an array, filter out '!', join it back together
  //  return s.split(" ").filter((str) => str !== '!').join(" ")
  //let splitS = s.split(" ") //[ 'Jump', 'In!' ]
  //let splitS = s.split("") //
  //console.log(splitS); // [
  //     'J', 'u', 'm',
  //     'p', '!', ' ',
  //     'I', 'n', '!'
  //   ]
  // return s.replaceAll("!", "")
}

console.log(removeExclamationMarks("Jump! In!"));

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

  return games.reduce((game, element) => {
    // ! game = accummulated value and element is CV being processed
    let arraySplit = element.split(":");
    return arraySplit[0] > arraySplit[1]
      ? (game += 3)
      : arraySplit[0] < arraySplit[1]
      ? (game += 0)
      : (game += 1);
  }, 0);
}

function updateLight(current) {
  //receive a string of one color
  //return the next following color afterwards

  //'red' => 'green'

  //if else stmts?

  if (current === "green") {
    return "yellow";
  } else if (current === "yellow") {
    return "red";
  } else if (current === "red") {
    return "green";
  }
}

function openOrSenior(data) {
  //receive an array of array of age, handicap level
  //return an array back if they are classified as 'Senior' or 'Open'
  //([[52, 3], [78, 23], [16, 3]]) => ['Open', 'Senior', 'Open']

  //iterate through the data set
  //check if the age is 55 years and older
  //then check the handicap level if it is > 7
  //return 'Senior' if both conditions are met
  //else return 'Open'

  //   let output = [];

  //   for (let i = 0; i < data.length; i++) {
  //     //   console.log(data[i])
  //     let dataSet = data[i];
  //     if (dataSet[0] >= 55 && dataSet[1] > 7) {
  //       output.push("Senior");
  //     } else {
  //       output.push("Open");
  //     }
  //   }
  //   return output;

  return data.map(([age, handicap]) =>
    (age >= 55) & (handicap > 7) ? "Senior" : "Open"
  );
}

function setAlarm(employed, vacation) {
  //receive two boolean for employed and vacation
  //return boolean;
  //if vacation is true, then return false
  //if not employed and not on vacation, return false
  //else return true

  //   if (vacation === true && employed === false) {
  //     return false
  //   }  else if (employed === true && vacation === false) {
  //     return true
  //   } else if (employed === false && vacation === false) {
  //     return false
  //   } else {
  //     return false
  //   }

  return employed && !vacation;
}

var number = function (busStops) {
  // get an array of arrays = [people who get on the bus, people who get off the bus]
  //return the amount of people who still left on the bus
  //[[4, 0], [5, 2], [3,6]] =>
  //4 people get on, 5 people who get on (9), 2 people left (7)
  //3 people get on(10), then 6 people get off => 4

  //edge case: the amount of people who get off cannot surpass the amt that are on the bus

  //initialize an amt for people on bus
  //iterate through and subtract from total amt on bus
  //return total

  //   return busStops.map(([getOn, getOff]) => )

  //   let totalPeople = 0;

  //   for (let i = 0; i < busStops.length; i++) {
  //     //     console.log(busStops[i])
  //     const peopleSet = busStops[i];
  //     totalPeople += peopleSet[0];
  //     totalPeople -= peopleSet[1];
  //   }
  //   return totalPeople;

  return busStops.reduce((total, [on, off]) => total + on - off, 0);
};

// return names.filter((name) => name.length > 5)

function switchFlick(array) {
  let switchBoolean = true;
  return array.map((word) => {
    if (word === "flick") {
      switchBoolean = !switchBoolean;
    }
    return switchBoolean;
  });
}

console.log(switchFlick(["jump", "flick", "app", "flick", "trust"]));

// return array.map((num) => typeof num === 'number')

for (let char of string) {
  if (answer.hasOwnProperty(char)) {
    answer[char]++;
  } else {
    answer[char] = 1;
  }
}

function howMuchILoveYou(nbPetals) {
  // receive a number
  //return a string based on the total amount petals plucked from the flower
  //petals(9) => 'a lot'

  //any remainders left over aligns with

  // if (nbPetals % 6 === 1) {
  //   return "I love you"
  // } else if (nbPetals % 6 ===  2) {
  //   return 'a little'
  // } else if (nbPetals % 6 === 3) {
  //   return "a lot"
  // }  else if (nbPetals % 6 === 4) {
  //   return "passionately"
  // }  else if (nbPetals % 6 === 5) {
  //   return "madly"
  // }  else {
  //   return "not at all"
  // }

  const phrases = [
    "I love you",
    "a little",
    "a lot",
    "passionately",
    "madly",
    "not at all",
  ];

  return phrases[(nbPetals - 1) % phrases.length];
}

function gaslighting(shirtWord, yourWord, friendsLetters) {
  //receive strings for all 3
  //return true if friend knows you're fooling him, else return false
  //'jump', 'pump',[p] => true

  //traverse through shirtWord and yourWord,
  //compare each letter to each other and check if the friendsLetters exist in shirtWord
  //return true

  //return false

  //edge case: if the strings are smaller than the friendsLetters?

  for (let i = 0; i < shirtWord.length; i++) {
    // Check if the letters are different
    if (
      (shirtWord[i] !== yourWord[i] &&
        !friendsLetters.includes(shirtWord[i])) ||
      !friendsLetters.includes(yourWord[i])
    ) {
      return true; // Friend knows you're fooling
    }
    return false; // Friend does not know
  }
}

function sumMix(x) {
  //receive an array of integers and string of numbers
  //return total sum
  //["3", "6",'4', 1] => 14

  //keep a total amount
  //iterate through array
  //if it is a string, then turn it into an integer and add to total
  //else it's a number, and add to the total
  //return total

  //   let total = 0;
  //   for (let i = 0;i < x.length;i++) {
  //     if (typeof x[i] === 'string') {
  //       total += parseInt(x[i])
  //     } else {
  //       total += x[i]
  //     }
  //   }
  // return total;

  return x.reduce((total, cv) => total + Number(cv), 0);
}

function reverseWords(str) {
  let reversedWord = "";
  let reversedStr = "";

  for (let i = 0; i < str.length; i++) {
    if (str[i] !== " ") {
      reversedWord = str[i] + reversedWord;
    } else {
      reversedStr += reversedWord + " ";
      reversedWord = ""; //clear it back to empty
    }
  }
  return reversedStr + reversedWord;

  //return str.split(" ").map(word => word.split("").reverse().join("")).join(" ")
}

function goals(laLigaGoals, copaDelReyGoals, championsLeagueGoals) {
  // receive an integer for all 3's
  //return the total sum of all 3 integers
  //goals(2, 4, 8) => 14

  //edge case: there's no negative points

  return laLigaGoals + copaDelReyGoals + championsLeagueGoals;
}

function removeSmallest(numbers) {
  //receive an array of integers
  //return back an array of integers with the smallest value removed
  //if multiple smallest value, remove the lowest index one

  //smallest([1,2, 3, 1, 5,2]) => [2, 3, 1, 5, 2]

  //create a copy of the numbers array
  //find the min index
  //slice it out
  //return it

  const copyNumbers = numbers.slice(0);
  const minValue = numbers.indexOf(Math.min(...numbers));
  copyNumbers.splice(minValue, 1);
  return copyNumbers;

  //return numbers.filter((num) => num !== numbers.indexOf(Math.min(...numbers)))
}

function nameFiil(names) {
  return names.filter((name) => name.length === 4);
}

function switcheroo(array) {
  let switchBolean = false;
  return array.map((word) => {
    if (word === "flick") {
      switchBolean = !switchBolean;
      return switchBolean;
    }
  });
}

function revWords(string) {
  //receive a string with spaces
  //return the string in reverse
  //"double space" => "ecaps elbuod"

  //split the words into their own separate word
  //iterate through the word
  //and add in current letter to the beginning
  //then add the word back into a new string
  //return the string

  let revWord = "";
  let revStr = "";

  for (let i = 0; i < string.length; i++) {
    if (string[i] !== " ") {
      revWord = string[i] + revWord;
    } else {
      revStr += revWord + " ";
      revWord = "";
    }
    return revStr + revWord;
  }
}

//return numbers.filter((num) => num !== numbers.indexOf(Math.min(...numbers)))
//const copyNumbers = numbers.slice(0);
//const minValue = numbers.indexOf(Math.min(...numbers));
//copyNumbers.splice(minValue, 1);
//return copyNumbers;

function arithmetic(a, b, operator) {
  //integers for a and b, and a string to state what operator is
  //return the total based on what the operation stated
  //4, 6, "subtract" => 4 - 6 = -2

  //if the operator states "add", add a + b
  //if operator states "subtract", a - b
  //multiply, a * b
  //divide, a / b

  // if (operator === "add") {
  //   return a + b
  // } else if (operator === "subtract") {
  //   return a - b
  // } else if (operator === "multiply") {
  //   return a * b
  // } else {
  //   return a /b
  // }

  switch (operator) {
    case "add":
      return a + b;
      break;
    case "subtract":
      return a - b;
      break;
    case "multiply":
      return a * b;
      break;
    case "divide":
      return a / b;
  }
}

//have to create an empty string for the word, and for the reversed String
//iterate through the string
//add in the letter to the remaining word
//check if you have encountered a space
//if so, clear the word and add the reversed word to the string
//return string

let revWord = "";
let revStr = "";

for (let i = 0; i < str.length; i++) {
  if (str[i] !== " ") {
    revWord = str[i] + revWord;
  } else {
    revStr += revWord + " ";
    revWord = "";
  }
  return revStr + revWord;
}

//return numbers.filter((num, idx) => idx !== numbers.indexOf(Math.min(...numbers)))

//switch case = stmt and you're evaulating an expression and there are cases for each expression
//also a default you could use

switch (operator) {
  case "add":
    return a + b;
    break;
  default:
    console.log("can't find");
}

function twiceAsOld(dadYearsOld, sonYearsOld) {
  // receive two ingeters for dad's age and son's age
  //return how many years ago father was 2x as old as his son
  //twiceAsOld(40, 10) => 10 * 2 = 20; 40 -20 = 20;

  //calc twice Son's age;
  //then subtract from dad's current age;
  //return the age

  //36 , 7 => 7 * 2 = 14; 36 - 14 = 22
  //30 * 2 = 60; 55 - 60 = 5

  let twiceSonAge = sonYearsOld * 2;
  const dadTwice = Math.abs(dadYearsOld - twiceSonAge);
  return dadTwice;
}

function oddOrEven(array) {
  //receive an array of integers
  //return "odd" or "even" based on total amount
  //[0] => 'even'; [0, 2, 4, 1] => 7 => 'odd'

  //edge case: if it is 0, or empty, return 'even';

  //create a total
  //iterate through the array
  //add up to the total
  //check if the total leaves any remainder, then it's odd
  //else it's even

  if (array.length === 0) return "even";

  let total = 0;

  for (let i = 0; i < array.length; i++) {
    total += array[i];
  }
  if (total % 2 === 0) {
    return "even";
  } else {
    return "odd";
  }

  //return array.reduce((accum, cv) => accum + cv, 0) % 2 ? 'even' : 'odd'
}

//return names.filter((name) => name.length === 4)

function pillars(number, distance, width) {
  //return total distance between 1st pillar and last pillar

  //calc distance
  //1m = 100cm
  //omit the first pillar

  let totalDistance = distance * 100 * (number - 1);
  let totalWidth = (number - 2) * width;
  return totalDistance + totalWidth;

  //edge case: if 1 pillar, then return 0
}

const flick = (array) => {
  let switchBool = true;
  return array.map((str) => {
    if (str === "flick") {
      switchBool = !switchBool;
    }
    return switchBool;
  });
};

function hoopCount(n) {
  //receive an integer
  //return a certain message depending on how many numbers received
  //17 => "Great, now move on to tricks"

  //if n >=10, "Great, now move on to tricks", else "Keep at it until you get it"

  return n >= 10
    ? "Great, now move on to tricks"
    : "Keep at it until you get it";
}

const sequenceSum = (begin, end, step) => {
  // receive all 3 integers
  //return the total from begin, end, by the steps taken
  //(2, 8, 2) => (2 + 4 + 6 + 8) => 20

  //if begin value > end, return 0
  //if end is not the result of the steps taken, don't add to sum

  //create a total sum
  //start at begin, iterate up to end, increment by step
  //add each number
  //return total

  if (begin > end) return 0;

  let total = 0;

  for (let i = begin; i <= end; i += step) {
    total += i;
  }
  return total;
};

//(goose- 1) % goose.length;

function isoGram(string) {
  //takes in a string of characters
  //return true if no repeating letters
  //'jump' = true

  //create an object
  //store the values
  //check if the values exist
  //if there's a value in there already, return false
  //else return true

  let seenVals = {};

  let lowercaseStr = string.toLowerCase();

  for (let letter of lowercaseStr) {
    if (!seenVals[letter]) {
      seenVals[letter] = 1;
    } else {
      return false;
    }
  }
  return true;
}

function firstNonConsecutive(arr) {
  //receive an array of integers
  //return the digit that's not consecutive, which means +1 after the previous digit
  //[1,2,3,8,9] => 8

  //if array is empty, return null

  //iterate through the array
  //start at the second element, compare it to the previous value
  //if it is not consecutive, return the value
  //else return null

  if (!arr) return null;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] !== arr[i - 1] + 1) {
      //take the value at arr[i] and compare it to (move the index down by 1) then add by 1
      return arr[i];
    }
  }
  return null;
}
function breakChocolate(n, m) {
  //get a row and column of integer (whole number)
  //return total amount of splits you need to make
  //breakChoc(6, 6) =>

  //if input dad is invalid, rturn 0 b/c no breaks are neccessary;

  //edge case
  //n = columns
  //m = rows

  //horizontal and vertical breaks:
  // (n-1) || (m - 1) b/c there are only n - 1 spaces between the rows b/c the last row doesnt need a break

  //columns * rows -1

  if (n === 0 || m === 0) return 0;

  return n * m - 1;
}

function between(a, b) {
  // receive two integers
  //return an array back of all the integers between a and b
  //[8, 12] => [8, 9, 10, 11, 12]

  //edge case: if a > b, return empty array

  //create an empty array
  //iterate starting at a, and keep going until reach b
  //push the integer into the empty array
  //return array

  if (a > b) return [];

  let answer = [];
  for (let i = a; i <= b; i++) {
    answer.push(i);
  }
  return answer;
}

function calculateYears(principal, interest, tax, desired) {
  // receive integers for all parameters
  //return how many years it will take to receive desired outcome

  //capture years
  //capture principal=principal+((principal*interest)-(principal*interest*tax))
  //if principle < desired, return years

  let years = 0;

  while (principal < desired) {
    years++;
    principal = principal + (principal * interest - principal * interest * tax);
  }
  return years;
}

function stray(numbers) {
  //receive an array of integers
  //return which number is odd one out
  //[3, 4, 3, 3, 3] => 4

  //sort it
  //check if the first value is not the same as the second value
  //then return the first value
  //else return the value at the end

  let sortedArray = numbers.sort();

  if (sortedArray[0] !== sortedArray[1]) {
    return sortedArray[0];
  } else {
    return sortedArray[sortedArray.length - 1];
  }
}

function switchItUp(number) {
  switch (number) {
    case 1:
      return "One";
      break;
    case 2:
      return "Two";
      break;
    case 3:
      return "Three";
      break;
    case 4:
      return "Four";
      break;
    case 5:
      return "Five";
      break;
    case 6:
      return "Six";
      break;
    case 7:
      return "Seven";
      break;
    case 8:
      return "Eight";
      break;
    case 9:
      return "Nine";
      break;
  }
}
