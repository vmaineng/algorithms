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

    return (-num)
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
return arr.reduce((a,b) => a + (b > 0 ? b : 0), 0)
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
for (let i =0; i < x.length; i++) {
    if (x[i] !== " ") {
        result += x[i]
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

function maps(x){
    return x.map((num) => num * 2)
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

for (let i = 1;i <= num ; i++) {
    total += i //add the i's since there is no num[i]
}
return total;
      }

      console.log(summation(1))