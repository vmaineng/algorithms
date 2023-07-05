const longestOnes = (nums, k) => {
    if (nums < k) return ;

    let count = 0; 
    let start = 0; 
    let longest = 0;
    let flip = k;

    for (let end = 0; end < nums.length; end++) {
        const item = nums[end]

        if (item === 1) {
            count++
        } else if (item === 0 && flip !== 0) {
            count++;
            //deduct a chance to flip
            flip--;
        } else {
            // longest = Math.max(count, longest);
            // console.log(longest)
            //start a new window
            end = start;
            start++
            count = 0;
            flip = k;
            console.log(flip)
        }

    }
    longest = Math.max(count, longest);
    // console.log(longest)
    return longest

}

console.log(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))