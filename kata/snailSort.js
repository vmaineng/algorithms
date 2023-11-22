// Given an n x n array, return the array elements arranged from outermost 
// elements to the middle element, traveling clockwise.

// array = [[1,2,3],
//          [4,5,6],
//          [7,8,9]]
// snail(array) #=> [1,2,3,6,9,8,7,4,5]
// For better understanding, please follow the numbers of the next array 
// consecutively:

// array = [[1,2,3],
//          [8,9,4],
//          [7,6,5]]
// snail(array) #=> [1,2,3,4,5,6,7,8,9]

const snail = (array) => {
 // an array of array of integers
  //return one array of integers going clockwise to the middle
  
  //iterate through the array
  //push the first row
  //get the right side items
  //push the bottom (reverse the numbers)
  //get the left side numbers

  let finalArray = [];
  while (array.length) { //while array is not empty
    finalArray.push(...array.shift()) //captures the first row

    for (let i = 0; i < array.length; i++) { //captures the right side numbers
        finalArray.push(array[i].pop());
    }
    
    finalArray.push(...(array.pop() || []).reverse()) //grab bottom row

    for (let i = array.length - 1; i >= 0; i--) { //grab left column
        finalArray.push(array[i].shift())//
    }
  }
}


console.log(snail([[1,2,3],
    [4,5,6],
    [7,8,9]]))
