//iterative

// function count(num) {
//     let total = 0;

//     while (total < num ) {
//         total++
//     }
//     return total;
// }


//recursive
function count(num) {
    if (num ===4) return "done"
  
        return count(num + 1)
   
}
console.log(count(3))

function recursiveSearch(arr, target) {
//an array of integers, and an integer (whole numbers)
//return the index found
//[-2, 3, 4, 5], 3 => 1

//iterate through the array
//if array value === target, end
//otherwise, keep iterating

if (arr[0] === target) return "done";
if (arr.length === 0) return "empty";

return recursiveSearch(arr.slice(1), target);
}

console.log(recursiveSearch([1,2,3,4], 4))