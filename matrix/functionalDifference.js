// Given a square matrix, calculate the absolute difference between the sums of its diagonals.

// For example, the square matrix  is shown below:

// 1 2 3
// 4 5 6
// 9 8 9  
// The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

// Function description

// Complete the  function in the editor below.

// diagonalDifference takes the following parameter:

// int arr[n][m]: an array of integers


function diagonalDifference(arr) {
    // Write your code here
    let sum1 = 0;
    let sum2 = 0; 
    for(let i =0; i < arr.length; i++){
        console.log(arr[i], arr[i][i]) //arr[i][i] is the row and column
        sum1 += arr[i][i];
        sum2 += arr[i][arr.length - 1 - i]; // in reverse
        
    }
    const finalDifference = Math.abs(sum2 - sum1)
    return finalDifference;

}

let arr1 = [[11,2,4],[4,5,6],[10,8,-12]]

console.log(diagonalDifference(arr1))

//in each iteration of the loop, the row represents the current row index;
//when the row is 0, it access elements at row[0][0]
//when row is 1, it access the element at row[1][1]

//likewise for otherside, when row is 0
//it is row[0][arr.length - 1 - 0], access the last element of the first row
//for a square matrix.