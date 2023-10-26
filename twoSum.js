var twoSum = function(nums, target) {
    //an array of integers (nums), and a target (integer)
    //could be positive or negative
    //return the the index of the values
    //[-1, 0, 4, -3, 2], -4 => [0, 3]
    //[1, 1], 2 => [] b/c can't return the same element twice
    
    //iterate through the entire array
    //check to see if this the first index + second index's values = target
    //if so, return the index of the value
    //else return null;
    
    // for (let i = 0; i < nums.length; i++) {
    //     for (let j = i + 1; j < nums.length; j++) {
    //         if (nums[i] + nums[j] === target){
    //             return [i, j]
    //         }
    //     }
    // }
    //  return null; 
    
    //time: O (n^2)
    //space: O(1) - no extra memory created

    //optimized:
    //use a Set to capture the array of nums in to show
    //only unique values
    //iterate through and see if Set has the difference
    //then return the indices

    //using a Set will distort the index positions

    //use an object
    //iterate through the array
    //store the index position in the object as the value
    //then return index
    //else if we have never seen it, store it in

    let answer = new Map();

    for (let i = 0; i < nums.length; i++) {
        let difference = nums[i] - target
        if (answer.has(difference)) {

            console.log(answer, answer.get(difference))
            return [i, answer.get(difference)] //get the differencce
        } else {
            answer.set(nums[i], i) //set the values, and the index
        }
    }

    
    };

    console.log(twoSum([2,7,11,15], 9))