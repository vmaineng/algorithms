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

console.log(makeNegative(-4))