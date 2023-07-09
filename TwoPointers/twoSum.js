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

// let left = 0;
// let right = array.length - 1

// while (left < right) {
//     if (array[left] + array[right] === target) {
//         return [left, right]
//     } else if (array[left] < target) {
//         left++
//     } else {
//         right --
//     }
// }

//optimized:

    let results = {};
    
    for (let i = 0; i < array.length; i++) {
        //setting key here ; result key of 2
        // 2 = 0; keeping track of value, and the index
        //getting value of array and being set to key
        //store if it doesn't equal to the difference, store the index
        let difference = target - array[i]
        
    
    //does fridge have vegetables of carrots?
    //i is further out of object
    //return i and index you stored (carrots)
        if (results.hasOwnProperty(difference)) {
            //{ '2': 1, '3': 0 } stores the index position
            //looking for the index position
            //console.log(Object.keys(results)) // 2, 3 => the values at index position are keys
         //console.log(Object.values(results)) // 1, 0 => the index position
            return [results[difference], i]
        } else {
            //set it in the object
           results[array[i]] = i
        }
    }
    

}

console.log(twoSum([3,2,4], 6))