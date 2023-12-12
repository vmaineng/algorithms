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
   
}

}

console.log(spiral(myArray))