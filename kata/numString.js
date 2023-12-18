//convert number to a string

function numberToString(num) {
  //an integer (whole)
  //return the integer to strings
  //345 => '345

  return num.toString();
}

//console.log(numberToString(456))

function ops(num) {
  //a whole integer
  //return the opposite of number
  //-4 => 4

  return -num;
}
// console.log(ops(-4))

function positiveSum(arr) {
  //get an array of num both positive and negative
  //return total of positive numbers
  //[1, -4, 3, 5 ] => 9; [-3, -4, -5] => 0

  //initialize a total at 0;
  //iterate through the nums
  //check to see if greater than 0, then add to total
  //return total;

  // let total = 0;

  // for (const num of arr) {
  //     if (num > 0) {
  //         total += num
  //     }
  // }
  // return total;
  return arr.reduce((a, b) => a + (b > 0 ? b : 0), 0);
}

// console.log(positiveSum([1, -4, 3, 5]))

function makeNegative(num) {
  //get an integer
  //return the negative number of it
  //9 => -9; -4 => -4

  //if number is 0, return 0
  //if number is positive, make it negative
  //otherwise if number is negative already, return the number

  if (num === 0) return 0;
  return num > 0 ? -num : num;
}

// console.log(makeNegative(-4))

function noSpace(x) {
  //get a string with spaces
  //return the string back with no spaces
  //'test this algo' => 'testthisalgo'

  //split by spaces
  //join back
  //return the string

  //   return x.split(" ").join("")

  let result = "";
  for (let i = 0; i < x.length; i++) {
    if (x[i] !== " ") {
      result += x[i];
    }
  }
  return result;
}

// console.log(noSpace("test this algo"))

function litres(time) {
  //get a number in time
  //return how many litres Nathan needs to drink
  //for 1 hour, he needs to drink 0.5 litres
  //round down
  //time = 3 => 1 hr = 0.5 ; 2hr => 1; 3 hours => 1.5 litres

  //return the time * 0.5
  return Math.floor(time * 0.5);
}

// console.log(litres(6.7))

function maps(x) {
  return x.map((num) => num * 2);
}

var summation = function (num) {
  //an integer
  //return the numbers adding up to the integer
  //1 => 1
  //2 => 1 + 2 => 3
  //4 => 1 + 2 + 3 +4  = 10

  //iterate up to the numb and add to the total
  //     let total = 0;
  //     let n = 1;
  //    while (n <= num ) {
  //   total += n
  //      n++
  //   }

  //   return total;

  let total = 0;

  for (let i = 1; i <= num; i++) {
    total += i; //add the i's since there is no num[i]
  }
  return total;
};

//   console.log(summation(1))

function findOdd(A) {
  //an array of integers
  //return which number that appears odd times
  //[3, 4, 5, 3, 4, 5, 3] => 3 b/c 3; 4: 2; 5: 2

  //if the length is one, return the number

  //create an object
  //iterate through array
  //keep track of how many times I've seen it
  //return the key that appears an odd amount of time
  //frequency of key is odd
  //even or odd: % ; 0 even ; odd

  if (A.length === 1) return A[0];

  let visited = {}; //{ 0: 3, 1: 2 }
 let oddCount = 0;

  for (let i = 0; i < A.length; i++) {
    //build the values
    //0 = 1; +1
    visited[A[i]] = visited[A[i]] + 1 || 1; // {0: 5, 1: 3}
  }
  //if it exists in the object, do this; else do that;

  for (const key in visited) {
    //looking at keys odd frequency
    if (visited[key] % 2 !== 0) {
        oddCount = Math.max(oddCount, visited[key]) //
    //   console.log(visited[key]);
     }
  }
  return oddCount;
}
//time: O(n) //it doesn't grow as n grow
//space: O(n)

// console.log(findOdd([0,1,0,1,0,1,0,0]))

function paperwork(n, m) {
  //integers - negative and positive
  //return the amount of pages needed
  //n= -4; m = 4 => 0; n = 4, m = 10 => 40
  
  //if n or m is negative, return 0
  //return n * m
  
  if (n < 0 || m < 0) return 0;
  
  let total = n * m
  return total;
}

function solution(str){
  return str.split('').reverse().join('');  
}

function solution(number){
  //an integer number
  //return the total of all numbers divisible by 3 and/or 5 
  //15 => 3, 5, 6, 9, 15 => 38
  
  //edge case: if number is <0, return 0;
  
  //intiailize a total
  //iterate up to the number provided
  //check to see if it the number is divisible by 3 & 5
  //add to total
  //check to see if it is divisble by 5
  //add to total
  //check to see if it is divisble by 3
  //add to total
  //return total
  
  if (number < 0) return 0;
  
  let total = 0;
  
  for (let i = 1; i < number; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      total += i
    } else if (i % 3 === 0) {
      total += i
    } else if (i % 5 === 0){
      total += i
    }
}
  
  return total;
}
