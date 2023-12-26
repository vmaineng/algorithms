const searchSorted = (matrix, target) => {
//matrix, and a coordinate
//return the location of the coordinates


//if matrix is empty, return null;
//find the row and the column
//search until target has been found
//if greater, move column to the left
//move row down
//return the row and column

let row = 0; 
let column = matrix[0].length - 1; //column at first row

while (row < matrix.length && column >= 0) {
    if (matrix[row][column] > target) { //move column to the left
        column -= 1
    } else if ( matrix[row][column] < target) {
        row += 1 //move row down
    } else {
        return [row, column]
    }
}
return [-1, -1]
}

console.log(searchSorted())