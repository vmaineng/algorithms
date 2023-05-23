const threeSum = (nums) => {
    //initialize an array to capture results

    //brute force = O(n^3)
    //three for nested loops 
    //see if i and j k = target,
    //push answer into array

    //optimized method: 
    //sort from ascending order
    //iterate through the loop
    //do two pointers on left and right
    //see if they match target


    let answer = [];
    nums.sort((a,b) => (a - b))
    
    let i = 0;
    let j = nums.length - 1;



    while (i < j) {
        if (nums[i] + nums[j] === 0) {
            answer.push(nums[i], nums[j])
            i++
            j--
        } else if {

        }
    }

    return answer

}

console.log(threeSum([-1,0,1,2,-1,-4]))