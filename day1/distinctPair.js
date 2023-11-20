// Given an input Array and a target value k, return all distinct pairs of 
// consecutive numbers that add up to k. A pair is distinct if no other pair 
// contains the same numbers. The order of the pairs and order of the values 
// in each pair does not matter, e.g. we consider [[2, 8], [7, 3]] to be the
//  same as [[3, 7], [8, 2]].

function distinct(array, target) {
//get an array of positive & whole integers, and a positive&whole integer
//return back the pair values and ensure the pair values are different from the other pair
//[9, 4, 5, ,-3, 5], 9 => [ 4, 5]

//edge cases: if the array is less than 1, can't make a pair

//intialize a result array to capture pairs
//iterate
//see if it adds up to target
//push into the result array
//return it

if (array.length < 2) return "pair cannot be found";

// let result =[];

// for (let i = 0; i < array.length; i++) {
//     if (array[i] + array[i + 1] === target) {
//         result.push([array[i], array[i + 1]]) //initializing array outside will help create separate arrays
//     }
// }
// return result

//optimized
//use a set to keep track of unique pairs

//iterate
//ask if set has not seen pairs, add to the set

let result = [];
let seenSet = new Set();

for (let i = 0; i < array.length - 1; i++) {
    let currentNum = array[i];
    let nextNum = array[i + 1];
    let pair = [currentNum, nextNum]

    if (currentNum + nextNum === target && !seenSet.has(pair.toString())) {
        result.push(pair);
        seenSet.add(pair.toString())
    }
}
return result;

}

console.log(distinct([0, 1, 1, 2, 0, 1], 2))