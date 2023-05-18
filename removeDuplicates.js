const removeDuplicates = (nums) => {
    //input: array
    //output: how many numbers are unique; integer

    //brute force - for nested loops of i and j to keep track of each number
    //next to each other
    //keep track of how many unique numbers I find

    let i = 0;
  for (let j = 1; j < nums.length; j++) {
    if (nums[i] !== nums[j]) {

      i++;
      //move i pointer
      nums[i] = nums[j];
      //reassign the value of where i pointer is the the value of j's poitner

    }
  }
  console.log(i)
  //i is pointing to previous value and needs to finish iterating through rest of array
  return i + 1;


}

console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))