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
//identify if the value next to it is +1
//if so increase length;
//if not; reset length to 0
//return length;

const sortedArray = array.sort((a,b) => a -b );


if (array.length === 1) return 1;

let length = 0; 
let temp = 1;

for (let i = 0; i < sortedArray.length - 1; i++) {
    if (sortedArray[i+1] = sortedArray[i] + 1){
        length ++
        console.log(length);
    } else {
        length = 0
    }
}
return length;


}

console.log(longestConsecutive([100, 4, 100, 1, 3, 2,5]))