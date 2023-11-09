// Sort an Array of numbers using selection sort. The selection sort 
// algorithm sorts an array by repeatedly finding the minimum element
//  (lowest value) in the input Array, and then putting it at the correct 
//  location in the sorted Array.

// Input: [3, -1, 5, 2]
// Output: [-1, 2, 3, 5]

function selectionSort(arr) {
    //array of whole integers
    //return the array sorted using selection sort - find min value first
    //[90, -3424, 34, -259, 668] => [-3424, -259, 34, 90, 668]

    //initalize a new array
    //find min value
    //push into the new array
    //return array

    //time: O(n)
    //space: O(n)

let sortedArray = [];

for (let element of arr) {
    if (arr[element] > 0) {
        sortedArray.push(element)
    }
}
return sortedArray

}

console.log(selectionSort([]))