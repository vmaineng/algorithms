const longestConsecutive = (array) => {
//get an array of numbers; could be positive or negative numbers
//return the length of the longest consecutive sequence listed
//[-4, 14, 12, -3, -5, 1, 0] => [-5, -4, -3]

//if array has one element = return length as 1
//if array has two element, see if the second element comes before or after the first element
//if so, return length as two, else return length as 1;

//initialize a length to keep track of current longest sequence
//sort array
//iterate through array
//identify if the value next to it is +1 and -1 (prefix and postfix)
//if so increase length;
//if not; reset length to 0
//return length;

// const sortedArray = array.sort((a,b) => a -b );


if (array.length === 1) return 1;

let length = 1; 
let maxLength = 1; //start maxlength at 1 to account for the first number;


//old solution
// for (let i = 0; i < sortedArray.length - 1; i++) {
//     if (sortedArray[i+1] === sortedArray[i] + 1){
//         length ++
//         maxLength = Math.max(maxLength, length)
//         console.log(length);
//     } else  {
//         length = 1
        
//     }
// }
// return maxLength;

//to account for post and prefix
for (let i = 0; i < array.length - 1; i++){
    if (array[i] === array[i + 1] - 1) {
        length++
        maxLength =Math.max(length, maxLength)
    } else if ( array[i] === array[i + 1] ) {
        length++
        
    } else {
        length = 1
        maxLength =Math.max(length, maxLength)
    }
}
return maxLength

}

console.log(longestConsecutive([100, 4, 100, 1, 3, 2,5]))