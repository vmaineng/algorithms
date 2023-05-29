const twoSumTwo = (numbers, target) => {
    //brute force: 
    //create a nested for loop to generate every possible outcomes
    //then return the values at the index if the sum matches


    //optimized method:
    //create two pointers; one from left and the other at the right;
    //check if the sum at the two pointers index == sum,
    //if so return it

//starting the array at index 1 instead of 0

    let left = 0;
    let right = numbers.length -1;

    while (left < right) {
        let sum = numbers[left] + numbers[right]

        if (sum === target) {
            return [left, right]
        } else if (sum > target) {
            right--
        } else [
            left++
        ]
    }
}

console.log(twoSumTwo([2,3,4], 6))