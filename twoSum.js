function twoSum(array, target) {
//take in an array, target
//return the target indices
//[0, 1 , 2, 3], 3 => 1, 2 b/c of the first incident

//iterate through the array
//add each index to the next index
//check if sum of the two index are equaled to the target
//return the indices located at the value

// for (let i = 0; i < array.length; i++) {
//     for (let j = i + 1; j < array.length; j++) {
//         if (array[i] + array[j] === target) {
//             // console.log(i, j)
//             return [i,j]
//         }
//     }
// }

//optimized solution:

let left = 0;
let right = array.length - 1

while (left < right) {
    if (array[left] + array[right] === target) {
        return [left, right]
    } else if (array[left] < target) {
        left++
    } else {
        right --
    }
}

}

console.log(twoSum([3,2,4], 6))