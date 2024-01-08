const containDups = (array) => {
//an array of integers - positive and negative
//return true if value appears twice, else return false if all unique
//[2, -2, 4, -2] => true

//if only one value, return false
//if only two values, return true if they are equal to each other, else return false

if (array.length === 1) return false;
if (array.length === 2) {
    if (array[0] === array[1]) {
        return true;
    } else {
        return false;
    }
}

//brute force - use sorting method
//time: O(n log n)
//space: O(1)

//sort the values
//check if the value next to it are equal to each other return true, 
//else return false

// array.sort((a,b) => a - b);

// for (let i = 0; i < array.length; i++) {
//     console.log(array)
//     if (array[i] === array[i + 1]) {
//         return true;
//     } else {
//         return false;
//     }
// }

//optimized
//use a set to store the number
//ask set if it has the number, return true;
//else return false;
//time: O(n)
//space: O (n)

let count = new Set();

for (const num of array) {
    console.log(count)
    if (count.has(num)) {
        return true;
    } else {
        count.add(num)
    }
}
return false;

}



console.log(containDups([2, -2, 4, -2]))