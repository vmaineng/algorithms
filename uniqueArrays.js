// Return the number of unique arrays that can be 
// formed by picking exactly one element from each subarray.

// For example: solve([[1,2],[4],[5,6]]) = 4, 
// because it results in only 4 possibilites. 
// They are [1,4,5],[1,4,6],[2,4,5],[2,4,6].

// Make sure that you don't count duplicates;
//  for example solve([[1,2],[4,4],[5,6,6]]) = 4, 
//  since the extra outcomes are just duplicates.

// solve([[1,2],[4],[5,6]]),4)
// solve([[1,2],[4,4],[5,6,6]]),4)
// solve([[1,2],[3,4],[5,6]]),8)
// solve([[1,2,3],[3,4,6,6,7],[8,9,10,12,5,6]]),72)


function solve(array) {
//an array of array fillled with integers
//return total amount of unique arrays that can be formed

//[[1,2], [4]] => [1,4], [2,4] => 2

//initialize an amount to keep track of unique arrays made
//iterate through array in the Set


let count = 0; 

let uniqueSet = new Set(array)

for (let i = 0; i < uniqueSet.length; i++) {
    
}

}

console.log(solve([[1,2],[4],[5,6]]))