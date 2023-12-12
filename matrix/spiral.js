const myArray = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]

function spiral(matrix) {
    //an array of array = 2d array
    //return 1D array of numbers in order
    
    //initialize an array to capture the result
    //identify the upper and lower bounds
    //while the endRow does not cross the startRow & endCol does not cross startCol
    //push in the values from the first row
    //increase the startrow index

const result = [];

//identify upper and lower bounds
    const rowCount = matrix.length;
    const columnCount = matrix[0].length;
    let startRow = 0;
    let endRow = rowCount - 1;
    let startColumn = 0;
    let endColumn = columnCount - 1;

while (endRow >= startRow && endColumn >= startColumn) {

    for(let column = startColumn; column <= endColumn; column++) {
        //console.log(matrix[startRow]) //matrix[0]
         //console.log(matrix[startRow][column]) //matrix[0][i] /the first row and move to the other column
        result.push(matrix[startRow][column])
    }
    //increment our start row since we visited each value
    startRow++;
   
    for (let row = startRow; row <= endRow; row++) {
        //console.log(matrix[row]) //grab the second row
        //console.log(matrix[row][endColumn]) //grabs last digit from the end column
        result.push(matrix[row][endColumn])
    }
    //move the endcolumn in by one since we visited all the values on the right
    endColumn--;

//since we incremented the startRow, we need to make sure we have not crossed to bottom row
if (endRow >= startRow) {
    for (let column= endColumn; column >= startColumn; column--) {
        result.push(matrix[endRow][column])
    }
}
//move it up by one, since we visited the bottom numbers
endRow--;

//verify the columns have not crossed
if (endColumn >= startColumn) {
    //add in numbers bottom-up for the start column
    for (let row = endRow; row >= startRow; row--) {
        result.push(matrix[row][startColumn])
    }
}
//increment the column in since we have visited it already
startColumn++;

}
return result;

}

console.log(spiral(myArray))