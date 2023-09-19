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
        sum1 += arr[i][i];
        sum2 += arr[i][arr.length - 1 - i];
    }
    const finalDifference = Math.abs(sum2 - sum1)
    return finalDifference;
    

}