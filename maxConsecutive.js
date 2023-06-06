const maxConsecutive = (nums) => {
    //brute force: 
    //create a current to keep track of the max:
    //check the value at each index
    //if they are the same, store them the current
    //then get the max out of current one that is stored vs the current one right now


    //optimized method: 
    //create a current to keep track of the max:

    let maxSum = 0;
    let currentSum = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] ===1) {
            currentSum += 1
            console.log(currentSum)
        } else {
            maxSum = Math.max(maxSum, currentSum)
            //reset currentSum back to 0
            currentSum = 0;
        }
    }
    return maxSum
}

console.log(maxConsecutive([1,0,1,1,0,1]))