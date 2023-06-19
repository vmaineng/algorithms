const lessTwo = (array) => {
    for (let i = 0; i < array.length - 3; i++) {
        console.log(array[i])
    }
}

console.log(lessTwo([1,2,4,3]))

//array.length: 1, 2, 4,3
//array.length - 3: 1